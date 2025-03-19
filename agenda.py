from imports import*

root = tk.Tk()
root.title("Agenda")
root.geometry("1200x950")
root.configure(background=co1)
root.resizable(width=False, height=False)
#root.overrideredirect(1)
largura_root = 1200
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
frame_logo = Frame(root, width=1200, height=52, bg=co1)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_botoes = Frame(root, width=1200, height=65, bg=co1)
frame_botoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_painel = Frame(root, width=1200, height=500, bg=co1)
frame_painel.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

frame_tabela= Frame(root, width=1200, height=200, bg=co1)
frame_tabela.grid(row=6, column=0, pady=0, padx=10, sticky=NSEW)

#********************************************************************************************************************************
# Trabalhando no frame logo
app_lg = Image.open('img/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Agenda", width=1200, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

#***************************************************************************************************************************************
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






root.mainloop()