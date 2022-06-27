from cProfile import label
from cgitb import text
import tkinter
from tkinter import *
from tkinter import ttk

#cores
co0 = "#FFFFFF"
co1 = "#333333"
co2 = "#fcc058"
co3 = "#38576b"
co4 = "#3297a8"
co5 = "#fff873"
co6 = "#fvv058"
co7 = "#e85151"
co8 = "#34eb3d"
fundo = "#3b3b3b"

#Configurando a janela

janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

#Dividindo a tela.

frame_cima = Frame (janela, width =260, height= 100, bg=co1, relief='raised')
frame_cima.grid (row = 0, column = 0, sticky = NW)
frame_baixo = Frame (janela, width =260, height= 300, bg=co0, relief='flat')
frame_baixo.grid (row = 1, column = 0, sticky = NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#Configurando o frame cima

#Painel Jogador
app_1 = Label(frame_cima, text="Voce", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place (x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place (x=0, y=0)
app_1_pontos = Label (frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place (x=50, y=20)

#Separador dos pontos
app_ = Label (frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place (x=120, y=20)

#Painel PC
app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place (x=190, y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place (x=200, y=70 )
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)
















janela.mainloop()