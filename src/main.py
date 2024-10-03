from machine import I2S, Pin, UART
import network
import socket


SCK_PIN = 14
WS_PIN = 12
SD_PIN = 13
MUTE_PIN = 16

SSID = "Enter your SSID"
PASSWORD = "Your Wlan Password"

HOST = ""
PORT = 12345


def connect_wlan():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while True:
        if wlan.isconnected():
            print("Verbunden")
            print(wlan.ifconfig())
            break


def main():
    connect_wlan()

    audio_out = I2S(
        0,
        sck=Pin(SCK_PIN),
        ws=Pin(WS_PIN),
        sd=Pin(SD_PIN),
        mode=I2S.TX,
        bits=16,
        format=I2S.STEREO,
        rate=44100,
        ibuf=20000,
    )
    mute = Pin(Pin(MUTE_PIN), Pin.OUT)
    mute.value(1)
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_connection.bind((HOST, PORT))
    socket_connection.listen(1)
    connection, _ = socket_connection.accept()
    while True:
        music = connection.recv(2048)
        if not music:
            connection.close()
            break
        audio_out.write(music)


if __name__ == "__main__":
    main()
