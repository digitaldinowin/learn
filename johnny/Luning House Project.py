from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
motor_pair = MotorPair('A','E')
motor = Motor('C')
motor_speed = 50
motor1_speed = -50
turn_speed = 9
turn_speed2= turn_speed * 2

#completes the first objective
motor_pair.move(115, unit='cm', steering=0, speed=motor_speed)
motor.run_for_degrees(90, speed=motor1_speed)
motor_pair.move(turn_speed2, unit='cm', steering=100, speed=100)
motor_pair.move(-10, unit='cm', steering=0, speed=motor_speed)
motor.run_for_degrees(90, speed=-motor1_speed)
#completes the second objective
motor_pair.move(turn_speed, unit='cm', steering=-100, speed=motor_speed)
motor_pair.move(30, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(turn_speed, unit='cm', steering=-100, speed=motor_speed)
motor_pair.move(50, unit='cm', steering=0, speed=motor_speed)
motor.run_for_degrees(90, speed=motor1_speed)
motor_pair.move(turn_speed2, unit='cm', steering=100, speed=motor_speed)
motor.run_for_degrees(90, speed=-motor1_speed)
motor_pair.move(50, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(turn_speed, unit='cm', steering=100, speed=motor_speed)
motor_pair.move(30, unit='cm', steering=0, speed=motor_speed)
motor_pair.move(turn_speed, unit='cm', steering=-100, speed=motor_speed)
motor_pair.move(115, unit='cm', steering=0, speed=motor_speed)