from cProfile import label
from lzma import FILTER_LZMA1
from tkinter import *

#back-end
def calcular():
    if in1_fr1.get().replace('.','',1) and in2_fr1.get().replace('.','',1):
        x=round(float(in1_fr1.get())/(float(in2_fr1.get())**2),2)
        lb3_fr2['text'] = x
        if x < 18.5:
            lb4_fr2['text'] = 'Abaixo do Peso'            
        elif x >= 18.5 and x <= 24.9:
            lb4_fr2['text'] = 'Normal'  
        elif x >= 25.0 and x <= 29.9:
            lb4_fr2['text'] = 'Sobrepeso'  
        elif x >= 30.0 and x <= 39.9:
            lb4_fr2['text'] = 'Obesidade'  
        elif x > 40:
            lb4_fr2['text'] = 'Obesidade Grave' 

    else:
        lb3_fr2['text'] = 'Erro!!!'
 


#front-end
root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.bind('q', lambda event: quit())

#criar os widgets
lb1_fr1 = Label (fr1, text='Peso', font= 'Arial 25')
lb2_fr1 = Label (fr1, text='Altura', font= 'Arial 25')
in1_fr1 = Entry (fr1, font= 'Arial 25')
in2_fr1 = Entry (fr1, font= 'Arial 25')
bt1_fr1 = Button (fr1, text='Calcular', font= 'Arial 25', command=calcular)
lb3_fr2 = Label (fr2, text=0.0, font= 'Arial 25')
lb4_fr2 = Label (fr2, text='Interpretação do IMC', font= 'Arial 25')
lb5_fr1 = Label (fr1, text = 'teste', font = 'Arial 25')

fr1.pack()
fr2.pack()

#organizar os widgets
lb1_fr1.grid(row=0, column=0, sticky=NSEW)
lb2_fr1.grid(row=1, column=0, sticky=NSEW)
lb5_fr1.grid(row=3, column=0,sticky=NSEW)
in1_fr1.grid(row=0, column=1, sticky=NSEW)
in2_fr1.grid(row=1, column=1, sticky=NSEW)
bt1_fr1.grid(row=2, column=0, columnspan=3, sticky=NSEW)
lb3_fr2.grid(row=0, column=0, columnspan=3, sticky=NSEW)
lb4_fr2.grid(row=1, column=0, columnspan=3, sticky=NSEW)
#run #Função expecífica para manter a janela aparecendo.
root.mainloop()

