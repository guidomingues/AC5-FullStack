#Precisa rodar com flask run
from app import app
from models.ModelConn import ClienteModel

@app.route('/cadastrar/', methods=["GET"])
def index():
    return ClienteModel.cadastrarEmail()