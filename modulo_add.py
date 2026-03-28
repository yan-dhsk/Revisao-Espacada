import sqlite3

def adicionar_materia(cursor, nome):
    cursor.execute("INSERT INTO materias (m_nome) VALUE (?)", (nome,))

def adicionar_assunto(cursor, m_nome, nome):
    cursor.execute("SELECT m_id FROM materias WHERE m_nome = (?)", (m_nome,))
    m_id0 = cursor.fetchone()
    m_id = m_id0[0]
    cursor.execute("INSERT INTO assuntos (m_id, a_nome) VALUE (?, ?)", (m_id, nome))

def adicionar_topico(cursor, a_nome, nome):
    cursor.execute("SELECT a_id FROM assuntos WHERE a_nome = (?)", (a_nome,))
    a_id0 = cursor.fetchone()
    a_id = a_id0[0]
    cursor.execute("INSERT INTO topicos (a_id, t_nome) VALUE (?, ?)", (a_id, nome))

def adicionar_subtopico(cursor, t_nome, nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar):
    cursor.execute("SELECT t_id FROM assuntos WHERE t_nome = (?)", (t_nome,))
    t_id0 = cursor.fetchone()
    t_id = t_id0[0]
    cursor.execute("INSERT INTO subtopico (t_id, s_nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar) VALUE (?, ?, ?, ?, ?, ?)", (t_id, nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar))