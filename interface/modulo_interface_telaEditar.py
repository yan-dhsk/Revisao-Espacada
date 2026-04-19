import tkinter as tk
from lógica import modulo_update

largura = 500
altura = 480

destruir = []

def tela_editar(cursor, bancoDados, destruir2, root_principal):
    global destruir
    destruir.clear()
    root = tk.Toplevel()
    root.title("Editar")
    root.geometry(f'{largura}x{altura}')
    root.resizable(False, False)

    desenhar_tela_principal(root, 0, cursor, bancoDados, destruir2, root_principal)


def desenhar_tela_principal(root, situacao, cursor, bancoDados, destruir2, root_principal):
    global destruir

    frame = tk.Frame(root)
    destruir.append(frame)
    frame.pack()

    if situacao == 1:
        sucesso = tk.Label(frame, text="Editado com sucesso", font=("Arial", 20), fg="green")
        destruir.append(sucesso)
        sucesso.pack()

    pergunta = tk.Label(frame, text="O que você quer editar?", font=("Arial", 20))
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

    for x in range(len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
    frame2 = tk.Frame(canvas)
    frame2.grid_columnconfigure(0, weight=1)

    window_id = canvas.create_window((0, 0), window=frame2, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    frame2.bind('<Configure>', on_frame_configure)

    def on_canvas_configure(event):
        canvas.itemconfig(window_id, width=event.width)
    canvas.bind('<Configure>', on_canvas_configure)

    destruir.append(canvas)
    destruir.append(scrollbar)

    scrollbar.pack(side='right', fill='y')
    canvas.pack(side='left', fill='both', expand=True)

    for x in range(len(todas_revisoes)):
        revisao = tk.Button(
            frame2,
            text=todas_revisoes[x][0],
            command=lambda id=todas_revisoes[x][1]: desenhar_editar(
                root, escolha, id, cursor, bancoDados, destruir2, root_principal
            )
        )
        revisao.grid(column=0, row=x)


def desenhar_editar(root, escolha, id, cursor, bancoDados, destruir2, root_principal):
    global destruir

    if escolha == 4:
        for x in range(len(destruir)):
            destruir[x].destroy()
        destruir.clear()

        frameOpcao = tk.Frame(root)
        destruir.append(frameOpcao)
        frameOpcao.pack()

        pergunta = tk.Label(frameOpcao, text="O que deseja alterar?", font=("Arial", 16))
        pergunta.pack(pady=(0, 20))
        destruir.append(pergunta)

        botaoNome = tk.Button(frameOpcao, text="Nome", font=("Arial", 14), bg="blue", fg="white", width=10, height=2, command=lambda: desenhar_campo_nome(root, id, cursor, bancoDados, destruir2, root_principal))
        botaoNome.pack(pady=(5, 0))
        destruir.append(botaoNome)

        botaoData = tk.Button(frameOpcao, text="Data", font=("Arial", 14), bg="blue", fg="white", width=10, height=2, command=lambda: desenhar_campo_data(root, id, cursor, bancoDados, destruir2, root_principal))
        botaoData.pack(pady=(10, 0))
        destruir.append(botaoData)
        return

    for x in range(len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    frame3 = tk.Frame(root)
    destruir.append(frame3)
    frame3.pack()

    novoNomeLabel = tk.Label(frame3, text="Digite o novo nome:", font=("Arial", 16))
    novoNomeLabel.pack()
    destruir.append(novoNomeLabel)

    digitarNovoNome = tk.Entry(frame3)
    digitarNovoNome.pack(padx=4)
    destruir.append(digitarNovoNome)

    confirmar = tk.Button(frame3, text="Confirmar", bg="blue", fg="white", width=10, height=2, command=lambda: chamada_editar(root, escolha, id, digitarNovoNome.get(), cursor, bancoDados, destruir2, root_principal))
    confirmar.pack(pady=(10, 0))
    destruir.append(confirmar)


def desenhar_campo_nome(root, id, cursor, bancoDados, destruir2, root_principal):
    global destruir

    for x in range(len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    frameNome = tk.Frame(root)
    destruir.append(frameNome)
    frameNome.pack()

    labelNome = tk.Label(frameNome, text="Digite o novo nome:", font=("Arial", 16))
    labelNome.pack()
    destruir.append(labelNome)

    entryNome = tk.Entry(frameNome)
    entryNome.pack(padx=4)
    destruir.append(entryNome)

    confirmar = tk.Button(frameNome, text="Confirmar", bg="blue", fg="white", width=10, height=2, command=lambda: chamada_editar(root, 4, id, entryNome.get(), cursor, bancoDados, destruir2, root_principal))
    confirmar.pack(pady=(10, 0))
    destruir.append(confirmar)


def desenhar_campo_data(root, id, cursor, bancoDados, destruir2, root_principal):
    global destruir

    for x in range(len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    frameData = tk.Frame(root)
    destruir.append(frameData)
    frameData.pack()

    labelData = tk.Label(frameData, text="Digite a nova data (AAAA-MM-DD):", font=("Arial", 16))
    labelData.pack()
    destruir.append(labelData)

    entryData = tk.Entry(frameData)
    entryData.pack(padx=4)
    destruir.append(entryData)

    confirmar = tk.Button(frameData, text="Confirmar", bg="blue", fg="white", width=10, height=2, command=lambda: chamada_editar(root, 5, id, entryData.get(), cursor, bancoDados, destruir2, root_principal))
    confirmar.pack(pady=(10, 0))
    destruir.append(confirmar)


def chamada_editar(root, escolha, id, novoValor, cursor, bancoDados, destruir2, root_principal):
    from interface.modulo_interface_telaPrincipal import limpar_tela, desenhar_tela

    if escolha == 1:
        resultado = modulo_update.alterar_nome_materia(cursor, id, novoValor)
    elif escolha == 2:
        resultado = modulo_update.alterar_nome_assunto(cursor, id, novoValor)
    elif escolha == 3:
        resultado = modulo_update.alterar_nome_topico(cursor, id, novoValor)
    elif escolha == 4:
        resultado = modulo_update.alterar_nome_subtopico(cursor, id, novoValor)
    elif escolha == 5:
        resultado = modulo_update.alterar_data_revisar_subtopico(cursor, id, novoValor)
    else:
        resultado = False

    if resultado == False:
        for x in range(len(destruir)):
            destruir[x].destroy()
        destruir.clear()

        frameErro = tk.Frame(root)
        destruir.append(frameErro)
        frameErro.pack()

        erro = tk.Label(frameErro, text="Erro ao editar item!", font=("Arial", 16), fg="red")
        erro.pack()
        destruir.append(erro)
        return

    bancoDados.commit()

    for x in range(len(destruir)):
        destruir[x].destroy()
    destruir.clear()

    limpar_tela(destruir2)
    desenhar_tela(root_principal, cursor, bancoDados)

    desenhar_tela_principal(root, 1, cursor, bancoDados, destruir2, root_principal)
