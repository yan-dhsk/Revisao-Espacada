import sqlite3

def adicionar_materia(cursor, nome):
    cursor.execute("INSERT INTO materias (m_nome) VALUES (?)", (nome,))

def adicionar_assunto(cursor, m_nome, nome):
    cursor.execute("SELECT m_id FROM materias WHERE m_nome = (?)", (m_nome,))
    m_id0 = cursor.fetchone()
    if m_id0:
        m_id = m_id0[0]
        cursor.execute("INSERT INTO assuntos (m_id, a_nome) VALUES (?, ?)", (m_id, nome))
        return True
    else:
        return False

def adicionar_topico(cursor, a_nome, nome):
    cursor.execute("SELECT a_id FROM assuntos WHERE a_nome = (?)", (a_nome,))
    a_id0 = cursor.fetchone()
    if a_id0:
        a_id = a_id0[0]
        cursor.execute("INSERT INTO topicos (a_id, t_nome) VALUES (?, ?)", (a_id, nome))
        return True
    else:
        return False

def adicionar_subtopico(cursor, t_nome, nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar):
    cursor.execute("SELECT t_id FROM topicos WHERE t_nome = (?)", (t_nome,))
    t_id0 = cursor.fetchone()
    if t_id0:
        t_id = t_id0[0]
        cursor.execute("INSERT INTO subtopico (t_id, s_nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar) VALUES (?, ?, ?, ?, ?, ?)", (t_id, nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar))
        return True
    else:
        return False