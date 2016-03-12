from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)
sense.show_message("Hello World", text_colour=(0, 0, 0), back_colour=(0, 0, 255))

sense.clear(0,0,0)
