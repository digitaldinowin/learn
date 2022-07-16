from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
motor=MotorPair('E','F')
color=ColorSensor('A')
power=20
while 1!=2 :
    if color!='red':
        motor.start_tank_at_power(7.5,power)
    if color=='red':
        motor.start_tank_at_power(7.5,power)