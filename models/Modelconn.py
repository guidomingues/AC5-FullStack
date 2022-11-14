from app import app
from flask_mysqldb import MySQL

mysql = MySQL(app)


class ClienteModel():

    def cadastrarEmail():
        nome = 'Guilherme'
        email = 'guilhermedomingues@impacta.com'
        telefone = '11 987654321'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes (nome, email, telefone) VALUES(%s,%s,%s)''',(nome,email,telefone))
        mysql.connection.commit()
        cursor.close()

        return 'Criado com sucesso'