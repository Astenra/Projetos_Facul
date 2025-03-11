# Projeto: Servidor de Comunicação Simples

Este projeto consiste em implementar um servidor de comunicação simples que recebe um login e uma senha via requisição e retorna os mesmos dados como resposta. 

## Alunos
- **Eduardo Zoldan** - 2210169
- **Rafael Luiz** - 2211814
- **Gustavo Maia** - 2211155

---

## Tecnologias Utilizadas
- Linguagem de programação: **Python**
- Biblioteca: **Flask** (framework para criação de APIs)

---

## Requisitos
Certifique-se de que os seguintes itens estão instalados no seu sistema:
- Python 3.7 ou superior
- Gerenciador de pacotes pip

### Instalação de Dependências

1. Abra o terminal.
2. Instale o Flask utilizando o comando abaixo:
   ```bash
   pip install flask
   ```

---

## Configuração do Servidor

### Passos para Configuração e Execução do Servidor

1. **Clone este repositório** ou crie um diretório para o projeto.
2. **Crie o arquivo `server.py`** com o seguinte código:

   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route('/login', methods=['POST'])
   def login():
       data = request.get_json()
       login = data.get('login')
       senha = data.get('senha')
       return jsonify({"login": login, "senha": senha})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Execute o servidor** utilizando o comando:
   ```bash
   python server.py
   ```

4. O servidor estará disponível no endereço:
   ```
   http://127.0.0.1:5000/login
   ```

---

## Testando o Servidor

Para testar o servidor, você pode utilizar ferramentas como **Postman** ou **Insomnia**.

### Passos para Teste

1. Abra o Postman ou Insomnia.
2. Configure uma requisição do tipo **POST**.
3. Use o endpoint:
   ```
   http://127.0.0.1:5000/login
   ```
4. No corpo da requisição, envie os dados no formato JSON, como no exemplo abaixo:
   ```json
   {
       "login": "usuario_teste",
       "senha": "senha_teste"
   }
   ```
5. Envie a requisição e confira a resposta, que será:
   ```json
   {
       "login": "usuario_teste",
       "senha": "senha_teste"
   }
   ```

---

## Observações
- Certifique-se de que a porta 5000 está disponível no seu sistema.
- Se necessário, execute o terminal como administrador para evitar problemas de permissão.
- Para testes em outro dispositivo na mesma rede, substitua `127.0.0.1` pelo IP da máquina que está executando o servidor.

