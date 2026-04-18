import tkinter as tk
import sqlite3
from datetime import date
import modulo_update
import modulo_interface_telaAdicionar
import modulo_interface_telaRemover


largura = 800
altura = 600

destruir = []

def tela_principal(cursor, bancoDados):
    root = tk.Tk()
    root.title("Revisões espaçadas")
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)

    desenhar_tela(root, cursor, bancoDados)

    root.mainloop()

def desenhar_tela(root, cursor, bancoDados):
    global destruir

    inicio = tk.Label(root, text="Bem-Vindo", font=("Arial", 28))
    inicio.pack()
    destruir.append(inicio)

    botoes = tk.Frame(root)
    destruir.append(botoes)

    botao_adicionar = tk.Button(botoes, text="Adicionar", bg="blue", fg="white", width=10, height=2, command=lambda : modulo_interface_telaAdicionar.tela_adicionar(cursor, bancoDados, destruir, root))
    botao_editar = tk.Button(botoes, text="Editar", bg="blue", fg="white", width=10, height=2)
    botao_remover = tk.Button(botoes, text="Remover", bg="blue", fg="white", width=10, height=2, command=lambda : modulo_interface_telaRemover.tela_deletar(cursor, bancoDados, destruir, root))
    
    botao_adicionar.pack(side='left')
    botao_editar.pack(side='left', padx=(10, 0))
    botao_remover.pack(side='left', padx=(10,0))
    botoes.pack()


    hoje = tk.Label(root, text="Revisar hoje:", font=("Arial", 14))
    hoje.place(x= (largura*0.025), y=((altura+200)*0.125))
    destruir.append(hoje)

    medida_base = desenhar_revisoes(root, 800, 1, cursor, bancoDados) + 200

    revisar_depois = tk.Label(root, text="Revisar depois:", font=('Arial', 14), fg='gray')
    revisar_depois.place(x = (largura*0.025), y=((200+medida_base)*0.125))
    destruir.append(revisar_depois)

    medida_base2 = desenhar_revisoes(root, medida_base + 200, 2, cursor, bancoDados)

    revisoes_atrasadas = tk.Label(root, text="Revisões atrasadas:", font=('Arial', 14), fg='red')
    revisoes_atrasadas.place(x = (largura*0.025), y=((medida_base2+200)*0.125))
    destruir.append(revisoes_atrasadas)

    desenhar_revisoes(root, medida_base2 + 200, 3, cursor, bancoDados)


def desenhar_revisoes(root, medida_base, escolha, cursor, bancoDados):
    global destruir

    if escolha == 1:
        cursor.execute("SELECT s_nome, t_id, s_id, data_revisar FROM subtopico WHERE data_revisar = (?)", (date.today(), ))
    elif escolha == 2:
        cursor.execute("SELECT s_nome, t_id, s_id, data_revisar FROM subtopico WHERE data_revisar > (?)", (date.today(), ))
    elif escolha == 3:
        cursor.execute("SELECT s_nome, t_id, s_id, data_revisar FROM subtopico WHERE data_revisar < (?)", (date.today(), ))

    subtopicos = cursor.fetchall()
    topicos = []
    assuntos = []
    materias = []
    checkin = []

    for x in range (len(subtopicos)):
        cursor.execute("SELECT t_nome, a_id FROM topicos WHERE t_id = (?)", (subtopicos[x][1], ))
        topicos.append(cursor.fetchall())

    for x in range (len(topicos)):
        cursor.execute("SELECT a_nome, m_id FROM assuntos WHERE a_id = (?)", (topicos[x][0][1], ))
        assuntos.append(cursor.fetchall())

    for x in range (len(assuntos)):
        cursor.execute("SELECT m_nome FROM materias WHERE m_id = (?)", (assuntos[x][0][1], ))
        materias.append(cursor.fetchall())

    for _ in range(len(subtopicos)):
        checkin.append(tk.IntVar())

    espaço = 400
    indice = 0

    desenhar_nomes_colunas(root, largura, medida_base)

    while True:
        if subtopicos != None and indice < len(subtopicos):
            revisao3 = tk.Label(root, text=materias[indice][0], font=("Arial", 10))
            revisao2 = tk.Label(root, text=assuntos[indice][0][0], font=("Arial", 10))
            revisao1 = tk.Label(root, text=topicos[indice][0][0], font=("Arial", 10))
            revisao = tk.Label(root, text=subtopicos[indice][0], font=("Arial", 10))
            revisao4 = tk.Label(root, text=subtopicos[indice][3], font=("Arial", 10))
            destruir.extend([revisao, revisao1, revisao2, revisao3, revisao4])

            check = tk.Checkbutton(root, text='', variable=checkin[indice])
            destruir.append(check) 
            check.config(command=lambda s_id=subtopicos[indice][2]: [modulo_update.revisar(cursor, s_id), bancoDados.commit(), limpar_tela('a'), desenhar_tela(root, cursor, bancoDados)])

            revisao4.place(x= ((largura + 22400)*0.025), y=((medida_base + espaço)*0.125))
            revisao.place(x= ((largura + 16900)*0.025), y=((medida_base + espaço)*0.125))
            revisao1.place(x= ((largura + 11400)*0.025), y=((medida_base + espaço)*0.125))
            revisao2.place(x= ((largura + 5900)*0.025), y=((medida_base + espaço)*0.125))
            revisao3.place(x= ((largura + 400)*0.025), y=((medida_base + espaço)*0.125))
            check.place(x= ((largura + 27900)*0.025), y=((medida_base + espaço)*0.125))

            espaço += 200
            indice += 1
        else:
            break;
    if escolha == 1:
        return espaço + altura
    elif escolha == 2:
        return medida_base + espaço

def desenhar_nomes_colunas(root, largura, altura):
    global destruir

    materias_coluna = tk.Label(root, text="Materias", font=('Arial', 12))
    materias_coluna.place(x= ((largura + 400)*0.025), y=((altura+200)*0.125))
    destruir.append(materias_coluna)

    assuntos_coluna = tk.Label(root, text="Assuntos", font=('Arial', 12))
    assuntos_coluna.place(x= ((largura + 5900)*0.025), y=((altura+200)*0.125))
    destruir.append(assuntos_coluna)

    topicos_coluna = tk.Label(root, text="Tópicos", font=('Arial', 12))
    topicos_coluna.place(x= ((largura + 11400)*0.025), y=((altura+200)*0.125))   
    destruir.append(topicos_coluna)

    subtopicos_coluna = tk.Label(root, text="Subtópicos", font=('Arial', 12))
    subtopicos_coluna.place(x= ((largura + 16900)*0.025), y=((altura+200)*0.125))  
    destruir.append(subtopicos_coluna)

    datas_revisar_coluna = tk.Label(root, text="Data", font=('Arial', 12))
    datas_revisar_coluna.place(x= ((largura + 22400)*0.025), y=((altura+200)*0.125))  
    destruir.append(datas_revisar_coluna)

    linha = tk.Canvas(root, width=660, height=2, bg="#000000")
    linha.place(x= ((largura + 400)*0.025), y=((altura+360)*0.125))
    linha.create_line(0, 0, 700, 0, fill="#000000", width=2)
    destruir.append(linha)

def limpar_tela(destruir2):
    global destruir
    if destruir2 == 'a':
        for x in range (len(destruir)):
            destruir[x].destroy()
        destruir.clear()
    else:
        for x in range (len(destruir2)):
            destruir2[x].destroy()
        destruir2.clear()