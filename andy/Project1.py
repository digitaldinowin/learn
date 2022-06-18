from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import random

hub = PrimeHub()

rickroll = "never gonna give you up never gonna let you down never gonna run around and desert you"
hub.light_matrix.show_image('ARROW_W')

morbin = ColorSensor('F')
morbius = MotorPair('A', 'E')
print(rickroll)
fsdfsfd = 0

while True:
    if morbin.get_color() == 'red':
        morbius.start(0, -69)
    else:
        morbius.stop()
        print(fsdfsfd)
        if fsdfsfd == 0:
            morbius.move(15, 'cm', speed=-10)
            morbius.move_tank(-90, 'degrees', left_speed=-10, right_speed=0)
            fsdfsfd = 1
        if fsdfsfd == 1:
            morbius.move_tank(180, 'degrees', left_speed=0, right_speed=-10)
            fsdfsfd = 0
