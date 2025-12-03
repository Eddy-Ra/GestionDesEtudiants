from flask import Flask, request

app = Flask(__name__)

clients = []


@app.route('/')
def home():
    return "Bienvenue au serveur de chat!"


@app.route('/send', methods=['POST'])
def send_message():
    message = request.form['message']
    clients.append(message)
    return "Message envoyé!"


@app.route('/messages')
def get_messages():
    return '<br>'.join(clients)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
