from tkinter import *

class GUI():
    """Classe da Interface Gráfica
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self):
        # Criando uma janela
        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        # Definição das variáveis que recebem os dados inseridos pelo usuário
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Criando os objetos que farão parte das janelas
        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblcpf = Label(self.window, text="CPF")

        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar selecionados")
        self.btnDel = Button(self.window, text="Deletar selecionados")
        self.btnClose = Button(self.window, text="Fechar")

        # Associando objetos ao Grid da janela
        self.lblnome.grid(column=0, row=0)
        self.lblsobrenome.grid(column=0, row=1)
        self.lblemail.grid(column=0, row=2)
        self.lblcpf.grid(column=0, row=3)

        self.entNome.grid(column=1, row=0, padx=50, pady=50)
        self.entSobrenome.grid(column=1, row=1)
        self.entEmail.grid(column=1, row=2)
        self.entCPF.grid(column=1, row=3)

        self.listClientes.grid(column=2, row=0, rowspan=10)
        self.scrollClientes.grid(column=6, row=0, rowspan=10)

        self.btnViewAll.grid(column=0, row=4, columnspan=2)
        self.btnBuscar.grid(column=0, row=5, columnspan=2)
        self.btnInserir.grid(column=0, row=6, columnspan=2)
        self.btnUpdate.grid(column=0, row=7, columnspan=2)
        self.btnDel.grid(column=0, row=8, columnspan=2)
        self.btnClose.grid(column=0, row=9, columnspan=2)

        # Conectando o Scrollbar com a ListBox
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Adicionando estilo (swag)
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(sticky='NS', padx=0, pady=0)
            elif widget_class == "Scrollbar":
                child.grid_configure(sticky='NS', padx=0, pady=0)
            else:
                child.grid_configure(sticky='N', padx=self.x_pad, pady=self.y_pad)

    def run(self):
        self.window.mainloop()