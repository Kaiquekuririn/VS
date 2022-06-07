from logging import root
from msilib.schema import Font
from tkinter import *
from tkinter.tix import COLUMN
from tokenize import cookie_re
from turtle import color, title

root = Tk()
root.title = ('Cadastro')
fr1 = Frame (root)
fr2 = Frame (root)
fr3 = Frame (root)

#label 1 frame
lb0_fr1 = Label(fr1, text = '  Dados Pessoais', font= 'Arial 25')
lb1_fr1 = Label(fr1, text = ' Nome:', font= 'Arial 25')
lb2_fr1 = Label(fr1, text = ' Data Nasc:', font= 'Arial 25')
lb3_fr1 = Label(fr1, text = ' CPF:', font= 'Arial 25')
lb4_fr1 = Label(fr1, text = ' Telefone:', font= 'Arial 25')
#Entry do 1 frame
in1_fr1 = Entry(fr1, font= 'Arial 25')
in2_fr1 = Entry(fr1, font= 'Arial 25')
in3_fr1 = Entry(fr1, font= 'Arial 25')
in4_fr1 = Entry(fr1, font= 'Arial 25')
#Posição dps Label:
lb0_fr1.grid (row=0, column=0,sticky=NSEW)
lb1_fr1.grid (row=1, column=0,sticky=W)
lb2_fr1.grid (row=2, column=0,sticky=W)
lb3_fr1.grid (row=3, column=0,sticky=W)
lb4_fr1.grid (row=4, column=0,sticky=W)
#Posição Entry:
in1_fr1.grid(row=1,column=1,sticky=NSEW)
in2_fr1.grid(row=2,column=1,sticky=NSEW)
in3_fr1.grid(row=3,column=1,sticky=NSEW)
in4_fr1.grid(row=4,column=1,sticky=NSEW)
#Label do 2 frame
lb0_fr2 = Label(fr2, text = '  Endereço:', font= 'Arial 25')
lb1_fr2 = Label(fr2, text = '  Rua:', font= 'Arial 25')
lb2_fr2 = Label(fr2, text = '  Bairro', font= 'Arial 25')
lb3_fr2 = Label(fr2, text = '  Cidade:', font= 'Arial 25')
lb4_fr2 = Label(fr2, text = '  N°:', font= 'Arial 25')
lb5_fr2 = Label(fr2, text=  '  UF:', font='Arial 25')
#Entry 2 frame
in1_fr2 = Entry(fr2, font= 'Arial 25')
in2_fr2 = Entry(fr2, font= 'Arial 25')
in3_fr2 = Entry(fr2, font= 'Arial 25')
in4_fr2 = Entry(fr2, font= 'Arial 25')
in5_fr2 = Entry(fr2, font= 'Arial 25')
#Posição dos label frame 2 
lb0_fr2.grid (row=0,  column=0,sticky=W)
lb1_fr2.grid (row=1, column=0,sticky=W)
lb2_fr2.grid (row=2, column=0,sticky=W)
lb3_fr2.grid (row=2, column=2,sticky=W)
lb4_fr2.grid (row=1, column=4,sticky=W)
lb5_fr2.grid (row=2, column=4,sticky=W)
#Posição dos entry frame 2
in1_fr2.grid(row=1,column=1,sticky=NSEW)
in2_fr2.grid(row=2,column=1,sticky=NSEW)
in3_fr2.grid(row=2,column=3,sticky=NSEW)
in4_fr2.grid(row=1,column=5,sticky=NSEW)
in5_fr2.grid(row=2,column=5, sticky=NSEW)
#Criando os button 3° frame
bt0_fr3 = Button(fr3, text = 'Gravar Dados', font='Arial 25')
bt1_fr3 = Button(fr3, text= 'Listar Dados', font= 'Arial 25')
#Posição dos button 3° frame:
bt0_fr3.grid( row=0, column=0, sticky= W)
bt1_fr3.grid( row=0, column=1, sticky= W)
#pack
fr1.grid(sticky=W)
fr2.grid(sticky=W)
fr3.grid(sticky=W)
#loop
root.mainloop()






