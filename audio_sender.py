import socket

def send_audio_data_tcp(stream, audio, server_ip, server_port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((server_ip, server_port))

    try:
        while True:
            audio_data = stream.read(1024)
            connection.sendall(audio_data)
    finally:
        connection.close()
        stream.stop_stream()
        stream.close()
        audio.terminate()

