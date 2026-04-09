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
    hoje.place(x= (largura*0.025), y=((altura)*0.125))

    medida_base = desenhar_revisoes_hoje(root) + 200
    desenhar_revisar_depois(root, medida_base)

    root.mainloop()

def desenhar_revisar_depois(root, medida_base):
    cursor.execute("SELECT s_nome, t_id FROM subtopico WHERE data_revisar > (?)", (date.today(), ))

    revisar_depois = tk.Label(root, text="Revisar depois:", font=('Arial', 14))
    revisar_depois.place(x = (largura*0.025), y=(medida_base*0.125))

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

    espaço = 400
    indice = 0

    desenhar_nomes_colunas(root, largura, medida_base)

    while True:
        if subtopicos != None and indice < len(subtopicos):
            revisao3 = tk.Label(root, text=materias[indice][0], font=("Arial", 10))
            revisao3.place(x= ((largura + 400)*0.025), y=((medida_base + espaço)*0.125))

            revisao2 = tk.Label(root, text=assuntos[indice][0][0], font=("Arial", 10))
            revisao2.place(x= ((largura + 5900)*0.025), y=((medida_base + espaço)*0.125))
            
            revisao1 = tk.Label(root, text=topicos[indice][0][0], font=("Arial", 10))
            revisao1.place(x= ((largura + 11400)*0.025), y=((medida_base + espaço)*0.125))

            revisao = tk.Label(root, text=subtopicos[indice][0], font=("Arial", 10))
            revisao.place(x= ((largura + 16900)*0.025), y=((medida_base + espaço)*0.125))

            espaço += 200
            indice += 1
        else:
            break;

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

    espaço = 400
    indice = 0

    desenhar_nomes_colunas(root, largura, altura)

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

    return espaço + altura

def desenhar_nomes_colunas(root, largura, altura):
    materias_coluna = tk.Label(root, text="Materias", font=('Arial', 12))
    materias_coluna.place(x= ((largura + 400)*0.025), y=((altura+200)*0.125))

    assuntos_coluna = tk.Label(root, text="Assuntos", font=('Arial', 12))
    assuntos_coluna.place(x= ((largura + 5900)*0.025), y=((altura+200)*0.125))

    topicos_coluna = tk.Label(root, text="Tópicos", font=('Arial', 12))
    topicos_coluna.place(x= ((largura + 11400)*0.025), y=((altura+200)*0.125))   

    subtopicos_coluna = tk.Label(root, text="Subtópicos", font=('Arial', 12))
    subtopicos_coluna.place(x= ((largura + 16900)*0.025), y=((altura+200)*0.125))  

    linha = tk.Canvas(root, width=560, height=2, bg="#000000")
    linha.place(x= ((largura + 400)*0.025), y=((altura+360)*0.125))
    linha.create_line(0, 0, 700, 0, fill="#000000", width=2)

tela_principal()