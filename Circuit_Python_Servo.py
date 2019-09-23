import time

import board
import touchio
from adafruit_motor import servo
import pulseio

touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0!

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
x = 90
while True:
    my_servo.angle = x

    if touch_A1.value:
        if x<180:
            x += .5

    if touch_A2.value:

        if x>0:
            x -= .5


    print(x)

