import socket
import threading

host = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
noms = []

def mess(message):
    for client in clients:
        client.send(message)

def hand_client(client):
    while True:
        try:
            message = client.recv(1024)
            mess(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nom1 = noms[index]
            mess(f'{nom1} a quitté'.encode('utf8'))
            noms.remove(nom1)
            break

def receive():
    while True:
        client, adresse = server.accept()
        print(f"Connexion établie {str(adresse)}")

        client.send('NICK'.encode('utf8'))
        nom1 = client.recv(1024).decode('utf8')
        noms.append(nom1)
        clients.append(client)

        print(f"Le pseudo est {nom1}")
        mess(f'{nom1} a rejoint le chat!'.encode('utf8'))
        client.send('Connecté au serveur!'.encode('utf8'))

        thread = threading.Thread(target=hand_client, args=(client,))
        thread.start()

print("Le serveur est en fonction...")
receive()
