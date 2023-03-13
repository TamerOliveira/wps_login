from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    'wps@wps.com': ['1234', '12345678911'],
    'caio@wps.com': ['4321', '12345678912'],
    'tamer@wps.com': ['13579', '12345678913'],
    'teste@wps.com': ['4231', '12345678914'],
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
        if password != database[user][0]:
            return 'Senha invalida!', 401
        else:
            res = database[user][1]
            return ({
                "contrato": res,
            })


if __name__ == '__main__':
    app.run()
