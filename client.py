import socket
import threading


HOST = "SERVER_IP_HERE"
PORT = 50001

def receive_messages(sock):
    
    while True:
        try:
            msg = sock.recv(1024).decode()

            if msg:
                print(f"\n{msg}")
                print("> ", end="", flush=True)
            else:
                print("\n[DISCONNECTED] Server closed the connection.")
                break

        except:
            break


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print("[CONNECTED] Connected to server.")

        my_name = input("Enter your unique name: ").strip()
        client_socket.send(my_name.encode())

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()

        print("Write messages in this format: TargetName:Message")
        print("Example: Bob:Hello Bob")
        print("Type quit to exit.")

        while True:
            msg_to_send = input("> ").strip()

            if msg_to_send.lower() == "quit":
                break

            if ":" not in msg_to_send:
                print("Wrong format. Use: TargetName:Message")
                continue

            client_socket.send(msg_to_send.encode())

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        client_socket.close()
        print("\nClient closed.")


if __name__ == "__main__":
    start_client()
