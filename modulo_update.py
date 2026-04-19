from datetime import date, timedelta

def alterar_nome_materia(cursor, m_id, novo_nome):
    cursor.execute("UPDATE materias SET m_nome = (?) WHERE m_id = (?)", (novo_nome, m_id))
    return True

def alterar_nome_assunto(cursor, a_id, novo_nome):
    cursor.execute("SELECT m_id FROM assuntos WHERE a_id = (?)", (a_id, ))
    id_materia1 = cursor.fetchone()
    id_materia = id_materia1[0]
    cursor.execute("SELECT a_nome FROM assuntos WHERE a_nome = (?) and m_id = (?)", (novo_nome, id_materia))
    nome = cursor.fetchone()
    if nome:
        return False
    else:
        cursor.execute("UPDATE assuntos SET a_nome = (?) WHERE a_id = (?)", (novo_nome, a_id))
        return True
    
def alterar_materia_assunto(cursor, a_id, novo_m_id):
    cursor.execute("UPDATE assuntos SET m_id = (?) WHERE a_id = (?)", (novo_m_id, a_id))

def alterar_nome_topico(cursor, t_id, novo_nome):
    cursor.execute("SELECT a_id FROM topicos WHERE t_id = (?)", (t_id, ))
    id_assunto1 = cursor.fetchone()
    id_assunto = id_assunto1[0]
    cursor.execute("SELECT t_nome FROM topicos WHERE t_nome = (?) AND a_id = (?)", (novo_nome, id_assunto))
    nome = cursor.fetchone()
    if nome:
        return False
    else:
        cursor.execute("UPDATE topicos SET t_nome = (?) WHERE t_id = (?)", (novo_nome, t_id))
        return True

def alterar_assunto_topico(cursor, t_id, novo_a_id):
    cursor.execute("UPDATE topicos SET a_id = (?) WHERE t_id = (?)", (novo_a_id, t_id))

def alterar_nome_subtopico(cursor, s_id, novo_nome):
    cursor.execute("SELECT t_id FROM subtopico WHERE s_id = (?)", (s_id, ))
    id_topico1 = cursor.fetchone()
    id_topico = id_topico1[0]
    cursor.execute("SELECT s_nome FROM subtopico WHERE s_nome = (?) AND t_id = (?)", (novo_nome, id_topico))
    nome = cursor.fetchone()
    if nome:
        return False
    else:
        cursor.execute("UPDATE subtopico SET s_nome = (?) WHERE s_id = (?)", (novo_nome, s_id))
        return True
    
def alterar_data_revisar_subtopico(cursor, s_id, data_nova):
    try:
        date.fromisoformat(data_nova)
    except ValueError:
        return False

    cursor.execute("SELECT ultima_revisao FROM subtopico WHERE s_id = (?)", (s_id,))
    ultima_revisao1 = cursor.fetchone()
    ultima_revisao = ultima_revisao1[0]
    if ultima_revisao is None:
        ultima_revisao = date.today().isoformat()
    if data_nova < ultima_revisao:
        return False
    else:
        cursor.execute("UPDATE subtopico SET data_revisar = (?) WHERE s_id = (?)", (data_nova, s_id))
        return True
    
def revisar(cursor, s_id):
    cursor.execute("SELECT ultima_revisao, data_estudo, numero_revisoes, data_revisar FROM subtopico WHERE s_id = (?)", (s_id, ))
    dados = cursor.fetchone()
    
    ultimaRevisao = dados[0]
    dataEstudo = dados[1]
    numeroRevisoes = dados[2]
    dataRevisar = dados[3]
    
    if ultimaRevisao is None:
        if dataEstudo is not None:
            ultimaRevisao = dataEstudo
        else:
            ultimaRevisao = date.today().isoformat()
            
    if dataEstudo is None:
        dataEstudo = date.today().isoformat()
    
    if dataRevisar is not None:
        dataRevisaoEfetiva = dataRevisar
    else:
        dataRevisaoEfetiva = date.today().isoformat()
    
    if numeroRevisoes == 0:
        novaDataRevisar = date.fromisoformat(str(dataRevisaoEfetiva)) + timedelta(days=1)
    elif numeroRevisoes == 1:
        novaDataRevisar = date.fromisoformat(str(dataRevisaoEfetiva)) + timedelta(days=6)
    else:
        diasPassados = (date.fromisoformat(str(dataRevisaoEfetiva)) - date.fromisoformat(str(dataEstudo))).days
        intervalo = int(diasPassados * 2.5)
        
        if intervalo <= 0:
            intervalo = 1
            
        novaDataRevisar = date.fromisoformat(str(dataRevisaoEfetiva)) + timedelta(days=intervalo)
        
    numeroRevisoesNovo = numeroRevisoes + 1
    
    cursor.execute(
        "UPDATE subtopico SET ultima_revisao = (?), numero_revisoes = (?), data_revisar = (?) WHERE s_id = (?)", 
        (dataRevisaoEfetiva, numeroRevisoesNovo, novaDataRevisar, s_id)
    )
    return True