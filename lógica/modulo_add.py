from datetime import date

def adicionar_materia(cursor, nome):
    cursor.execute("SELECT m_id FROM materias WHERE m_nome = (?)", (nome,))
    if cursor.fetchone():
        return True
    cursor.execute("INSERT INTO materias (m_nome) VALUES (?)", (nome,))
    return True

def adicionar_assunto(cursor, m_nome, nome):
    cursor.execute("SELECT m_id FROM materias WHERE m_nome = (?)", (m_nome,))
    m_id0 = cursor.fetchone()
    if m_id0:
        m_id = m_id0[0]
        cursor.execute("SELECT a_id FROM assuntos WHERE a_nome = (?) AND m_id = (?)", (nome, m_id))
        if cursor.fetchone():
            return True
        cursor.execute("INSERT INTO assuntos (m_id, a_nome) VALUES (?, ?)", (m_id, nome))
        return True
    else:
        return False

def adicionar_topico(cursor, m_nome, a_nome, nome):
    cursor.execute("""
        SELECT a.a_id FROM assuntos a
        JOIN materias m ON a.m_id = m.m_id
        WHERE a.a_nome = ? AND m.m_nome = ?
    """, (a_nome, m_nome))
    a_id0 = cursor.fetchone()
    if a_id0:
        a_id = a_id0[0]
        cursor.execute("SELECT t_id FROM topicos WHERE t_nome = ? AND a_id = ?", (nome, a_id))
        if cursor.fetchone():
            return True
        cursor.execute("INSERT INTO topicos (a_id, t_nome) VALUES (?, ?)", (a_id, nome))
        return True
    else:
        return False

def adicionar_subtopico(cursor, m_nome, a_nome, t_nome, nome):
    cursor.execute("""
        SELECT t.t_id FROM topicos t
        JOIN assuntos a ON t.a_id = a.a_id
        JOIN materias m ON a.m_id = m.m_id
        WHERE t.t_nome = ? AND a.a_nome = ? AND m.m_nome = ?
    """, (t_nome, a_nome, m_nome))
    t_id0 = cursor.fetchone()
    if t_id0:
        t_id = t_id0[0]
        cursor.execute("SELECT s_id FROM subtopico WHERE t_id = ? AND s_nome = ?", (t_id, nome))
        if cursor.fetchone():
            return False
        data_hoje = date.today()
        cursor.execute(
            "INSERT INTO subtopico (t_id, s_nome, data_estudo, ultima_revisao, numero_revisoes, data_revisar) VALUES (?, ?, ?, ?, ?, ?)",
            (t_id, nome, data_hoje, data_hoje, 0, data_hoje)
        )
        return True
    else:
        return False
