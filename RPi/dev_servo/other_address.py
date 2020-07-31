""" This is a tutorial from learn.adafruit.com """
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo
import time

def servotest():
    # setup i2c
    add0 = 0x40
    add1 = 0x41
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = adafruit_pca9685.PCA9685(i2c, address=add1)

    print("set the number of channels")
    kit = ServoKit(channels=16, address=add1)
    servo_channel = pca.channels[0]

    # set servo range
    kit.servo[0].set_pulse_width_range(600,2400)
    kit.servo[0].actuation_range = 180

    pca.frequency = 50

    print("make an servo instance")
    servo  = adafruit_motor.servo.Servo(servo_channel)

    print("set the angle")
    kit.servo[0].angle = 180
    time.sleep(1)
    kit.servo[0].angle = 0
    print("end")

if __name__ == '__main__':
    print("Start servo_local.py")
    servotest()


