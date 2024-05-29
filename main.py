from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

# Cores
cor0 = "#2e2d2b"  # preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra
cor5 = "#e06636"  # profit
cor6 = "#038cfc"  # azul
cor7 = "#3fbfb9"  # verde
cor8 = "#263238"  # verde
cor9 = "#e9edf5"  # verde

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('986x600')
janela.configure(background=cor9)
janela.resizable(True, True)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames
frameCima = Frame(janela, bg=cor1, relief=FLAT)
frameCima.grid(row=0, column=0, sticky="nsew")

frameMeio = Frame(janela, bg=cor1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky="nsew")

frameBaixo = Frame(janela, bg=cor1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky="nsew")

# Configurar layout responsivo para a janela principal
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Criando funções
global tree, imagem, imagem_string, l_imagem
imagem_string = ''

def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    mostrar()

def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.set_date(treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0, 'end')

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameMeio, command=update, width=13, text='Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor2, fg=cor1)
        b_confirmar.grid(row=6, column=2, padx=5, pady=5, sticky=W)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def deletar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=cor1, fg=cor4)
    l_imagem.grid(row=0, column=4, rowspan=5, padx=10, pady=10, sticky=E)

def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item(valor)
    imagem = item[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=cor1, fg=cor4)
    l_imagem.grid(row=0, column=4, rowspan=5, padx=10, pady=10, sticky=E)

# Frame de cima
app_img = Image.open('curso.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Análise e Desenvolvimento de Sistemas', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg=cor4)
app_logo.grid(row=0, column=0, sticky=W)

# Frame meio
# Criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.grid(row=0, column=0, padx=10, pady=5, sticky=W)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.grid(row=0, column=1, padx=10, pady=5, sticky=W)

l_local = Label(frameMeio, text='Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_local.grid(row=1, column=0, padx=10, pady=5, sticky=W)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.grid(row=1, column=1, padx=10, pady=5, sticky=W)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_descricao.grid(row=2, column=0, padx=10, pady=5, sticky=W)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.grid(row=2, column=1, padx=10, pady=5, sticky=W)

l_model = Label(frameMeio, text='Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_model.grid(row=3, column=0, padx=10, pady=5, sticky=W)
e_model = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.grid(row=3, column=1, padx=10, pady=5, sticky=W)

l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_cal.grid(row=4, column=0, padx=10, pady=5, sticky=W)
e_cal = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
e_cal.grid(row=4, column=1, padx=10, pady=5, sticky=W)

l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_valor.grid(row=5, column=0, padx=10, pady=5, sticky=W)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.grid(row=5, column=1, padx=10, pady=5, sticky=W)

l_serial = Label(frameMeio, text='Número de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_serial.grid(row=6, column=0, padx=10, pady=5, sticky=W)
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.grid(row=6, column=1, padx=10, pady=5, sticky=W)

l_imagem_texto = Label(frameMeio, text='Adicionar imagem', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_imagem_texto.grid(row=7, column=0, padx=10, pady=5, sticky=W)
b_carregar = Button(frameMeio, command=escolher_imagem, text='Carregar Imagem'.upper(), width=20, overrelief=RIDGE, font=('ivy 8 bold'), bg=cor7, fg=cor1)
b_carregar.grid(row=7, column=1, padx=10, pady=5, sticky=W)

# Botões
b_inserir = Button(frameMeio, command=inserir, text='Inserir'.upper(), width=20, overrelief=RIDGE, font=('ivy 8 bold'), bg=cor2, fg=cor1)
b_inserir.grid(row=0, column=2, padx=10, pady=5, sticky=W)

b_atualizar = Button(frameMeio, command=atualizar, text='Atualizar'.upper(), width=20, overrelief=RIDGE, font=('ivy 8 bold'), bg=cor6, fg=cor1)
b_atualizar.grid(row=1, column=2, padx=10, pady=5, sticky=W)

b_deletar = Button(frameMeio, command=deletar, text='Deletar'.upper(), width=20, overrelief=RIDGE, font=('ivy 8 bold'), bg=cor5, fg=cor1)
b_deletar.grid(row=2, column=2, padx=10, pady=5, sticky=W)

b_ver_imagem = Button(frameMeio, command=ver_imagem, text='Ver Imagem'.upper(), width=20, overrelief=RIDGE, font=('ivy 8 bold'), bg=cor3, fg=cor1)
b_ver_imagem.grid(row=7, column=2, padx=10, pady=5, sticky=W)

# Tabela
def mostrar():
    global tree
    tabela_head = ['ID', 'Nome', 'Local', 'Descricao', 'Modelo', 'Data', 'Valor', 'Serial', 'Imagem']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended", columns=tabela_head, show="headings")

    # Vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center","center","center"]
    h=[30,170,140,100,120,100,100,100,120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar()

janela.mainloop()
