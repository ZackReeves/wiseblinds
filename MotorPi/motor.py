from gpiozero import Servo 
import time


class Motor:
    def __init__(self):
        self.motor_pin = 17
        self.correction = 0
        self.maxPWM = (2+self.correction)/1000
        self.minPWM = (1-self.correction)/1000

        self.servo = Servo(self.motor_pin,min_pulse_width=self.minPW,max_pulse_width=self.maxPW)

        self.time_to_close = 5

        self.current_state = 1
        #state will be the input to show if we need to open the curtains:1 , close the curtains:0, or open them halfway: 0.5

    def move_curtains(self, next_state):
        if self.current_state == next_state:
            print("do nothing")
        else:
            if next_state > self.current_state:
                #turns one way for the number of seconds needed to get to the next state
                self.servo.value =-0.16
                print("stop")
                time.sleep(1)
                self.servo.value =-0.5 #test to see if this is the right direction
                print("go")
                time.sleep(abs(next_state-self.current_state)*self.time_to_close)
                self.servo.value =-0.16
                print("stop")
                time.sleep(1)
                print("test")
                self.current_state = next_state
            else:
                #turns one way for the number of seconds needed to get to the next state
                self.servo.value =-0.16
                print("stop")
                time.sleep(1)
                self.servo.value =0.5
                print("go") #test to see if this is the right direction
                time.sleep(abs(next_state-self.current_state)*self.time_to_close)
                self.servo.value =-0.16
                print("stop")
                time.sleep(1)
                print("test")
                self.current_state = next_state

