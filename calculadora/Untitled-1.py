from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN

#add ação
def entrada(valor):
   lb1['text'] += valor

def resultado():
   x=eval (lb1['text'])
   lb1['text']=x


def limpar():
   lb1 ['text'] = ''


#criando janela 
root = Tk()

#front end
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.geometry('320x500')
   
#criando widgets nuerais
lb1 = Label (root, text='', font= 'Arial 25')
bt1= Button (root, text = '1', font='Arial 20', command=lambda: entrada ('1')) 
bt2= Button (root, text= '2', font = 'Arial 20',command=lambda: entrada ('2'))
bt3= Button (root, text='3', font= 'Arial 20', command=lambda: entrada ('3'))
bt4 = Button (root, text='4', font= 'Arial 25', command=lambda: entrada('4'))
bt5 = Button (root, text='5', font= 'Arial 25', command=lambda: entrada('5'))
bt6 = Button (root, text='6', font= 'Arial 25', command=lambda: entrada('6'))
bt7 = Button (root, text='7', font= 'Arial 25', command=lambda: entrada('7'))
bt8 = Button (root, text='8', font= 'Arial 25', command=lambda: entrada('8'))
bt9 = Button (root, text='9', font= 'Arial 25', command=lambda: entrada('9'))

#criando widgets de sinais
bt10 = Button (root, text='.', font= 'Arial 25', command=lambda: entrada('.'))
bt11 = Button (root, text='=', font= 'Arial 25', command=lambda: resultado())
bt12 = Button (root, text='+', font= 'Arial 25', command=lambda: entrada('+aa '))
bt13 = Button (root, text='-', font= 'Arial 25', command=lambda: entrada('-'))
bt14 = Button (root, text='x', font= 'Arial 25', command=lambda: entrada('*'))
bt15 = Button (root, text='/', font= 'Arial 25', command=lambda: entrada('/'))
bt16 = Button (root, text='√', font= 'Arial 25', command=lambda: entrada('√'))
bt17 = Button (root, text='x²', font= 'Arial 25', command=lambda: entrada('x²'))
bt18 = Button (root, text='%', font= 'Arial 25', command=lambda: entrada('%'))
bt19 = Button (root, text='⌫', font= 'Arial 25', command=lambda: limpar())
bt20 = Button (root, text='C', font= 'Arial 25', command=lambda: limpar())

#Chamando teclas
lb1.grid (row=0, column=0, columnspan=4,sticky=NSEW)
bt1.grid(row=6, column=0, sticky=NSEW)
bt2.grid(row=6, column=1, sticky=NSEW)
bt3.grid(row=6, column=2, sticky=NSEW)
bt4.grid(row=5, column=0, sticky=NSEW)
bt5.grid(row=5, column=1, sticky=NSEW)
bt6.grid(row=5, column=2, sticky=NSEW)
bt7.grid(row=4, column=0, sticky=NSEW)
bt8.grid(row=4, column=1, sticky=NSEW)
bt9.grid(row=4, column=2, sticky=NSEW)

#Chamando sinais
bt10.grid(row=7, column=2, sticky=NSEW)
bt11.grid(row=7, column=3, sticky=NSEW)
bt12.grid(row=6, column=3, sticky=NSEW)
bt13.grid(row=5, column=3, sticky=NSEW)
bt14.grid(row=4, column=3, sticky=NSEW)
bt15.grid(row=3, column=3, sticky=NSEW)
bt16.grid(row=3, column=2, sticky=NSEW)
bt17.grid(row=3, column=1, sticky=NSEW)
bt18.grid(row=3, column=0, sticky=NSEW)
bt19.grid(row=2, column=2, columnspan=2, sticky=NSEW)
bt20.grid(row=2, column=0, columnspan=2, sticky=NSEW)

#interação teclado numeros
root.bind('0', lambda event: entrada('0'))
root.bind('1', lambda event: entrada('1'))
root.bind('2', lambda event: entrada('2'))
root.bind('3', lambda event: entrada('3'))
root.bind('4', lambda event: entrada('4'))
root.bind('5', lambda event: entrada('5'))
root.bind('6', lambda event: entrada('6'))
root.bind('7', lambda event: entrada('7'))
root.bind('8', lambda event: entrada('8'))
root.bind('9', lambda event: entrada('9'))

#interação teclado sinais
root.bind('.', lambda event: entrada('.'))
root.bind('=', lambda event: resultado())
root.bind('+', lambda event: entrada('+'))
root.bind('-', lambda event: entrada('-'))
root.bind('*', lambda event: entrada('*'))
root.bind('/', lambda event: entrada('/'))
#root.bind('16', lambda event: entrada())
root.bind('^^', lambda event: entrada('**'))
root.bind('%', lambda event: entrada('/100'))
#root.bind('', lambda event: limpar())
root.bind('c', lambda event: limpar())



 

root.mainloop() 
