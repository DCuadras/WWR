import math
from datetime import datetime
from threading import current_thread
from turtle import width
current_date_time = datetime.now()
w = int(input('What is the width of the tire in millimeters? '))
a = int(input('What is the aspect ratio of the tire in millimeters? '))
d = int(input('What is the diameter of the tire in millimeters? '))
v_a = math.pi * (w * w) * a
v_b = w * a + 2540 * d
v_c = v_a * v_b / 10000000000
print(f'The approximate volume is: {v_c:.2f} liters')
print(f'{current_date_time:%Y-%m-%d}, {w}, {a}, {d}, {v_c:.2f}')
with open("Volumes.txt","a") as testtxt:
    testtxt.write(f"{current_date_time:%Y-%m-%d}, {w}, {a}, {d}, {v_c:.2f} \n")