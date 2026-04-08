import tkinter as tk
import sqlite3
from datetime import date

bancoDados = sqlite3.connect("Revisões.db")
cursor = bancoDados.cursor()

largura = 800
altura = 600

def tela_principal():
    root = tk.Tk()
    root.title("Revisões espaçadas")
    root.geometry(f"{largura}x{altura}")

    inicio = tk.Label(root, text="Bem-Vindo", font=("Arial", 28))
    inicio.pack()

    hoje = tk.Label(root, text="Revisar hoje:", font=("Arial", 14))
    hoje.place(x= (largura*0.025), y=(altura*0.125))

    desenhar_revisoes_hoje(root)

    root.mainloop()

def desenhar_revisoes_hoje(root):
    
    cursor.execute("SELECT s_nome, t_id FROM subtopico WHERE data_revisar = (?)", (date.today(), ))
    
    subtopicos = cursor.fetchall()
    topicos = []
    assuntos = []
    materias = []

    for x in range (len(subtopicos)):
        cursor.execute("SELECT t_nome, a_id FROM topicos WHERE t_id = (?)", (subtopicos[x][1], ))
        topicos.append(cursor.fetchall())

    for x in range (len(topicos)):
        cursor.execute("SELECT a_nome, m_id FROM assuntos WHERE a_id = (?)", (topicos[x][0][1], ))
        assuntos.append(cursor.fetchall())

    for x in range (len(assuntos)):
        cursor.execute("SELECT m_nome FROM materias WHERE m_id = (?)", (assuntos[x][0][1], ))
        materias.append(cursor.fetchall())

    espaço = 300
    indice = 0

    while True:
        if subtopicos != None and indice < len(subtopicos):
            revisao3 = tk.Label(root, text=materias[indice][0], font=("Arial", 10))
            revisao3.place(x= ((largura + 400)*0.025), y=((altura + espaço)*0.125))

            revisao2 = tk.Label(root, text=assuntos[indice][0][0], font=("Arial", 10))
            revisao2.place(x= ((largura + 5900)*0.025), y=((altura + espaço)*0.125))
            
            revisao1 = tk.Label(root, text=topicos[indice][0][0], font=("Arial", 10))
            revisao1.place(x= ((largura + 11400)*0.025), y=((altura + espaço)*0.125))

            revisao = tk.Label(root, text=subtopicos[indice][0], font=("Arial", 10))
            revisao.place(x= ((largura + 16900)*0.025), y=((altura + espaço)*0.125))

            espaço += 200
            indice += 1
        else:
            break;

tela_principal()