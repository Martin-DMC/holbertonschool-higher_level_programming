#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

print("------------------")
circle = Circle(radius=-6)
rectangle = Rectangle(width=0, height=7)

shape_info(circle)
shape_info(rectangle)
print("------------------")
circle = Circle(radius=0)
rectangle = Rectangle(width=5, height=0)

shape_info(circle)
shape_info(rectangle)