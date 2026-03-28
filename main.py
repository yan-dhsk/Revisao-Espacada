import sqlite3
import modulo_add

estudo = sqlite3.connect("Revisões.db")
cursor = estudo.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS materias (m_id INTEGER PRIMARY KEY AUTOINCREMENT,  m_nome TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS assuntos (a_id INTEGER PRIMARY KEY AUTOINCREMENT,  m_id INTEGER, a_nome TEXT, FOREIGN KEY (m_id) REFERENCES materias(m_id))")
cursor.execute("CREATE TABLE IF NOT EXISTS topicos (t_id INTEGER PRIMARY KEY AUTOINCREMENT, a_id INTEGER, t_nome TEXT, FOREIGN KEY (a_id) REFERENCES assuntos(a_id))")
cursor.execute("CREATE TABLE IF NOT EXISTS subtopico (s_id INTEGER PRIMARY KEY AUTOINCREMENT, t_id INTEGER, s_nome TEXT, data_estudo DATE, ultima_revisao DATE, numero_revisoes INTEGER, data_revisar DATE, FOREIGN KEY (t_id) REFERENCES topicos(t_id))")

estudo.commit()
