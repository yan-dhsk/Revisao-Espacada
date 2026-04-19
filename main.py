import sqlite3
from interface import modulo_interface_telaPrincipal

bancoDados = sqlite3.connect("Revisões.db")
cursor = bancoDados.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("CREATE TABLE IF NOT EXISTS materias (m_id INTEGER PRIMARY KEY AUTOINCREMENT,  m_nome TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS assuntos (a_id INTEGER PRIMARY KEY AUTOINCREMENT,  m_id INTEGER, a_nome TEXT, FOREIGN KEY (m_id) REFERENCES materias(m_id)ON DELETE CASCADE)")
cursor.execute("CREATE TABLE IF NOT EXISTS topicos (t_id INTEGER PRIMARY KEY AUTOINCREMENT, a_id INTEGER, t_nome TEXT, FOREIGN KEY (a_id) REFERENCES assuntos(a_id) ON DELETE CASCADE)")
cursor.execute("CREATE TABLE IF NOT EXISTS subtopico (s_id INTEGER PRIMARY KEY AUTOINCREMENT, t_id INTEGER, s_nome TEXT, data_estudo DATE, ultima_revisao DATE, numero_revisoes INTEGER, data_revisar DATE, FOREIGN KEY (t_id) REFERENCES topicos(t_id) ON DELETE CASCADE)")

modulo_interface_telaPrincipal.tela_principal(cursor, bancoDados)

bancoDados.close()
