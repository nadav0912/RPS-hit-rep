import socket
import RPi.GPIO as GPIO
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from board import SCL, SDA

# Create I2C bus
i2c = busio.I2C(SCL, SDA)

# Create PCA9685 object
pca = PCA9685(i2c)
pca.frequency = 50  # Typical servo frequency

# Create servo objects on channels 0 to 4
servos = [servo.Servo(pca.channels[i]) for i in range(5)]


class BionicHandControl():
    def __init__(self):
        # Create I2C bus
        i2c = busio.I2C(SCL, SDA)

        # Create PCA9685 object
        self.pca = PCA9685(i2c)
        self.pca.frequency = 50  # Typical servo frequency
        
        # Create servo objects on channels 0 to 4
        self.servos = [servo.Servo(pca.channels[i]) for i in range(5)]
        
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
        
        
    def ledOn(self):
        GPIO.output(18, GPIO.HIGH)

    def ledOff(self):
        GPIO.output(18, GPIO.LOW)


if __name__ == "__main__":
    import socket

    HOST = ''         # Listen on all interfaces
    PORT = 8000      # Choose any unused port

    hand = BionicHandControl()      # Robotic hand class

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Create socket
    sock.bind((HOST, PORT))                                     # Binds the socket to your IP and port
    sock.listen(1)                                              # Listen mode, accepts 1 client at a time

    with sock:
        print(f"Listening on port {PORT}...")
        conn, addr = sock.accept()          # conn - The connection socket, addr - (IP, port) of the connected client

        with conn:

            print(f"Connected by {addr}")

            while True:

                # Recieve command
                data = conn.recv(1024).decode().strip()
                if not data:
                    break
                print(f"Received: {data}")
                
                # Command handling
                if data == "rock":
                    hand.rock()
                elif data == "paper":
                    hand.paper()
                elif data == "scissors":
                    hand.scissors()
                elif data == "ledOn":
                    hand.ledOn()
                elif data == "ledOff":
                    hand.ledOff()
                elif data == "quit":
                    break
                else:
                    print("Unknown command")

        print("Connection closed")