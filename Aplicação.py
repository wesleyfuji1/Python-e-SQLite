from tkinter import *
import Backend as core
from Interface import GUI # Importa o backend

app = None
selected = None  # Variável para armazenar a linha selecionada na lista

def view_command():
    trans = core.TransactionObject()  # Instancia a classe
    rows = trans.view()
    app.listClientes.delete(0, END)  # Limpa a Listbox
    for r in rows:
        # Formatando a exibição para exibir de forma legível
        id_cliente = r[0]
        nome = r[1]
        sobrenome = r[2]
        email = r[3]
        cpf = r[4]
        # A string a ser exibida na Listbox, mas a tupla será mantida no backend
        display_text = f"{id_cliente} {nome} {sobrenome} - {email} - {cpf}"
        # Inserindo a tupla completa, mas exibindo apenas a versão formatada
        app.listClientes.insert(END, display_text)  # Aqui não precisamos mais de uma tupla com a string formatada

def search_command():
    app.listClientes.delete(0, END)
    trans = core.TransactionObject()
    rows = trans.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    nome = app.txtNome.get()
    sobrenome = app.txtSobrenome.get()
    email = app.txtEmail.get()
    cpf = app.txtCPF.get()
    trans = core.TransactionObject()
    trans.insert(nome, sobrenome, email, cpf)
    view_command()  # Exibe todos os registros novamente após a inserção

def update_command():
    # Verifica se há um item selecionado na Listbox
    if selected:
        id_cliente = selected[0]  # O primeiro valor da tupla é o ID
        nome = app.txtNome.get()
        sobrenome = app.txtSobrenome.get()
        email = app.txtEmail.get()
        cpf = app.txtCPF.get()
        # Chama a função de atualização no backend
        trans = core.TransactionObject()
        trans.update(id_cliente, nome, sobrenome, email, cpf)
        view_command()  # Atualiza a lista após a atualização
    else:
        print("Nenhum cliente selecionado para atualização.")

def del_command():
    # Verifica se há um item selecionado na Listbox
    if selected:
        id_cliente = selected[0]  # O primeiro valor da tupla é o ID
        # Chama a função de deleção no backend
        trans = core.TransactionObject()
        trans.delete(id_cliente)
        view_command()  # Atualiza a lista após a exclusão
    else:
        print("Nenhum cliente selecionado para exclusão.")

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]  # Obtém o índice do item selecionado

    # Obtenha a tupla completa do banco de dados (o metodo view() já retorna os dados completos)
    rows = trans.view()  # Obtém todos os registros
    selected = rows[index]  # Pega a tupla completa de acordo com o índice selecionado

    # Agora 'selected' é a tupla (id, nome, sobrenome, email, cpf)
    nome = selected[1]
    sobrenome = selected[2]
    email = selected[3]
    cpf = selected[4]

    # Preenchendo os campos de entrada
    app.entNome.delete(0, END)
    app.entNome.insert(END, nome)

    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, sobrenome)

    app.entEmail.delete(0, END)
    app.entEmail.insert(END, email)

    app.entCPF.delete(0, END)
    app.entCPF.insert(END, cpf)

    return selected

if __name__ == "__main__":
    app = GUI()  # Cria a interface gráfica
    app.listClientes.bind("<<ListboxSelect>>", getSelectedRow)  # Vincula evento de seleção

    # Chama o metodo que garante a criação da tabela no banco de dados
    trans = core.TransactionObject()
    trans.initDB()  # Cria a tabela 'clientes' se ela não existir

    # Conecta os botões aos comandos
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)

    view_command()  # Exibe todos os registros ao iniciar a aplicação

    app.run()  # Inicia o loop da interface gráfica