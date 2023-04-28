from audio_capture import get_audio_input
from audio_sender import send_audio_data_tcp

if __name__ == "__main__":
    stream, audio = get_audio_input()

    server_ip = "127.0.0.1"  # server IP
    server_port = 12345  # server port

    send_audio_data_tcp(stream, audio, server_ip, server_port)

