
""" 
This is test
"""
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo
from quxpy import metro
import time

Address_List = [0x40,0x41,]
kits = []
Num_Channels = 16

def create_servo(board_address):
    """ 
    ikko no board no setup wo suru.
    hikisuu ha address
    """
    kit = ServoKit(channels=Num_Channels , address=board_address)
    for i in range(Num_Channels):
        kit.servo[i].set_pulse_width_range(600,2400)
        kit.servo[i].actuation_range = 180
    return kit

def setup():
    """
    servo driver no boards no setup wo suru.
    """
    for address in Address_List:
        kits.append(create_servo(address))

def angle_zero(i_kit, i_servo):
    kits[i_kit].servo[i_servo].angle = 0

def angle_plus(i_kit, i_servo):
    if kits[i_kit].servo[i_servo].angle >= 130:
        kits[i_kit].servo[i_servo].angle -= 120
    kits[i_kit].servo[i_servo].angle += 50
    print(kits[i_kit].servo[i_servo].angle) 
    
def servo(servo_id, angle):
    board_id = servo_id // Num_Channels
    channel_id = servo_id % Num_Channels
    kits[board_id].servo[channel_id].angle = angle
    

def test10():
    print("test10")
    angle_plus(1,0)

def test01():
    print("test01")
    angle_plus(0,1)


def servotest():
    angle_zero(1,0)
    angle_zero(0,1)

    metro.add(test10,1.0)
    metro.add(test01,1.5)

    try:
        metro.start()
        while True:
            print("main loop")  
            time.sleep(1)
    except KeyboardInterrupt:
        metro.terminate()
        print("finish")
            

setup()

if __name__ == '__main__':
    print("Start servo_local.py")
    servotest()


