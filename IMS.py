from tkinter import *

#back-end
def calcular():
    if in1.get().replace('.','',1) and in2.get().replace('.','',1):
        x=round(float(in1.get())/(float(in2.get())**2),2)
        lb3['text'] = x
        if x < 18.5:
            lb4['text'] = 'Abaixo do Peso'            
        elif x >= 18.5 and x <= 24.9:
            lb4['text'] = 'Normal'  
        elif x >= 25.0 and x <= 29.9:
            lb4['text'] = 'Sobrepeso'  
        elif x >= 30.0 and x <= 39.9:
            lb4['text'] = 'Obesidade'  
        elif x > 40:
            lb4['text'] = 'Obesidade Grave' 

    else:
        lb3['text'] = 'Erro!!!'



#front-end
root = Tk()
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
lb1 = Label (root, text='Peso', font= 'Arial 25')
lb2 = Label (root, text='Altura', font= 'Arial 25')
in1 = Entry (root, font= 'Arial 25')
in2 = Entry (root, font= 'Arial 25')
bt1 = Button (root, text='Calcular', font= 'Arial 25', command=calcular)
lb3 = Label (root, text=0.0, font= 'Arial 25')
lb4 = Label (root, text='Interpretação do IMC', font= 'Arial 25')

#organizar os widgets
lb1.grid(row=0, column=0, sticky=NSEW)
lb2.grid(row=1, column=0, sticky=NSEW)
in1.grid(row=0, column=1, sticky=NSEW)
in2.grid(row=1, column=1, sticky=NSEW)
bt1.grid(row=2, column=0, columnspan=3, sticky=NSEW)
lb3.grid(row=3, column=0, columnspan=3, sticky=NSEW)
lb4.grid(row=4, column=0, columnspan=3, sticky=NSEW)

#run #Função expecífica para manter a janela aparecendo.
root.mainloop()
