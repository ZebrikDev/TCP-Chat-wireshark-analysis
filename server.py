import socket
import threading

HOST = '0.0.0.0'   
PORT = 50001    


clients = {}
clients_lock = threading.Lock()

def handle_client(client_socket, client_address):
    
    client_name = None
                                                                                                    
    try:
        client_name = client_socket.recv(1024).decode('utf-8').strip()

        if client_name == '':
            client_socket.send('ERROR: empty name is not allowed'.encode('utf-8'))
            return

        with clients_lock:
            if client_name in clients:
                client_socket.send('ERROR: this name is already connected'.encode('utf-8'))
                return
            clients[client_name] = client_socket

        print(f'[CONNECTED] {client_name} from {client_address}')
        client_socket.send('Connected to server. Use format TargetName:Message'.encode('utf-8'))

        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode('utf-8').strip()

            if ':' not in message:
                client_socket.send('ERROR: use format TargetName:Message'.encode('utf-8'))
                continue

            target_name, text = message.split(':', 1)
            target_name = target_name.strip()
            text = text.strip()

            if target_name == '' or text == '':
                client_socket.send('ERROR: target and message cannot be empty'.encode('utf-8'))
                continue

            with clients_lock:
                target_socket = clients.get(target_name)

            if target_socket is None:
                client_socket.send('ERROR: user not found'.encode('utf-8'))
            else:
                target_socket.send(f'From {client_name}: {text}'.encode('utf-8'))

    except Exception as error:
        print(f'[ERROR] client {client_address}: {error}')

    finally:
        if client_name is not None:
            with clients_lock:
                if clients.get(client_name) == client_socket:
                    del clients[client_name]
            print(f'[DISCONNECTED] {client_name}')

        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen(5)
    print(f'[LISTENING] Server is listening on {HOST}:{PORT}')

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        client_thread.start()


if __name__ == '__main__':
    start_server()
