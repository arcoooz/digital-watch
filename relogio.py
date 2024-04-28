from tkinter import *
import tkinter
from datetime import datetime

#color

color1 = '#fff'     #white
color2 = '#000000'  #black
color3 = '#0000ff'  #blue
color4 = '#ffc0cb'  #pink
color5 = '#7300df'  #purple
color6 = '#535353'  #gray

fundo = color6
cor = color1

janela = Tk()
janela.title()
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=color6)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day 
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%Y')

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + ' '+ str(dia) + '/' + str(mes) + '/' + str(ano))

l1 = Label(janela, text='', font=('Arial 80'), bg=color6, fg=color4)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text='', font=('Arial 20'), bg=color6, fg=color4)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()

