from tkinter import *
from datetime import *
import sqlite3

janela = Tk()

conector = sqlite3.connect("teste.db")

cursor = conector.cursor()


def cadastrar(jogador, hp, mp, classe):
    comando_sql = (
        f"INSERT INTO jogadores VALUES(1, '{jogador}', {hp}, {mp}, '{classe}')")
    cursor.execute(comando_sql)
    conector.commit()
    cursor.close()
    conector.close()


janela.title("Formulário")

textoUm = Label(janela, text="Jogador:")
textoUm.grid(column=1, row=1, padx=5, pady=5)

jogador = Entry(janela, width=100)
jogador.grid(column=1, row=2, padx=10, pady=10)

textoDois = Label(janela, text="HP:")
textoDois.grid(column=1, row=3, padx=5, pady=5)

hp = Entry(janela, width=100)
hp.grid(column=1, row=4, padx=10, pady=10)

textoTres = Label(janela, text="MP:")
textoTres.grid(column=1, row=5, padx=5, pady=5)

mp = Entry(janela, width=100)
mp.grid(column=1, row=6, padx=5, pady=5)

textoQuatro = Label(janela, text="Classe:")
textoQuatro.grid(column=1, row=7, padx=10, pady=10)

classe = Entry(janela, width=100)
classe.grid(column=1, row=8, padx=5, pady=5)

botao = Button(janela, text="Cadastrar",
               command=lambda: cadastrar(jogador.get(), hp.get(), mp.get(), classe.get()))
botao.grid(column=2, row=2, padx=10, pady=10)

janela.mainloop()
