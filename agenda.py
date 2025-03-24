from imports import*
from views import*
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Agenda")
root.geometry("980x750")
root.configure(background=co1)
root.resizable(width=False, height=False)
#root.overrideredirect(1)
largura_root = 980
altura_root = 750
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

frame_painel = Frame(root, width=980, height=380, bg=co1)
frame_painel.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

frame_tabela= Frame(root, width=980, height=453, bg=co0)
frame_tabela.grid(row=6, column=0, pady=0, padx=10, sticky=NSEW)

#********************************************************************************************************************************
# Trabalhando no frame logo
img_logo = Image.open("img/logo.png")
img_logo = img_logo.resize((50, 50))  # Ajusta o tamanho da imagem
img_logo = ImageTk.PhotoImage(img_logo)
app_lg = Label(frame_logo, image=img_logo, text="Agenda", width=1200, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_lg.place(x=0, y=0)

#***************************************************************************************************************************************
# Função para abrir o calendário e capturar a data
def calendario():
    def pegar_data():
        data_selecionada = cal.selection_get()  # Obtém a data selecionada
        entry_data.delete(0, END)  # Limpa o Entry
        entry_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))  # Insere a data formatada no Entry
        calendario_janela.destroy()  # Fecha o calendário
        calcular_idade()  # Chama a função de calcular idade automaticamente

    # Criar uma nova janela para o calendário
    calendario_janela = Toplevel(root)
    calendario_janela.title("Selecione a Data")
    calendario_janela.geometry("300x300")
    calendario_janela.resizable(width=False, height=False)
    largura_root = 300
    altura_root = 300
    #obter tamanho da tela
    largura_tela = calendario_janela.winfo_screenwidth()
    altura_tela = calendario_janela.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    calendario_janela.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

    # Criando o calendário dentro da nova janela
    cal = Calendar(calendario_janela, date_pattern="dd/mm/yyyy")
    cal.pack(pady=20)

    # Botão para confirmar a seleção da data
    btn_selecionar = Button(calendario_janela, text="Selecionar", command=pegar_data)
    btn_selecionar.pack(pady=10)

    def calcular_idade():
        data_nasc_str = entry_data.get()  # Obtém a data digitada/selecionada no Entry
        if not data_nasc_str:  # Se estiver vazio, não faz nada
            return
        try:
            data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y")  # Converte para formato de data
            data_atual = datetime.today()  # Obtém a data atual
        
            # Calcular idade inteira
            idade_anos = data_atual.year - data_nasc.year
            if (data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day):
                idade_anos -= 1  # Ajuste para aniversários ainda não ocorridos
        
            # Calcular diferença em dias desde o último aniversário
            ultimo_aniversario = datetime(data_atual.year, data_nasc.month, data_nasc.day)
            if data_atual < ultimo_aniversario:
                ultimo_aniversario = datetime(data_atual.year - 1, data_nasc.month, data_nasc.day)
        
            dias_desde_aniversario = (data_atual - ultimo_aniversario).days
            dias_no_ano = 365.25  # Considerando anos bissextos
        
            # Idade em decimal = anos completos + fração do ano
            idade_decimal = idade_anos + (dias_desde_aniversario / dias_no_ano)

            e_idade.delete(0, END)  # Limpa o campo antes de inserir o novo valor
            e_idade.insert(0, str(idade_anos))  # Exibe a idade como número inteiro
        except ValueError:
            e_idade.delete(0, END)
            e_idade.insert(0, "Erro") 
#-------------------------------  
def buscar_cep():
    cep = e_cep.get().strip().replace("-", "")  # Remove espaços e traços do CEP
    if len(cep) != 8 or not cep.isdigit():
        e_endereco.delete(0, END)
        e_bairro.delete(0, END)
        e_municipio.delete(0, END)
        e_endereco.insert(0, "CEP inválido")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" in dados:
            e_endereco.delete(0, END)
            e_bairro.delete(0, END)
            e_municipio.delete(0, END)
            e_endereco.insert(0, "CEP não encontrado")
        else:
            e_endereco.delete(0, END)
            e_bairro.delete(0, END)
            e_municipio.delete(0, END)

            e_endereco.insert(0, dados['logradouro'])
            e_bairro.insert(0, dados['bairro'])
            e_municipio.insert(0, f"{dados['localidade']} - {dados['uf']}")
    else:
        e_endereco.delete(0, END)
        e_bairro.delete(0, END)
        e_municipio.delete(0, END)
        e_endereco.insert(0, "Erro na consulta")
