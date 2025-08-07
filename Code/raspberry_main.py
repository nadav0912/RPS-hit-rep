import socket
import RPi.GPIO as GPIO
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from board import SCL, SDA

HOST = ''         # Listen on all interfaces
PORT = 8000      # Choose any unused port

class BionicHandControl():
    def __init__(self):
        # Create I2C bus
        i2c = busio.I2C(SCL, SDA)

        # Create PCA9685 object
        self.pca = PCA9685(i2c)
        self.pca.frequency = 50  # Typical servo frequency
        
        # Create servo objects on channels 0 to 4
        self.servos = [servo.Servo(self.pca.channels[i]) for i in range(5)]      # type: ignore
        
        self.open_angle = [180, 120, 113, 120, 123]
        self.close_angle = [55, 55, 55, 55, 45]
        
        # Led
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)

        
    def rock(self):
      for i in range(5):
          self.servos[i].angle = self.close_angle[i]


    def paper(self):
      for i in range(5):
          self.servos[i].angle = self.open_angle[i]

    def scissors(self):
        self.servos[1].angle = self.open_angle[1] + 10
        self.servos[2].angle = self.open_angle[2] + 10
        
        self.servos[0].angle = self.close_angle[0]
        self.servos[3].angle = self.close_angle[3]
        self.servos[4].angle = self.close_angle[4]
    
    def wait(self):
        for i in range(5):
          self.servos[i].angle = self.close_angle[i]
        
    def ledOn(self):
        GPIO.output(18, GPIO.HIGH)

    def ledOff(self):
        GPIO.output(18, GPIO.LOW)

    def zain(self):
        self.servos[2].angle = self.open_angle[2] + 10
        
        self.servos[0].angle = self.close_angle[0]
        self.servos[1].angle = self.close_angle[1]
        self.servos[3].angle = self.close_angle[3]
        self.servos[4].angle = self.close_angle[4]


if __name__ == "__main__":
    hand = BionicHandControl()      # Robotic hand class

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Create UDP socket
    sock.bind((HOST, PORT))                                     # Binds the socket to your IP and port
    print(f"UDP Listening on port {PORT}...")

    while True:

        # Recieve command
        data, addr = sock.recvfrom(1024)  # Receive from any client
        command = data.decode().strip().lower()
        print(f"Received: {data}")
        
        if command == "Zain":
            hand.zain()
        elif command == "rock":
            hand.rock()
        elif command == "paper":
            hand.paper()
        elif command == "scissors":
            hand.scissors()
        elif command == "wait":
            hand.wait()
        elif command == "ledOn":
            hand.ledOn()
        elif command == "ledOff":
            hand.ledOff()
        elif command == "quit":
            break
        else:
            print("Unknown command")

GPIO.cleanup()
print("Connection closed")