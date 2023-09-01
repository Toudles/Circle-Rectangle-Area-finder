"""
Assignment #11, Part 1
Andrew Park
"""

import math
class rectangle():
    def __init__(self, w, l, x, y):
        self.x=x
        self.y=y
        self.w=w
        self.l=l

    def get_area(self):
        self.area=self.w * self.l
        return self.area

    def get_perimeter(self):
        self.perimeter=(2 * self.w) + (2 * self.l)
        return self.perimeter

rectangle1 = rectangle(10,15,5,3)
rectangle2 = rectangle(3,5,15,7)
print("Rectangle #1 \n* Coordinates: (",rectangle1.x,",",rectangle1.y,")", "\n* Area:",round(rectangle1.get_area(),2),"\n* Perimeter:",round(rectangle1.get_perimeter(),2))
print("Rectangle #2 \n* Coordinates: (",rectangle2.x,",",rectangle2.y,")", "\n* Area:",round(rectangle2.get_area(),2),"\n* Perimeter:",round(rectangle2.get_perimeter(),2))
