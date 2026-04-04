from datetime import date, timedelta

def alterar_nome_materia(cursor, m_id, novo_nome):
    cursor.execute("SELECT m_nome FROM materias WHERE m_nome = (?)", (novo_nome, ))
    nome = cursor.fetchone()
    if nome:
        return False
    else:
        cursor.execute("UPDATE materias SET m_nome = (?) WHERE m_id = (?)", (novo_nome, m_id))

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

def alterar_data_revisao_subtopico(cursor, s_id, data_nova):
    cursor.execute("SELECT ultima_revisao FROM subtopico WHERE s_id = (?)", (s_id, ))
    ultima_revisao1 = cursor.fetchone()
    ultima_revisao = ultima_revisao1[0]
    if data_nova <= ultima_revisao:
        return False
    else:
        cursor.execute("UPDATE subtopico SET ultima_revisao = (?) WHERE s_id = (?)", (data_nova, s_id))


def alterar_data_revisar_subtopico(cursor, s_id, data_nova):
    cursor.execute("SELECT ultima_revisao FROM subtopico WHERE s_id = (?)", (s_id, ))
    ultima_revisao1 = cursor.fetchone()
    ultima_revisao = ultima_revisao1[0]
    if data_nova <= ultima_revisao:
        return False
    else:
        cursor.execute("UPDATE subtopico SET data_revisar = (?) WHERE s_id = (?)", (data_nova, s_id))

def revisar(cursor, s_id):
    cursor.execute("SELECT ultima_revisao, data_estudo, numero_revisoes, data_revisar FROM subtopico WHERE s_id = (?)", (s_id, ))
    datas0 = cursor.fetchone()
    if datas0[2] == 0:
        data_revisar = datas0[0] + timedelta(days=1)
    elif datas0[2] == 1:
        data_revisar = datas0[0] + timedelta(days=6)
    else:
        intervalo = int(((datas0[0] - datas0[1]).days)*2.5)
        data_revisar = datas0[0] + timedelta(days=intervalo)
    numero_revisoes = datas0[2] + 1
    cursor.execute("UPDATE subtopico SET ultima_revisao = (?), numero_revisoes = (?), data_revisar = (?) WHERE s_id = (?)", (date.today(), numero_revisoes, data_revisar, s_id))
    return True