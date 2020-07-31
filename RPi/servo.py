import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo
from quxpy import metro
import time

from concurrent.futures import ThreadPoolExecutor

#Address_List = [0x40,0x41,]
Address_List = [0x40, 0x41, 0x42]
kits = []
Num_Channels = 16

# Thread handler
executor = ThreadPoolExecutor(max_workers=None)

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
        try:
            kits.append(create_servo(address))
        except ValueError:
            print("I2C Address", address, "not found, skipping")

def rotate(servo_id, angle):
    """ 
    servo_id: 0-44
    board_id = servo_id / 16
    channel_id = servo_id % 16
    """
    board_id = servo_id // Num_Channels
    channel_id = servo_id % Num_Channels
    
    # protect pushers
    if channel_id == 0:
        angle_limits = [49, 10.0, 60]
        for i in range(3):
            if board_id == i and angle > angle_limits[i]:
                angle = angle_limits[i]
    # adjust rotate angle
    else:
        if angle <= 5:
            angle = 5
        elif angle >= 173:
            angle = 173

    print(servo_id, angle)    
    kits[board_id].servo[channel_id].angle = angle

def set_angle(servo_id, angle):
    """
    - Add rotate queue
    """
    executor.submit(rotate, servo_id, angle)

def terminate():
    executor.shutdown()

setup()

