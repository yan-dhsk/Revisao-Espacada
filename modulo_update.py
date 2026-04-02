import sqlite3
from datetime import date, timedelta

def alterar_nome_materia(cursor, m_id):
    print()

def alterar_nome_assunto(cursor, a_id):
    print()

def alterar_materia_assunto(cursor, a_id, m_id):
    print()

def alterar_nome_topico(cursor, t_id):
    print ()

def alterar_assunto_topico(cursor, t_id):
    print()

def alterar_nome_subtopico(cursor, s_id):
    print()

def alterar_data_subtopico(cursor, s_id, data_nova):
    print()

def alterar_revisoes_subtopico(cursor, s_id, revisoes):
    print()

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