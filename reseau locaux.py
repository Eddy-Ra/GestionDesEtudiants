# server
import socket
import threading

# Configuration du serveur
host = '127.0.0.1'  # Adresse locale
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


# Diffuser les messages à tous les clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Gérer les messages des clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} a quitté le chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break



def receive():
    while True:
        client, address = server.accept()
        print(f'Connecté avec {str(address)}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Le pseudo du client est {nickname}!')
        broadcast(f'{nickname} a rejoint le chat!'.encode('utf-8'))
        client.send('Connecté au serveur!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('Le serveur est en cours d\'exécution...')
receive()
