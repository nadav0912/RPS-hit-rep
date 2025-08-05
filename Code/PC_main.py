import socket

PI_IP = "192.168.137.2"  # Replace with your Pi's IP address
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with sock:
    print("Connected to Raspberry Pi!")

    while True:
        msg = input("Enter command (rock/paper/scissors/ledOn/ledOff/quit): ").strip()
        sock.sendto(msg.encode(), (PI_IP, PORT))

        if msg == "quit":
            print("Disconnected.")
            break