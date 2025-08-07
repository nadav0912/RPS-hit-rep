import socket

class RaspberryMessage():
    def __init__(self):
        self.PI_IP = "192.168.137.2"  # Replace with your Pi's IP address
        self.PORT = 8000

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to Raspberry Pi!")
    
    def rock(self) -> None:
      self.message('rock')

    def paper(self) -> None:
      self.message('paper')

    def scissors(self) -> None:
        self.message('scissors')
    
    def idle(self) -> None:
        self.message('idle')
        
    def ledOn(self) -> None:
        self.message('ledOn')

    def ledOff(self) -> None:
        self.message('ledOff')

    def zain(self) -> None:
        self.message('zain')

    def message(self, msg: str) -> None:
        self.sock.sendto(msg.encode(), (self.PI_IP, self.PORT))