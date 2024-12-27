import sqlite3 as sql

class TransactionObject:
    database = "Clientes.DB"
    conn = None
    cur = None
    Connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.Connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.Connected = False

    def execute(self, sql, parms=None):
        if TransactionObject.Connected:
            if parms is None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()  # Adicionado metodo fetchall no caso de falta

    def initDB(self):
        trans = TransactionObject()
        trans.connect()
        trans.execute("CREATE TABLE IF NOT EXISTS Clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.disconnect()

    def insert(self, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        print(f"Inserindo no banco: {nome}, {sobrenome}, {email}, {cpf}")  # Verifique os dados inseridos
        trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.conn.commit()  # Salva as alterações no banco de dados
        trans.disconnect()

    def view(self):
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.cur.fetchall()  # Corrigido para trans.cur.fetchall()
        trans.disconnect()
        return rows

    def search(self, nome="", sobrenome="", email="", cpf=""):
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def delete(self, id):
        trans = TransactionObject()
        trans.connect()
        print(f"Deletando o cliente com ID {id}")
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.conn.commit()  # Comita a transação
        trans.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        print(f"Atualizando ID {id} com os dados: {nome}, {sobrenome}, {email}, {cpf}")
        trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?",
                      (nome, sobrenome, email, cpf, id))
        trans.conn.commit()  # Comita a transação
        trans.disconnect()