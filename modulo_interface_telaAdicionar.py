import tkinter as tk
import sqlite3
from datetime import date
from lógica import modulo_add

largura = 250
altura = 340

def tela_adicionar(cursor, bancoDados, destruir, root_principal):
    root = tk.Toplevel()
    root.title("Adicionar")
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)

    dados_revisao = desenhar_tela_adicionar(root)
    desenhar_botao(cursor, bancoDados, root, dados_revisao, destruir, root_principal)


def desenhar_botao(cursor, bancoDados, root, dados_revisao, destruir, root_principal):
    adicionar = tk.Button(root, text="Adicionar", fg="white", bg="blue", width=20, height=2, command=lambda : verificar(root, cursor, dados_revisao, bancoDados, destruir, root_principal))
    tk.Label(root).grid(column=0, row=11)
    adicionar.grid(column=0, row=12)

def verificar(root, cursor, dados_revisao, bancoDados, destruir, root_principal):
    valores = [d.get().strip() for d in dados_revisao]
    if any(v == "" for v in valores):
        falha = tk.Label(root, text="Preencha todos os campos!", fg="red", font=("Arial", 14))
        if root.grid_slaves(row=13, column=0):
            root.grid_slaves(row=13, column=0)[0].destroy()
        falha.grid(column=0, row=13)
        return

    a = modulo_add.adicionar_materia(cursor, valores[0])
    b = modulo_add.adicionar_assunto(cursor, valores[0], valores[1])
    c = modulo_add.adicionar_topico(cursor, valores[0], valores[1], valores[2])
    d = modulo_add.adicionar_subtopico(cursor, valores[0], valores[1], valores[2], valores[3])

    print(a, b, c, d)

    if a == True and b == True and c == True and d == True:
        sucesso = tk.Label(root, text="Adicionado com sucesso!", fg='green', font=("Arial", 14))
        if root.grid_slaves(row=13, column=0):
            root.grid_slaves(row=13, column=0)[0].destroy()
        sucesso.grid(column=0, row=13)
        bancoDados.commit()

        from interface.modulo_interface_telaPrincipal import limpar_tela, desenhar_tela
        limpar_tela(destruir)
        desenhar_tela(root_principal, cursor, bancoDados)
    else:
        falha = tk.Label(root, text="Erro ao adicionar item!", fg="red", font=("Arial", 14))
        if root.grid_slaves(row=13, column=0):
            root.grid_slaves(row=13, column=0)[0].destroy()
        falha.grid(column=0, row=13)

def desenhar_tela_adicionar(root):
    materia = tk.Label(root, text="Digite o nome da máteria:", font=("Arial", 14))
    materia.grid(column = 0, row= 0, sticky="w")

    digitar_materia = tk.Entry(root)
    digitar_materia.grid(column=0, row=1, padx=(4, 0), sticky="nsew")

    tk.Label(root).grid(column=0, row=2)

    assunto = tk.Label(root, text="Digite o nome do assunto:", font=("Arial", 14))
    assunto.grid(column = 0, row= 3, sticky="w")

    digitar_assunto = tk.Entry(root )
    digitar_assunto.grid(column=0, row=4, padx=(4, 0), sticky="nsew")

    tk.Label(root).grid(column=0, row=5)

    topico = tk.Label(root, text="Digite o nome do tópico:", font=("Arial", 14))
    topico.grid(column = 0, row= 6, sticky="w")

    digitar_topico = tk.Entry(root )
    digitar_topico.grid(column=0, row=7, padx=(4, 0), sticky="nsew")

    tk.Label(root).grid(column=0, row=8)

    subtopico = tk.Label(root, text="Digite o nome do subtópico:", font=("Arial", 14))
    subtopico.grid(column = 0, row= 9, sticky="w")

    digitar_subtopico = tk.Entry(root )
    digitar_subtopico.grid(column=0, row=10, padx=(4, 0), sticky="nsew")

    return [digitar_materia, digitar_assunto, digitar_topico, digitar_subtopico]
