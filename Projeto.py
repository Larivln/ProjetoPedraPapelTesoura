import tkinter as tk
from random import choice
import time

opcoes = ['pedra', 'papel', 'tesoura']

def jogar():
    maquina = choice(opcoes)
    jogada_jogador = jogada.get()
    if maquina == jogada_jogador:
        resultado['text'] = f' TNC EMPATOU!'
    elif jogada_jogador == 'pedra':
        if maquina == 'papel':
            resultado['text'] = f'iih perdeu!! {maquina} embrulhou a merda da  {jogada_jogador}!'
        else:
            resultado['text'] = f'AEE GANHOU DO BOT! a {jogada_jogador} quebra a essa bosta de {maquina}!'
    elif jogada_jogador == 'papel':
        if maquina == 'tesoura':
            resultado['text'] = f'iih perdeu!! burrão não sabia que {maquina}  corta  {jogada_jogador}!'
        else:
            resultado['text'] = f'AEE GANHOU DO BOT! o {jogada_jogador} cobre essa merda de  {maquina}!'
    elif jogada_jogador == 'tesoura':
        if maquina == 'pedra':
            resultado['text'] = f'iih perdeu!! olha a {maquina} destroi a {jogada_jogador} igual a vida faz com voce ♥!'
        else:
            resultado['text'] = f'AEE GANHOU DO BOT! parabens a {jogada_jogador} era da tramontina corto rapido o {maquina}!'
    elif jogada_jogador == 'desiste':
        resultado['text'] = "DESISTIU! VOCÊ FAZ ISSO NA SUA VIDA TAMBÉM? KKKKK"
        app.after(3000, app.destroy)
    else:
        resultado['text'] = 'sabe escrever não ?'
        

app = tk.Tk()
app.title("Jogo de Pedra-Papel-Tesoura")

instrucoes = tk.Label(text="Escolha uma das opções para jogar contra o BOT:\n\n. pedra\n. papel\n. tesoura\n. desiste", font=("Helvetica", 14))
instrucoes.pack()

jogada = tk.StringVar()
entry = tk.Entry(textvariable=jogada, font=("Helvetica", 14))
entry.pack()

botao = tk.Button(text="Jogar", font=("Helvetica", 14), command=jogar)
botao.pack()

resultado = tk.Label(text="", font=("Helvetica",14))
resultado.pack()

app.mainloop()