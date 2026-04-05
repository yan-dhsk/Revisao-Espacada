def deletar_materia (cursor, m_id):
    cursor.execute("DELETE FROM materias WHERE m_id = (?)", (m_id, ))
    return True

def deletar_assunto (cursor, a_id):
    cursor.execute("DELETE FROM assuntos WHERE a_id = (?)", (a_id, ))
    return True

def deletar_topico (cursor, t_id):
    cursor.execute("DELETE FROM topicos WHERE t_id = (?)", (t_id, ))
    return True

def deletar_subtopico (cursor, s_id):
    cursor.execute("DELETE FROM subtopico WHERE s_id = (?)", (s_id, ))
    return True