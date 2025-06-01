from time import sleep

"""
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import RPi.GPIO as GPIO

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
"""


class BionicHandControlTest():
    """
    A mock/test class to simulate hand gesture controls and LED actions.
    This can be used for unit testing or demonstration purposes without needing hardware.
    """
    def __init__(self):
        pass 

    def idle(self):
        print("Idle gesture simulated.")
        
    def rock(self):
        print("Rock gesture simulated.")

    def paper(self):
        print("Paper gesture simulated.")

    def scissors(self):
        print("Scissors gesture simulated.")
        
    def ledOn(self):
        print("LED turned on.")

    def ledOff(self):
        print("LED turned off.")

    def CounterMove(self, gesture: str):
        if gesture == "rock":
            self.paper()
        elif gesture == "paper":
            self.scissors()
        elif gesture == "scissors":
            self.rock()
        elif gesture == "idle":
            self.idle()
        else:
            print(f"Unknown gesture: {gesture}")


if __name__ == "__main__":
    hand = BionicHandControlTest()
    
    hand.ledOn()

    
    for i in range(3):
        hand.paper()
        sleep(1) 
        hand.rock()
        sleep(1)
        hand.scissors()
        sleep(1)
        hand.rock()
        sleep(1)
        
    hand.rock()   
    
    hand.ledOff()


   

