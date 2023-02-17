from gpiozero import Servo 
import time

class Motor:
    def __init__(self):
        self.motor_pin = 17
        self.correction = 0

        self.maxPWM = 2300/1000000
        self.minPWM = 700/1000000

        self.servo = Servo(self.motor_pin,min_pulse_width=self.minPWM,max_pulse_width=self.maxPWM)

        self.time_to_close = 6

        self.current_state = 0 #0:closed 1:open

        self.speed = 0.5
        self.stop = -0.0025
        self.direction = 1

    def stop_motor(self):
        #self.motor_pin = 27
        self.servo.value = self.stop
        time.sleep(1)
    
    def move(self, next_state):
        if self.current_state != next_state:
            if next_state > self.current_state:
                self.direction = 1
            else:
                self.direction = -1

            self.stop_motor()

            self.servo.value = self.direction * self.speed
            time.sleep(abs(next_state-self.current_state)*self.time_to_close)
                
            self.stop_motor()

            self.current_state = next_state
        else:
            self.stop_motor()
            print("do nothing")