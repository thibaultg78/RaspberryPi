from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)

X = [0, 255, 0]  # Green
O = [0, 0, 0]  # White

question_mark = [
X, X, X, O, X, O, O, X,
X, O, X, O, X, O, X, O,
X, O, X, O, X, X, O, O,
X, O, X, O, X, X, O, O,
X, O, X, O, X, X, O, O,
X, O, X, O, X, O, X, O,
X, X, X, O, X, O, O, X,
O, O, O, O, O, O, O, O
]

sense.set_pixels(question_mark)
sleep(1)
sense.clear(0,0,0)
sleep(1)
sense.set_pixels(question_mark)
sleep(1)
sense.clear(0,0,0)
sleep(1)
sense.set_pixels(question_mark)
sleep(1)
sense.clear(0,0,0)
