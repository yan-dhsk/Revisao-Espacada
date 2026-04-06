import tkinter as tk
import sqlite3
from datetime import date

bancoDados = sqlite3.connect("Revisões.db")
cursor = bancoDados.cursor()

largura = 800
altura = 600

root = tk.Tk()
root.title("Revisões espaçadas")
root.geometry(f"{largura}x{altura}")

inicio = tk.Label(root, text="Bem-Vindo", font=("Arial", 28))
inicio.pack()

hoje = tk.Label(root, text="Revisar hoje:", font=("Arial", 14))
hoje.place(x= (largura*0.025), y=(altura*0.125))

cursor.execute("SELECT * FROM subtopico WHERE data_revisar = (?)", (date.today(), ))
revisoes_hoje = cursor.fetchone()

espaço = 30
indice = 0

if revisoes_hoje:
    revisao = tk.Label(root, text=revisoes_hoje[indice], font=("Arial", 10))
    revisao.place(x= (largura*0.025), y=((altura+espaço)*0.125))

if revisoes_hoje != None and indice < len(revisoes_hoje):
    espaço += 10
    indice += 1

root.mainloop()


