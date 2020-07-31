import board
import neopixel

Num_LED = 36
Num_Track = 3
Num_LED_Per_Track = 12
Np_brightness = 0.2
Col_width = 1.0
pixels = neopixel.NeoPixel(
    board.D18, Num_LED, auto_write=False, brightness=Np_brightness, pixel_order=neopixel.GRB
)
pixels.fill((0, 0, 0))
pixels.show()

## Store hue and brightness by LED
params = []
for i in range(0, Num_LED):
    params.append([0.5, 0.0])  # hue, brightness    

def show():
    for i in range(0, Num_LED):
        hue, brightness = params[i]
        set_led_color(i, brightness, hue)
    pixels.show()

def set_brightness(track_id, _brightness):
    led_first = track_id * Num_LED_Per_Track
    led_last = (track_id + 1) * Num_LED_Per_Track
    for i in range(led_first, led_last):
        if _brightness == 0:
            params[i][1] = 0.05
        elif _brightness == 1:
            params[i][1] = 1
       # params[i][1] = _brightness
    
        
def set_hue(led_id, _hue):
    params[led_id][0] = _hue

def set_led_color(led_id, brightness, hueval):
    user_id = led_id // Num_LED_Per_Track
    """
        What does the 3 below represent?
    """
    col_id = 0
    if user_id == 0:
        col_id = 0
    elif user_id == 1:
        col_id = 2
    elif user_id == 2:
        col_id = 1

    hue = 360 / Num_Track * (col_id + (hueval - 0.5) * Col_width)

    saturation = 255
    hue %= 360
    rgb_max = brightness
    rgb_min = rgb_max - (saturation / 255.0 * rgb_max)

    r, g, b = 0, 0, 0

    if 0 <= hue < 60:
        r = rgb_max
        g = (hue / 60) * (rgb_max - rgb_min) + rgb_min
        b = rgb_min
    elif 60 <= hue < 120:
        r = (120 - hue) / 60 * (rgb_max - rgb_min) + rgb_min
        g = rgb_max
        b = rgb_min
    elif 120 <= hue < 180:
        r = rgb_min
        g = rgb_max
        b = ((hue - 120) / 60) * (rgb_max - rgb_min) + rgb_min
    elif 180 <= hue < 240:
        r = rgb_min
        g = (240 - hue) / 60 * (rgb_max - rgb_min) + rgb_min
        b = rgb_max
    elif 240 <= hue < 300:
        r = ((hue - 240) / 60) * (rgb_max - rgb_min) + rgb_min
        g = rgb_min
        b = rgb_max
    elif 300 <= hue < 360:
        r = rgb_max 
        g = rgb_min
        b = (360 - hue) / 60 * (rgb_max - rgb_min) + rgb_min

    r *= 255.0
    g *= 255.0
    b *= 255.0
        
    pixels[led_id] = (int(r), int(g), int(b))
    # return (led_id, r,  g, b)


if __name__ == "__main__":
    # set_led_color(0, 1, 0.0)
    # set_led_color(1, 1, 0.2)
    # set_led_color(2, 1, 0.4)
    # set_led_color(3, 1, 0.6)
    # set_led_color(4, 1, 0.8)
    # set_led_color(5, 1, 1.0)

    # set_led_color(6, 1, 0.0)
    # set_led_color(7, 1, 0.2)
    # set_led_color(8, 1, 0.4)
    # set_led_color(9, 1, 0.6)
    # set_led_color(10, 1, 0.8)
    # set_led_color(11, 1, 1.0)

    # set_led_color(12, 1, 0.0)
    # set_led_color(13, 1, 0.2)
    # set_led_color(14, 1, 0.4)
    # set_led_color(15, 1, 0.6)
    # set_led_color(16, 1, 0.8)
    # set_led_color(17, 1, 1.0)

    # set_led_color(18, 1, 0.0)
    # set_led_color(19, 1, 0.2)
    # set_led_color(20, 1, 0.4)
    # set_led_color(21, 1, 0.6)
    # set_led_color(22, 1, 0.8)
    # set_led_color(23, 1, 1.0)

    for i in range(0, 6):
        for j in range(0, 6):
            set_led_color(i * 6 + j, 1, 0.2 * j)


    show()
