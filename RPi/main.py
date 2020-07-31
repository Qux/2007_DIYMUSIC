from quxpy import osc_receiver
from quxpy import osc_sender
from quxpy import metro

import servo
import led

### OSC Receivers
Servo_Port = 50000
Led_Port = 50001

servo_receiver = osc_receiver.OscReceiver(Servo_Port)
led_receiver = osc_receiver.OscReceiver(Led_Port)

### OSC Sender
Mac_IP = "192.168.0.10"
Mac_Port = 50000

def ping():
    osc_sender.send("/ping", 1.0)


try:
    ## setup metro
    metro.add(ping, 1.0)
    metro.add(led.show, 0.2)
    metro.start()

    ## setup osc_sender
    osc_sender.setup(Mac_IP, Mac_Port)

    ## setup OSC receivers
    servo_receiver.add("/servo", servo.set_angle)
    led_receiver.add("/hue", led.set_hue)
    led_receiver.add("/brightness", led.set_brightness)

    servo_receiver.start()
    led_receiver.start()
   
except KeyboardInterrupt:
    servo.terminate()
    servo_receiver.terminate()
    led_receiver.terminate()
    metro.terminate()
    
