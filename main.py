from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date


#cores
cor0 = "#2e2d2b" #preta
cor1 = "#feffff" #branca
cor2 = "#4fa882" #verde
cor3 = "#38576b" #valor
cor4 = "#403d3d" #letra
cor5 = "#e06636" #profit
cor6 = "#038cfc" #azul
cor7 = "#3fbfb9" #verde
cor8 = "#263238" #verde
cor9 = "#e9edf5" #verde

#criando janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frames
frameCima = Frame(janela, width=1043, height=50, bg=cor1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=cor1, pady=20,  relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=cor1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#frame cima

#Abrindo imagem
app_img = Image.open('curso.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Análise e Desenvolvimento de Sistemas', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg=cor4)

app_logo.place(x=0, y=0)


#frame meio

#criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=10)
e_nome= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text='Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_local.place(x=10, y=40)
e_local= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_descricao.place(x=10, y=70)
e_descricao= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_model = Label(frameMeio, text='Marca/Model', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_model.place(x=10, y=100)
e_model= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=101)

l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_cal.place(x=10, y=130)
e_cal= DateEntry(frameMeio, width=12, Background='darkblue', bordwidth=2, year=2024, date_pattern='dd/MM/yyyy')
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_valor.place(x=10, y=160)
e_valor= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text='Número de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_serial.place(x=10, y=190)
e_serial= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)


# criando botoões------------------------------------------------------------------------------------

#botão carregar
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, width=29, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_carregar.place(x=130, y=221)

#botão inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, image=img_add, width=95, text='Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_inserir.place(x=330, y=10)

#botão Atualizar
img_update= Image.open('update.png')
img_update= img_update.resize((20,20))
img_update= ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, image=img_update, width=95, text='Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_update.place(x=330, y=50)

#botão deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, image=img_delete, width=95, text='Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_delete.place(x=330, y=90)

#botão ver imagem
img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, image=img_item, width=95, text='Ver item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_item.place(x=330, y=221)

# Labels Quantidade total e Valores
l_total = Label(frameMeio, width=14, height=2,anchor=CENTER, font=('Ivy 17 bold'), bg=cor7, fg=cor1, relief=FLAT)
l_total.place(x=450, y=17)

l_valor_total = Label(frameMeio, text='  Valor Total de todos os itens  ' ,anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor1)
l_valor_total.place(x=450, y=12)


l_qtd = Label(frameMeio, width=10, height=2,anchor=CENTER, font=('Ivy 25 bold'), bg=cor7, fg=cor1, relief=FLAT)
l_qtd.place(x=450, y=90)

l_qtd_itens = Label(frameMeio, text='Quantidade total de itens' ,anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor1)
l_qtd_itens.place(x=460, y=92)


#tabela




#creating a treeaview with dual scrollbars
tabela_head = ['#item', 'Nome', 'Área', 'Descrição', 'Marca', 'Data da Compra', 'Valor da compra', 'Número de série']

lista_itens =[]

global tree

tree = ttk.Treeview(frameBaixo, selectmode="extended", columns=tabela_head, show="headings")

#vertical scrollbar
vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
#horizontal scrollbar
hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)


tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew') #essa linha está retirando o tírulo do centro
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameBaixo.grid_rowconfigure(0, weight=12)

hd=["center", "center", "center", "center", "center", "center", "center", "center"]
h =[40, 150, 100, 160, 130, 100,100, 100]
n=0

for col in tabela_head:
  tree.heading(col, text=col.title(), anchor=CENTER)
  tree.column(col, width=h[n], anchor=hd[n])
  n+=1

for item in lista_itens:
  tree.insert('', 'end', values=item)

quantidade =[888,88]
for iten in lista_itens:
   quantidade.append([iten[6]])

Total_valor =sum(quantidade)
Total_itens = len(quantidade)

l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
l_qtd['text'] = Total_itens





janela.mainloop()
