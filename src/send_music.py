#!/usr/bin/env python
from pathlib import Path
import socket


SONG = "CorazonesIntoxicadosCorregido-TheCasualties.wav"
PATH_TO_MUSICFILE = Path().home() / "Downloads" / SONG

WAV_HEADER_SIZE = 44
IP = "192.168.0.216"
PORT = 12345


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_connection:
        socket_connection.connect((IP, PORT))
        music = PATH_TO_MUSICFILE.read_bytes()
        socket_connection.sendall(music[WAV_HEADER_SIZE:])


if __name__ == "__main__":
    main()
