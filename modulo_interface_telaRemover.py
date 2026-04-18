import tkinter as tk
import sqlite3
from datetime import date
import modulo_delete

largura = 500
altura = 480

destruir = []

def tela_deletar(cursor, bancoDados, destruir2, root_principal):
    root = tk.Toplevel()
    root.title("Deletar")
    root.geometry(f'{largura}x{altura}')
    root.resizable(False, False)

    desenhar_tela_principal(root, 0, cursor, bancoDados, destruir2, root_principal)


def desenhar_tela_principal(root, situacao, cursor, bancoDados, destruir2, root_principal):
    global destruir

    frame = tk.Frame(root)
    destruir.append(frame)
    frame.pack()

    if situacao == 1:
        sucesso = tk.Label(frame, text="Deletado com sucesso", font=("Arial", 20), fg="green")
        destruir.append(sucesso)
        sucesso.pack()

    pergunta = tk.Label(frame, text="O que você quer apagar?", font=("Arial", 20))
    pergunta.pack()
    destruir.append(pergunta)

    materia = tk.Button(frame, text="Matéria", font=("Arial", 18), bg="blue", fg="white", width=10, height=2, command=lambda x=1: desenhar_lista(root, x, cursor, bancoDados, destruir2, root_principal))
    materia.pack(pady=(10, 0))
    destruir.append(materia)

    assunto = tk.Button(frame, text="Assunto", font=("Arial", 18), bg="blue", fg="white", width=10, height=2, command=lambda x=2: desenhar_lista(root, x, cursor, bancoDados, destruir2, root_principal))
    assunto.pack(pady=(10, 0))
    destruir.append(assunto)

    tópico = tk.Button(frame, text="Tópico", font=("Arial", 18), bg="blue", fg="white", width=10, height=2, command=lambda x=3: desenhar_lista(root, x, cursor, bancoDados, destruir2, root_principal))
    tópico.pack(pady=(10, 0))
    destruir.append(tópico)

    subtópico = tk.Button(frame, text="Subtópico", font=("Arial", 18), bg="blue", fg="white", width=10, height=2, command=lambda x=4: desenhar_lista(root, x, cursor, bancoDados, destruir2, root_principal))
    subtópico.pack(pady=(10, 0))
    destruir.append(subtópico)

def desenhar_lista(root, escolha, cursor, bancoDados, destruir2, root_principal):
    global destruir

    if escolha == 1:
        cursor.execute("SELECT m_nome, m_id FROM materias")
    elif escolha == 2:
        cursor.execute("SELECT a_nome, a_id FROM assuntos")
    elif escolha == 3:
        cursor.execute("SELECT t_nome, t_id FROM topicos")
    else:
        cursor.execute("SELECT s_nome, s_id FROM subtopico")

    todas_revisoes = cursor.fetchall()

    for x in range (len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    frame2 = tk.Frame(root)
    destruir.append(frame2)
    frame2.pack()

    for x in range (len(todas_revisoes)):
        revisao = tk.Button(frame2, text=todas_revisoes[x][0], command=lambda : chamada_deletar(root, escolha, todas_revisoes[x][1], cursor, bancoDados, destruir2, root_principal))
        revisao.grid(column=0, row=x)

def chamada_deletar(root, escolha, id, cursor, bancoDados, destruir2, root_principal):
    from modulo_interface_telaPrincipal import limpar_tela, desenhar_tela
    
    if escolha == 1:
        modulo_delete.deletar_materia(cursor, id)
    elif escolha == 2:
        modulo_delete.deletar_assunto(cursor, id)
    elif escolha ==3:
        modulo_delete.deletar_topico(cursor, id)
    else:
        modulo_delete.deletar_subtopico(cursor, id)

    bancoDados.commit()
    for x in range (len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    limpar_tela(destruir2)
    desenhar_tela(root_principal, cursor, bancoDados)

    desenhar_tela_principal(root, 1, cursor, bancoDados, destruir2, root_principal)
