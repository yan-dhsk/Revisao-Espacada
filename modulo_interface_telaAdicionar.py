import tkinter as tk
import sqlite3
from datetime import date
import modulo_add

bancoDados = sqlite3.connect("Revisões.db")
cursor = bancoDados.cursor()

largura = 250
altura = 340

def tela_adicionar():
    root = tk.Tk()
    root.title("Adicionar")
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)

    dados_revisao = desenhar_tela_adicionar(root)
    desenhar_botao(root, dados_revisao)

    root.mainloop()

def desenhar_botao(root, dados_revisao):
    adicionar = tk.Button(root, text="Adicionar", fg="white", bg="blue", width=20, height=2, command=lambda : [modulo_add.adicionar_materia(dados_revisao[0].get()), modulo_add.adicionar_assunto(dados_revisao[1].get()), modulo_add.adicionar_topico(dados_revisao[2].get()), modulo_add.adicionar_subtopico(dados_revisao[3].get())])
    tk.Label().grid(column=0, row=11)
    adicionar.grid(column=0, row=12)

def desenhar_tela_adicionar(root):
    materia = tk.Label(root, text="Digite o nome da máteria:", font=("Arial", 14))
    materia.grid(column = 0, row= 0, sticky="w")

    digitar_materia = tk.Entry(root)
    digitar_materia.grid(column=0, row=1, padx=(4, 0), sticky="nsew")

    tk.Label().grid(column=0, row=2)

    assunto = tk.Label(root, text="Digite o nome do assunto:", font=("Arial", 14))
    assunto.grid(column = 0, row= 3, sticky="w")

    digitar_assunto = tk.Entry(root )
    digitar_assunto.grid(column=0, row=4, padx=(4, 0), sticky="nsew")

    tk.Label().grid(column=0, row=5)

    topico = tk.Label(root, text="Digite o nome do tópico:", font=("Arial", 14))
    topico.grid(column = 0, row= 6, sticky="w")

    digitar_topico = tk.Entry(root )
    digitar_topico.grid(column=0, row=7, padx=(4, 0), sticky="nsew")

    tk.Label().grid(column=0, row=8)

    subtopico = tk.Label(root, text="Digite o nome do subtópico:", font=("Arial", 14))
    subtopico.grid(column = 0, row= 9, sticky="w")

    digitar_subtopico = tk.Entry(root )
    digitar_subtopico.grid(column=0, row=10, padx=(4, 0), sticky="nsew")

    return [digitar_materia, digitar_assunto, digitar_topico, digitar_subtopico]

tela_adicionar()
