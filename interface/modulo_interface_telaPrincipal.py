import tkinter as tk
import sqlite3
from datetime import date
from lógica import modulo_update
from interface import modulo_interface_telaAdicionar
from interface import modulo_interface_telaRemover
from interface import modulo_interface_telaEditar


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
    botao_editar = tk.Button(botoes, text="Editar", bg="blue", fg="white", width=10, height=2, command=lambda : modulo_interface_telaEditar.tela_editar(cursor, bancoDados, destruir, root))
    botao_remover = tk.Button(botoes, text="Remover", bg="blue", fg="white", width=10, height=2, command=lambda : modulo_interface_telaRemover.tela_deletar(cursor, bancoDados, destruir, root))
    
    botao_adicionar.pack(side='left')
    botao_editar.pack(side='left', padx=(10, 0))
    botao_remover.pack(side='left', padx=(10,0))
    botoes.pack()

    canvas_scroll = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas_scroll.yview)
    frame_conteudo = tk.Frame(canvas_scroll)

    frame_id = canvas_scroll.create_window((0, 0), window=frame_conteudo, anchor='nw')
    canvas_scroll.configure(yscrollcommand=scrollbar.set)
    frame_conteudo.bind('<Configure>', lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox('all')))
    canvas_scroll.bind('<Configure>', lambda e: canvas_scroll.itemconfig(frame_id, width=e.width))

    destruir.append(canvas_scroll)
    destruir.append(scrollbar)

    scrollbar.pack(side='right', fill='y')
    canvas_scroll.pack(side='left', fill='both', expand=True)

    hoje = tk.Label(frame_conteudo, text="Revisar hoje:", font=("Arial", 14))
    hoje.grid(column=0, row=0, sticky='w', pady=(5, 0))

    frame_hoje = tk.Frame(frame_conteudo)
    frame_hoje.grid(column=0, row=1, sticky='ew')
    desenhar_revisoes(frame_hoje, 1, cursor, bancoDados, root)

    revisar_depois = tk.Label(frame_conteudo, text="Revisar depois:", font=('Arial', 14), fg='gray')
    revisar_depois.grid(column=0, row=2, sticky='w', pady=(10, 0))

    frame_depois = tk.Frame(frame_conteudo)
    frame_depois.grid(column=0, row=3, sticky='ew')
    desenhar_revisoes(frame_depois, 2, cursor, bancoDados, root)

    revisoes_atrasadas = tk.Label(frame_conteudo, text="Revisões atrasadas:", font=('Arial', 14), fg='red')
    revisoes_atrasadas.grid(column=0, row=4, sticky='w', pady=(10, 0))

    frame_atrasadas = tk.Frame(frame_conteudo)
    frame_atrasadas.grid(column=0, row=5, sticky='ew')
    desenhar_revisoes(frame_atrasadas, 3, cursor, bancoDados, root)


def desenhar_revisoes(frame, escolha, cursor, bancoDados, root):
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

    desenhar_nomes_colunas(frame)

    indice = 0

    while True:
        if subtopicos != None and indice < len(subtopicos):
            revisao3 = tk.Label(frame, text=materias[indice][0][0], font=("Arial", 10))
            revisao2 = tk.Label(frame, text=assuntos[indice][0][0], font=("Arial", 10))
            revisao1 = tk.Label(frame, text=topicos[indice][0][0], font=("Arial", 10))
            revisao = tk.Label(frame, text=subtopicos[indice][0], font=("Arial", 10))
            revisao4 = tk.Label(frame, text=subtopicos[indice][3], font=("Arial", 10))

            check = tk.Checkbutton(frame, text='', variable=checkin[indice])
            check.config(command=lambda s_id=subtopicos[indice][2]: [modulo_update.revisar(cursor, s_id), bancoDados.commit(), limpar_tela('a'), desenhar_tela(root, cursor, bancoDados)])

            row = indice + 2
            revisao3.grid(column=0, row=row, sticky='w', padx=5)
            revisao2.grid(column=1, row=row, sticky='w', padx=5)
            revisao1.grid(column=2, row=row, sticky='w', padx=5)
            revisao.grid(column=3, row=row, sticky='w', padx=5)
            revisao4.grid(column=4, row=row, sticky='w', padx=5)
            check.grid(column=5, row=row, padx=5)

            indice += 1
        else:
            break


def desenhar_nomes_colunas(frame):
    materias_coluna = tk.Label(frame, text="Materias", font=('Arial', 12))
    materias_coluna.grid(column=0, row=0, sticky='w', padx=5)

    assuntos_coluna = tk.Label(frame, text="Assuntos", font=('Arial', 12))
    assuntos_coluna.grid(column=1, row=0, sticky='w', padx=5)

    topicos_coluna = tk.Label(frame, text="Tópicos", font=('Arial', 12))
    topicos_coluna.grid(column=2, row=0, sticky='w', padx=5)

    subtopicos_coluna = tk.Label(frame, text="Subtópicos", font=('Arial', 12))
    subtopicos_coluna.grid(column=3, row=0, sticky='w', padx=5)

    datas_revisar_coluna = tk.Label(frame, text="Data", font=('Arial', 12))
    datas_revisar_coluna.grid(column=4, row=0, sticky='w', padx=5)

    linha = tk.Canvas(frame, width=660, height=2, bg="#000000")
    linha.grid(column=0, row=1, columnspan=6, sticky='ew')
    linha.create_line(0, 0, 700, 0, fill="#000000", width=2)

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
