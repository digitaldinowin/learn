from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

movement = MotorPair('C', 'D')
e = Motor('E')
movement.set_default_speed(50)
movement.set_motor_rotation(17.5)
e.set_default_speed(100)
f = DistanceSensor('F')

def waitf(condition, d):
    if condition == "<":
        f.wait_for_distance_closer_than(d)
    if condition == ">":
        f.wait_for_distance_farther_than(d)

def yourmom():
    e.run_for_degrees(180)
    movement.start()
    waitf(">", 15)
    movement.stop()
    e.run_for_degrees(-180)
    movement.move(-30)

yourmom()
