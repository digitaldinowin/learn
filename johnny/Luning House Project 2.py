from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

motor_speed = 50
motor_pair = MotorPair('A', 'E')
motor = Motor('C')
right = 100
left = -100

motor_pair.move(135, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(9, unit='cm', steering=right, speed=motor_speed)
motor_pair.move(15, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(9, unit='cm', steering=left, speed=motor_speed)
motor_pair.move(18, unit='cm', steering=right, speed=motor_speed)
motor_pair.move(-10, unit='cm', steering=0, speed=motor_speed)
motor.run_for_degrees(-180, speed=100)
motor_pair.move(10, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(9, unit='cm', steering=right, speed=motor_speed)
motor_pair.move(10, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(9, unit='cm', steering=right, speed=motor_speed)
motor_pair.move(70, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(9, unit='cm', steering=right, speed=motor_speed)
motor_pair.move(40, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(9, unit='cm', steering=left, speed=motor_speed)
motor_pair.move(-20, unit='cm', steering=left, speed=motor_speed)
motor.run_for_degrees(180, speed=100)
motor.run_for_degrees(-180, speed=100)
