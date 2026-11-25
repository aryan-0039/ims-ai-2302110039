!pip install cadquery
import math
from cadquery import func as cf

def clutch_brick(length, width, height, stud_d, stud_h, spacing):
    brick = cf.box(length, width, height)
    stud = cf.cylinder(d=stud_d, h=stud_h)

    for i in range(8):
        row, col = divmod(i, 4)

        x = (col - 1.5) * spacing
        y = (row - 0.5) * spacing

        stud_position = stud.moved(x=x, y=y, z=height)
        brick = brick + stud_position

    return brick

brick = clutch_brick(31.2, 15.2, 9.6, 4.8, 1.7, 8.0)

expected = 31.2 * 15.2 * 9.6 + 8 * math.pi * (4.8 / 2) ** 2 * 1.7

assert abs(brick.Volume() - expected) < 0.5

brick.exportStl("brick.stl")

print("2 × 4 brick created successfully!")
print("Volume:", brick.Volume())

expected = (
    31.2 * 15.2 * 9.6
    + 8 * math.pi * (4.8 / 2) ** 2 * 1.7
)

print("Expected Volume:", expected)

assert brick.isValid()

assert abs(brick.Volume() - expected) < 0.5

print("Volume check passed!")
print("Actual Volume:", brick.Volume())
print("Expected Volume:", expected)
print("Number of studs: 8")

from google.colab import files

files.download("brick.stl")
