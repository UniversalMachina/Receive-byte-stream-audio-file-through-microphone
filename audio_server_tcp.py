import socket

def start_tcp_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)

    print(f"Server is listening on {ip}:{port}")

    while True:
        connection, client_address = server_socket.accept()

        print(f"Connection from {client_address}")

        try:
            while True:
                audio_data = connection.recv(1024)

                if not audio_data:
                    break

                print(f"Received audio data: {audio_data}")

        finally:
            connection.close()

if __name__ == "__main__":
    server_ip = "127.0.0.1"  # server IP
    server_port = 12345  #  server port
    start_tcp_server(server_ip, server_port)
