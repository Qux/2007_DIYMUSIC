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
    pca0 = adafruit_pca9685.PCA9685(i2c, address=add0)
    pca1 = adafruit_pca9685.PCA9685(i2c, address=add1)

    print("set the number of channels")
    kit0 = ServoKit(channels=16, address=add0)
    kit1 = ServoKit(channels=16, address=add1)
    servo_channel10 = pca1.channels[0]
    servo_channel01 = pca0.channels[1]

    pca0.frequency = 50
    pca1.frequency = 50

    # set servo range
    kit0.servo[1].set_pulse_width_range(600,2400)
    kit0.servo[1].actuation_range = 180
    kit1.servo[0].set_pulse_width_range(600,2400)
    kit1.servo[0].actuation_range = 180

    print("make an servo instance")
    # REVIEW: I do not understand for what the below line is 
    #servo  = adafruit_motor.servo.Servo(servo_channel10)

    print("set the angle")
    kit1.servo[0].angle = 180
    kit0.servo[1].angle = 180
    time.sleep(1)
    kit1.servo[0].angle = 0
    kit0.servo[1].angle = 0
    print("end")

if __name__ == '__main__':
    print("Start servo_local.py")
    servotest()


