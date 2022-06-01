from tkinter import *

#back-end
def imprimir():
    lb0['text'] = 'Burro pa caraio'
    print(in1.get())
    print(in2.get())
    print(in3.get())

#front
#window
janela = Tk()

#geometry
janela.geometry('400x300+500+500')
janela.minsize(width=900, height=500)

#widgets
lb0 = Label(janela, text='Insira seus Dados', font='Arial 25')
lb1 = Label(janela, text='Nome', font='Arial 15')
in1 = Entry(janela, font='Arial 15')
lb2 = Label(janela, text='CPF', font='Arial 15')
in2 = Entry(janela, font='Arial 15')
lb3 = Label(janela, text='Número do Cartão', font='Arial 15')
in3 = Entry(janela, font='Arial 15')
bt1 = Button(janela, text='Enviar', font='Arial 15', command=imprimir)
bt2 = Button(janela, text='Sair', font='Arial 15', command=quit)

#layout
lb0.pack()
lb1.pack()
in1.pack()
lb2.pack()
in2.pack()
lb3.pack()
in3.pack()
bt1.pack()
bt2.pack()

#run
janela.mainloop()