#-------------------------------         
def cadastrar_categoria():
    
    global root
    
    #Criando a janela
    root1 = Toplevel(root) 
    root1.title("Categoria")
    root1.geometry("200x200")
    root.configure(background=co1)
    root1.resizable(width=False, height=False)
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
    
    def nova_categoria():
        nome = e_categoria.get().strip()  # Remove espaços extras
        if nome == "":
            messagebox.showerror("Erro", "Preencha o campo!")
            return
        # Define the criar_categoria function or import it from the appropriate module
        def criar_categoria(categorias):
            # Add logic to handle the category creation
            print(f"Categoria criada: {categorias}")
        
        criar_categoria([nome])  # Adiciona ao banco
        messagebox.showinfo("Sucesso", "Categoria cadastrada com sucesso!")
        root1.destroy()
        
    def nova_subcategoria():
        nome = e_subcategoria.get().strip()  # Remove espaços extras
        if nome == "":
            messagebox.showerror("Erro", "Preencha o campo!")
            return
        def criar_subcategoria(subcategorias):
            # Add logic to handle the subcategory creation
            print(f"Subcategoria criada: {subcategorias}")
        
        criar_subcategoria([nome])  # Adiciona ao banco
        messagebox.showinfo("Sucesso", "Subcategoria cadastrada com sucesso!")  
        root1.destroy() 
        
    
    
        
      
    
        
    
    
    frame_painel_cat = Frame(root1, width=200, height=200, bg=co1)
    frame_painel_cat.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)
    
    l_categoria = Label(frame_painel_cat, text="Categoria", font=('Ivy 10 bold'), bg=co1, fg=co0)
    l_categoria.place(x=60, y=10)
    e_categoria= Entry(root1, width=19, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_categoria.place(x=35, y=40)
    
    
    app_img_add = Image.open('img/save.png')
    app_img_add = app_img_add.resize((18,18))
    app_img_add = ImageTk.PhotoImage(app_img_add)
    app_add = Button(frame_painel_cat,command=nova_categoria, image=app_img_add, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
    app_add.place(x=10 , y=60)
    
    app_img_del_cat = Image.open('img/delete.png')
    app_img_del_cat = app_img_del_cat.resize((18,18))
    app_img_del_cat = ImageTk.PhotoImage(app_img_del_cat)
    app_del_cat = Button(frame_painel_cat,command=None, image=app_img_del_cat, text="Delete", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
    app_del_cat.place(x=100, y=60)
    #-----------------------------------------------------------------------
    l_subcategoria = Label(frame_painel_cat, text="Subcategoria", font=('Ivy 10 bold'), bg=co1, fg=co0)
    l_subcategoria.place(x=60, y=110)
    e_subcategoria= Entry(frame_painel_cat, width=19, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_subcategoria.place(x=35, y=140)     
    
   
    app_img_subc = Image.open('img/save.png')
    app_img_subc = app_img_subc.resize((18,18))
    app_img_subc = ImageTk.PhotoImage(app_img_subc)
    app_subc = Button(frame_painel_cat,command=nova_subcategoria, image=app_img_subc, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
    app_subc.place(x=10 , y=160)
    
    app_img_del_sub = Image.open('img/delete.png')
    app_img_del_sub = app_img_del_sub.resize((18,18))
    app_img_del_sub = ImageTk.PhotoImage(app_img_del_sub)
    app_del_del_sub = Button(frame_painel_cat,command=None, image=app_img_del_sub, text="Delete", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
    app_del_del_sub.place(x=100, y=160)
#************************************************************************************
def cadastrar_contato():
    
    nome = e_nome.get().strip()
    ddd = e_ddd.get().strip()
    contato = e_contato.get().strip()
    categoria = c_categoria.get().strip()
    subcategoria = c_subcategoria.get().strip()
    email = e_email.get().strip()
    nascimento = entry_data.get().strip()
    idade = e_idade.get().strip()
    cep = e_cep.get().strip()
    endereco = e_endereco.get().strip()
    numero = e_numero.get().strip()
    complemento = e_complemento.get().strip()
    bairro = e_bairro.get().strip()
    municipio = e_municipio.get().strip()
    
    # **Verificar apenas campos essenciais**
    if not nome or not contato or not categoria:
        messagebox.showerror('Erro', 'Nome, Contato e Categoria são obrigatórios!')
        return

    # **Salvar valores opcionais como "" caso estejam vazios**
    lista = [
        nome, ddd or "", contato, categoria, subcategoria or "", email or "", 
        nascimento or "", idade or "", cep or "", endereco or "", numero or "", 
        complemento or "", bairro or "", municipio or ""
    ]
    
    # **Adicionar contato ao banco**
    criar_contato(lista)
    messagebox.showinfo('Sucesso', 'Contato cadastrado com sucesso!')

    # **Limpar campos após cadastro**
    e_nome.delete(0, END)
    e_ddd.delete(0, END)
    e_contato.delete(0, END)
    c_categoria.set("")  # Para Combobox, usa `set("")`
    c_subcategoria.set("")
    e_email.delete(0, END)
    entry_data.delete(0, END)
    e_idade.delete(0, END)
    e_cep.delete(0, END)
    e_endereco.delete(0, END)
    e_numero.delete(0, END)
    e_complemento.delete(0, END)
    e_bairro.delete(0, END)
    e_municipio.delete(0, END)
    
    # **Atualizar a lista de contatos na interface**
    mostrar_contatos()
 
def update_contato():
    try:
        tree_itens = tree_agenda.focus()
        tree_dicionario = tree_agenda.item(tree_itens)
        tree_lista = tree_dicionario['values']

        if not tree_lista:
            messagebox.showerror('Erro', 'Selecione um contato na tabela')
            return

        valor_id = tree_lista[0]  # ID do contato

        # Limpa os campos antes de preencher com os dados selecionados
        e_nome.delete(0, END)
        e_ddd.delete(0, END)
        e_contato.delete(0, END)
        c_categoria.set("")  
        c_subcategoria.set("")
        e_email.delete(0, END)
        entry_data.delete(0, END)
        e_idade.delete(0, END)
        e_cep.delete(0, END)
        e_endereco.delete(0, END)
        e_numero.delete(0, END)
        e_complemento.delete(0, END)
        e_bairro.delete(0, END)
        e_municipio.delete(0, END)

        # Preenche os campos com os dados do contato selecionado
        e_nome.insert(0, tree_lista[1])
        e_ddd.insert(0, tree_lista[2])
        e_contato.insert(0, tree_lista[3])
        c_categoria.set(tree_lista[4])
        c_subcategoria.set(tree_lista[5])
        e_email.insert(0, tree_lista[6])
        entry_data.insert(0, tree_lista[7])
        e_idade.insert(0, tree_lista[8])
        e_cep.insert(0, tree_lista[9])
        e_endereco.insert(0, tree_lista[10])
        e_numero.insert(0, tree_lista[11])
        e_complemento.insert(0, tree_lista[12])
        e_bairro.insert(0, tree_lista[13])
        e_municipio.insert(0, tree_lista[14])

        # Função interna para salvar a atualização
        def update():
            nome = e_nome.get().strip()
            ddd = e_ddd.get().strip()
            contato = e_contato.get().strip()
            categoria = c_categoria.get().strip()
            subcategoria = c_subcategoria.get().strip()
            email = e_email.get().strip()
            nascimento = entry_data.get().strip()
            idade = e_idade.get().strip()
            cep = e_cep.get().strip()
            endereco = e_endereco.get().strip()
            numero = e_numero.get().strip()
            complemento = e_complemento.get().strip()
            bairro = e_bairro.get().strip()
            municipio = e_municipio.get().strip()

            # Criar lista com os dados para atualização
            lista = [nome, ddd, contato, categoria, subcategoria, email, nascimento, idade, cep, endereco, numero, complemento, bairro, municipio, valor_id]

            # Verifica se algum campo está vazio
            if any(campo == '' for campo in lista[:-1]):  # Exclui o ID da verificação
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return

            # Atualiza no banco de dados
            atualizar_contato(lista)

            # Mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

            # Limpa os campos após a atualização
            e_nome.delete(0, END)
            e_ddd.delete(0, END)
            e_contato.delete(0, END)
            c_categoria.set("")  
            c_subcategoria.set("")
            e_email.delete(0, END)
            entry_data.delete(0, END)
            e_idade.delete(0, END)
            e_cep.delete(0, END)
            e_endereco.delete(0, END)
            e_numero.delete(0, END)
            e_complemento.delete(0, END)
            e_bairro.delete(0, END)
            e_municipio.delete(0, END)

            # Atualiza a exibição da tabela
            mostrar_contatos()

            # Destroi o botão após a atualização
            botao_update.destroy()

        # Cria o botão "Salvar e Atualizar"
        botao_update = Button(frame_botoes, command=update, text='Salvar e Atualizar'.upper(),
                              width=18, overrelief=RIDGE, font=('Ivy 10'), bg=co3, fg=co1)
        botao_update.grid(row=0, column=7)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um contato na tabela')
    
def deletar_contato():
    try:
        # Pegar o item selecionado na treeview
        tree_itens = tree_agenda.focus()
        tree_dicionario = tree_agenda.item(tree_itens)
        tree_lista = tree_dicionario['values']

        # Verifica se algum item foi selecionado
        if not tree_lista:
            messagebox.showerror('Erro', 'Selecione um usuário na tabela')
            return

        valor_id = tree_lista[0]  # ID do contato a ser deletado

        # Confirmação antes de excluir
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este contato?")
        if not resposta:
            return

        # Deletar do banco de dados usando a função correta
        deletar_contato(valor_id)

        # Mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Contato deletado com sucesso!')

        # Atualizar a tabela após exclusão
        mostrar_contatos()

    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao deletar contato: {str(e)}')
        
#********************************************************************************************************************************    
# Botoes Cabeçalho
app_img_add = Image.open('img/save.png')
app_img_add = app_img_add.resize((18,18))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(frame_botoes,command=cadastrar_contato, image=app_img_add, text="Salvar", width=80, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_add.grid(row=0, column=1)

app_img_update = Image.open('img/update.png')
app_img_update = app_img_update.resize((18,18))
app_img_update = ImageTk.PhotoImage(app_img_update)
app_update = Button(frame_botoes,command=update_contato, image=app_img_update, text="Atualizar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_update.grid(row=0, column=2)

app_img_delete = Image.open('img/delete.png')
app_img_delete = app_img_delete.resize((18,18))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(frame_botoes,command=deletar_contato, image=app_img_delete, text="Deletar", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
app_delete.grid(row=0, column=3)

app_img_adress = Image.open('img/andress.png')
app_img_adress = app_img_adress.resize((18,18))
app_img_adress = ImageTk.PhotoImage(app_img_adress)
app_adress = Button(frame_botoes,command=buscar_cep, image=app_img_adress, text="CEP", width=90, compound=LEFT, overrelief=RIDGE ,font=('Ivy 11'), bg=co1, fg=co0)
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
c_categoria['values'] = ver_categoria()
c_categoria.place(x=10, y=100)

c_subcategoria = ttk.Combobox(frame_painel, width=18, font=('Ivy 8 bold'))
c_subcategoria.set('Subcategorias')
c_subcategoria['values'] = ver_subcategoria()
c_subcategoria.place(x=150, y=100)

l_email = Label(frame_painel, text="E-Mail:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_email.place(x=10, y=130)
e_email= Entry(frame_painel, width=30, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_email.place(x=70, y=130)

# Botão para abrir o calendário
bt_calendario = Button(frame_painel, text="Data", command=calendario)
bt_calendario.place(x=10, y=160)
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
e_endereco.place(x=93, y=250)

l_numero = Label(frame_painel, text="Numero:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_numero.place(x=10, y=280)
e_numero= Entry(frame_painel, width=15, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_numero.place(x=70, y=280)

l_complemento = Label(frame_painel, text="Complemento:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_complemento.place(x=185, y=280)
e_complemento= Entry(frame_painel, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
e_complemento.place(x=285, y=280)

l_bairro = Label(frame_painel, text="Bairro:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_bairro.place(x=10, y=310)
e_bairro= Entry(frame_painel, width=15, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_bairro.place(x=70, y=310)

l_municipio = Label(frame_painel, text="Municipio:", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_municipio.place(x=185, y=310)
e_municipio= Entry(frame_painel, width=25, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_municipio.place(x=265, y=310)



def mostrar_contatos():
        
        app_nome = Label(frame_tabela, text="Tabela de Produtos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Definição do cabeçalho
        list_header = ['id','Nome', 'DDD', 'Contato', 'categoria',  'subcategoria','E_Mail', 'Nascimento', 'idade', 'CEP','Endereço','numero', 'Complemento', 'Bairro','Municipio', 'imagem']
    
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
        hd = ["center", "nw", "nw", "center", "center", "center", "center", "center", "center", "center","nw","center","nw","nw","nw","nw"]
        h = [40, 100, 40, 70, 70, 70, 150, 100,100,150, 150, 70, 70, 150, 150, 100, ]
    
        for n, col in enumerate(list_header):
            tree_agenda.heading(col, text=col.title(), anchor=NW)
            tree_agenda.column(col, width=h[n], anchor=hd[n])

        # Inserindo os dados
        if df_list:
            for item in df_list:
                tree_agenda.insert("", "end", values=item)
mostrar_contatos()    











root.mainloop()