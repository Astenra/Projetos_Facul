from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Recebe os dados do login e senha da requisição
    login_data = request.get_json()
    login = login_data.get('login')
    senha = login_data.get('senha')
    
    # Retorna o mesmo login e senha
    return jsonify({'login': login, 'senha': senha})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
