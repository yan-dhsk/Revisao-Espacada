import sqlite3
from datetime import date, timedelta

def adicionar_materia(cursor, nome):
    cursor.execute("SELECT m_id FROM materias WHERE m_nome = (?)", (nome, ))
    if cursor.fetchone():
        return False
    else:
        cursor.execute("INSERT INTO materias (m_nome) VALUES (?)", (nome,))
        return True

def adicionar_assunto(cursor, m_nome, nome):
    cursor.execute("SELECT m_id FROM materias WHERE m_nome = (?)", (m_nome,))
    m_id0 = cursor.fetchone()
    if m_id0:
        m_id = m_id0[0]
        cursor.execute("SELECT m_id FROM assuntos WHERE m_id = (?) AND a_nome = (?)", (m_id, nome))
        if cursor.fetchone():
            return False
        else:
            cursor.execute("INSERT INTO assuntos (m_id, a_nome) VALUES (?, ?)", (m_id, nome))
            return True
    else:
        return False

def adicionar_topico(cursor, a_nome, nome):
    cursor.execute("SELECT a_id FROM assuntos WHERE a_nome = (?)", (a_nome,))
    a_id0 = cursor.fetchone()
    if a_id0:
        a_id = a_id0[0]
        cursor.execute("SELECT a_id FROM topicos WHERE a_id = (?) AND t_nome = (?)", (a_id, nome))
        if cursor.fetchone():
            return False
        else:
            cursor.execute("INSERT INTO topicos (a_id, t_nome) VALUES (?, ?)", (a_id, nome))
            return True
    else:
        return False

def adicionar_subtopico(cursor, t_nome, nome):
    cursor.execute("SELECT t_id FROM topicos WHERE t_nome = (?)", (t_nome,))
    t_id0 = cursor.fetchone()
    if t_id0:
        t_id = t_id0[0]
        cursor.execute("SELECT t_id FROM subtopico WHERE t_id = (?) AND s_nome = (?)", (t_id, nome))
        if cursor.fetchone():
            return False
        else:
            data_estudo = date.today()
            ultima_revisao = date.today()
            numero_revisoes = 0
            data_revisar = date.today()
            cursor.execute("INSERT INTO subtopico (t_id, s_nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar) VALUES (?, ?, ?, ?, ?, ?)", (t_id, nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar))
            return True
    else:
        return False