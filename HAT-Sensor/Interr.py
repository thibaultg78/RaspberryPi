from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)
sleep(1)
sense.clear(0,0,0)
sleep(1)
sense.set_pixels(question_mark)
sleep(1)
sense.clear(0,0,0)
