import socket
import threading

pseudo = input("Choisissez un pseudo: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.7.13', 9090))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if message == 'NICK':
                client.send(pseudo.encode('utf8'))
            else:
                print(message)
        except:
            print("Une erreur est survenue!")
            client.close()
            break


def write():
    while True:
        message = f'{pseudo}: {input("")}'
        client.send(message.encode('utf8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
