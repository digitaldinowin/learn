from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
cd = MotorPair('C', 'D')
b = ColorSensor('B')

def hi(motors, color, speed=100, correction=0, angle=0.9, timeout=1.5):
    timer = Timer()
    while timer.now() < 1.5:
        if color.get_reflected_light > 50:
            motors.start_tank_at_power(speed * angle, speed)
            timer.reset()
        else:
            motors.start_tank_at_power(speed, speed * correction)

hi(cd, b)