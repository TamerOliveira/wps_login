from flask import Flask, jsonify, request

app = Flask(__name__) 
		
database = {
  "wps@wps.com": {
    "senha": "1234",
    "dados": {
      "contrato": "12345678912",
      "cnpj": "22.333.333/4444-22",
      "razao_social": "Empresa1"
    }
  },
  "tamer@wps.com": {
    "senha": "1235",
    "dados": {
      "contrato": "12345678913",
      "cnpj": "22.333.333/4444-22",
      "razao_social": "Empresa2"
    }
  },
  "caio@wps.com": {
    "senha": "1236",
    "dados": {
      "contrato": "12345678914",
      "cnpj": "22.333.333/4444-22",
      "razao_social": "Empresa3"
    }
  },
  "teste@wps.com": {
    "senha": "1237",
    "dados": {
      "contrato": "12345678915",
      "cnpj": "22.333.333/4444-22",
      "razao_social": "Empresa4"
    }
  }
}

@app.route('/')
def index():
    return 'ok', 200


@app.route('/login', methods=['POST']) 
def logins():
    login = request.get_json()
    user = login['username']
    password = login['password']
    if user not in database:
        return 'login invalido', 401
    else:
        if password != database[user]['senha']:
            return 'Senha invalida', 401
        else:
            json = database[user]['dados']
            return jsonify(json), 200

if __name__ == '__main__':
        app.run(debug= True)