from imports import*


root = tk.Tk()
root.title("Agenda")
root.geometry("980x900")
root.configure(background=co1)
root.resizable(width=False, height=False)
#root.overrideredirect(1)
largura_root = 980
altura_root = 950
#obter tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

#******************************************************************************************************************************
frame_logo = Frame(root, width=980, height=52, bg=co1)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_botoes = Frame(root, width=980, height=65, bg=co1)
frame_botoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_painel = Frame(root, width=980, height=500, bg=co1)
frame_painel.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

frame_tabela= Frame(root, width=980, height=200, bg=co1)
frame_tabela.grid(row=6, column=0, pady=0, padx=10, sticky=NSEW)

frame_img = Frame(frame_painel, width=120, height=120, bg=co10)
frame_img.place( y=70, x=500)

#********************************************************************************************************************************
# Trabalhando no frame logo
app_lg = Image.open('img/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Agenda", width=1200, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

#***************************************************************************************************************************************
# Função para abrir o calendário e capturar a data
def calendario():
    def pegar_data():
        data_selecionada = cal.selection_get()  # Obtém a data selecionada
        entry_data.delete(0, END)  # Limpa a entrada
        entry_data.insert(0, data_selecionada)  # Insere a data selecionada no campo de texto
        calendario_janela.destroy()  # Fecha o calendário

    # Criar uma nova janela para o calendário
    calendario_janela = Toplevel()
    calendario_janela.title("Selecione a Data")
    calendario_janela.geometry("100x100")
    calendario_janela.resizable(width=False, height=False)
    #root.overrideredirect(1)
    largura_calendario_janela = 100
    altura_calendario_janela = 100
    #obter tamanho da tela
    largura_tela = calendario_janela.winfo_screenwidth()
    altura_tela = calendario_janela.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    calendario_janela.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")
    cal = Calendar(calendario_janela, date_pattern="dd-mm-yyyy")  # Calendário com padrão de data
    cal.pack(pady=20)
    # Botão para confirmar a seleção da data
    btn_selecionar = Button(calendario_janela, text="Selecionar", command=pegar_data)
    btn_selecionar.pack(pady=10)
    
def escolher_imagem():
        global imagem_tk, l_imagem

        # Abrir janela para selecionar imagem
        imagem_path = fd.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
        if not imagem_path:  # Se o usuário cancelar, sair da função
            return

        # Abrir e redimensionar a imagem
        imagem = Image.open(imagem_path)
        imagem = imagem.resize((150, 150))  # Ajuste o tamanho conforme necessário
        imagem_tk = ImageTk.PhotoImage(imagem)

        # Atualizar ou criar o Label com a imagem
        if 'l_imagem' in globals():  
            l_imagem.config(image=imagem_tk)
            l_imagem.image = imagem_tk
        else:
        
            l_imagem = Label(frame_img, image=imagem_tk, bg="white")
            l_imagem.place(x=0, y=0)
            
def cadastrar_categoria():
    
    global root
    
    #Criando a janela
    root1 = Toplevel(root) 
    root1.title("Categoria")
    root1.geometry("200x120")
    root.configure(background=co1)
    root.resizable(width=False, height=False)
    largura_root = 200
    altura_root = 200
    #obter tamanho da tela
    largura_tela = root1.winfo_screenwidth()
    altura_tela = root1.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    root1.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")  
    
    
    l_id = Label(root1, text="Categoria", font=('Ivy 10 bold'), bg=co1, fg=co0)
    l_id.place(x=60, y=10)
    e_id= Entry(root1, width=19, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_id.place(x=35, y=40)     
    
    # Botoes Cabeçalho
    app_img_add = Image.open('img/save.png')
    app_img_add = app_img_add.resize((18,18))
    app_img_add = ImageTk.PhotoImage(app_img_add)
    app_add = Button(root1,command=None, image=app_img_add, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
    app_add.place(x=60 , y=60)
    
    l_id = Label(root1, text="Subcategoria", font=('Ivy 10 bold'), bg=co1, fg=co0)
    l_id.place(x=60, y=110)
    e_id= Entry(root1, width=19, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_id.place(x=35, y=140)     
    
    # Botoes Cabeçalho
    app_img_subc = Image.open('img/save.png')
    app_img_subc = app_img_subc.resize((18,18))
    app_img_subc = ImageTk.PhotoImage(app_img_subc)
    app_subc = Button(root1,command=None, image=app_img_subc, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
    app_subc.place(x=60 , y=160)
    
    
         
            
            
#********************************************************************************************************************************    
# Botoes Cabeçalho
app_img_add = Image.open('img/save.png')
app_img_add = app_img_add.resize((18,18))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(frame_botoes,command=None, image=app_img_add, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_add.grid(row=0, column=1)

app_img_update = Image.open('img/update.png')
app_img_update = app_img_update.resize((18,18))
app_img_update = ImageTk.PhotoImage(app_img_update)
app_update = Button(frame_botoes,command=None, image=app_img_update, text="Atualizar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_update.grid(row=0, column=2)

app_img_delete = Image.open('img/delete.png')
app_img_delete = app_img_delete.resize((18,18))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(frame_botoes,command=None, image=app_img_delete, text="Deletar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_delete.grid(row=0, column=3)

app_img_adress = Image.open('img/andress.png')
app_img_adress = app_img_adress.resize((18,18))
app_img_adress = ImageTk.PhotoImage(app_img_adress)
app_adress = Button(frame_botoes,command=None, image=app_img_adress, text="CEP", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_adress.grid(row=0, column=4)

app_img_categoria = Image.open('img/cat.png')
app_img_categoria = app_img_categoria.resize((18,18))
app_img_categoria = ImageTk.PhotoImage(app_img_categoria)
app_categoria = Button(frame_botoes,command=cadastrar_categoria, image=app_img_categoria, text="Categoria", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_categoria.grid(row=0, column=5)

app_img_procurar = Image.open('img/procurar.png')
app_img_procurar = app_img_procurar.resize((18,18))
app_img_procurar = ImageTk.PhotoImage(app_img_procurar)
app_procurar = Button(frame_botoes,command=None, image=app_img_procurar, text="Procurar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_procurar.grid(row=0, column=6)

app_img_imagem = Image.open('img/imagem.png')
app_img_imagem = app_img_imagem.resize((18,18))
app_img_imagem = ImageTk.PhotoImage(app_img_imagem)
app_imagem = Button(frame_botoes,command=escolher_imagem, image=app_img_imagem, text="Carregar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_imagem.grid(row=0, column=7)

#******************************************************************************************************************************************************************************************
# Painel
l_id = Label(frame_painel, text="id:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_id.place(x=10, y=10)
e_id= Entry(frame_painel, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_id.place(x=70, y=10)

l_nome = Label(frame_painel, text="Nome:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_nome.place(x=10, y=40)
e_nome= Entry(frame_painel, width=30, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_nome.place(x=70, y=40)

l_ddd = Label(frame_painel, text="DDD:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_ddd.place(x=10, y=70)
e_ddd= Entry(frame_painel, width=5, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_ddd.place(x=70, y=70)

l_contato = Label(frame_painel, text="Contato:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_contato.place(x=120, y=70)
e_contato= Entry(frame_painel, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_contato.place(x=190, y=70)

c_categoria = ttk.Combobox(frame_painel, width=18, font=('Ivy 8 bold'))
c_categoria.set('Categorias')
c_categoria['values'] = None
c_categoria.place(x=10, y=100)

c_subcategoria = ttk.Combobox(frame_painel, width=18, font=('Ivy 8 bold'))
c_subcategoria.set('Subcategorias')
c_subcategoria['values'] = None
c_subcategoria.place(x=150, y=100)

l_email = Label(frame_painel, text="E-Mail:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_email.place(x=10, y=130)
e_email= Entry(frame_painel, width=30, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_email.place(x=70, y=130)

# Botão para abrir o calendário
bt_calendario = Button(frame_painel, text="Data", command=calendario)
bt_calendario.place(x=10, y=160)
# Campo de entrada para exibir a data selecionada
entry_data = Entry(frame_painel, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
entry_data.place(x=70, y=160)

l_idade = Label(frame_painel, text="Idade:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_idade.place(x=10, y=190)
e_idade= Entry(frame_painel, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_idade.place(x=70, y=190)

l_cep = Label(frame_painel, text="CEP:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_cep.place(x=10, y=220)
e_cep= Entry(frame_painel, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_cep.place(x=70, y=220)

l_endereco = Label(frame_painel, text="Logradouro:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_endereco.place(x=10, y=250)
e_endereco= Entry(frame_painel, width=50, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_endereco.place(x=175, y=250)

c_local = ttk.Combobox(frame_painel, width=10, font=('Ivy 8 bold'))
c_local.set('Rua')
c_local['values'] = ['Rua', 'Avenida', 'Travessa']
c_local.place(x=93, y=250)

l_numero = Label(frame_painel, text="Numero:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_numero.place(x=10, y=280)
e_numero= Entry(frame_painel, width=15, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_numero.place(x=70, y=280)

l_complemento = Label(frame_painel, text="Complemento:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_complemento.place(x=185, y=280)
e_complemento= Entry(frame_painel, width=15, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_complemento.place(x=285, y=280)

l_bairro = Label(frame_painel, text="Bairro:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_bairro.place(x=10, y=310)
e_bairro= Entry(frame_painel, width=15, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_bairro.place(x=70, y=310)

l_municipio = Label(frame_painel, text="Municipio:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_municipio.place(x=185, y=310)
e_municipio= Entry(frame_painel, width=15, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_municipio.place(x=265, y=310)

c_local = ttk.Combobox(frame_painel, width=10, font=('Ivy 8 bold'))
c_local.set('Estado')
c_local['values'] = ['AC','AL', 'AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
c_local.place(x=380, y=310)

def mostrar_contatos():
        
        app_nome = Label(frame_tabela, text="Tabela de Produtos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Definição do cabeçalho
        list_header = ['id', 'Nome', 'DDD', 'Contato', 'categoria',  'subcategoria','E_Mail', 'Nascimento', 'idade', 'CEP','','Endereço','numero', 'Complemento', 'Bairro','Municipio', 'Estado','imagem']
    
        # Obtém os dados do estoque
        df_list = ver_contato()  # Certifique-se de que essa função retorna os dados corretamente
    
        global tree_agenda
    
        # Criando a Treeview
        tree_agenda = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        # Barras de rolagem
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_agenda.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_agenda.xview)  # Corrigido aqui

        tree_agenda.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
        # Posicionando os widgets
        tree_agenda.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
    
        frame_tabela.grid_rowconfigure(0, weight=12)

        # Configuração das colunas
        hd = ["center", "nw", "nw", "center", "center", "center", "center", "center", "center","center", "center","nw","center","nw","nw","nw","center","nw"]
        h = [40, 150, 150, 70, 70, 150, 150, 100,100,40, 150, 150, 70, 70, 150, 150, 100,100, ]
    
        for n, col in enumerate(list_header):
            tree_agenda.heading(col, text=col.title(), anchor=NW)
            tree_agenda.column(col, width=h[n], anchor=hd[n])

        # Inserindo os dados
        if df_list:
            for item in df_list:
                tree_agenda.insert("", "end", values=item)
mostrar_contatos()    











root.mainloop()