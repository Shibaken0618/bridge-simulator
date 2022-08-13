import math
from geom2d.vector import Vector
from geom2d import nums

#######################################
# class to create a point in a 2d plane
#######################################
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # function to find distance between 2 points
    def distance_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x**2 + delta_y**2)

    # override "+" to add x and y coordinate of points separately
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    # override "-" just like "+"
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    # using vector class, displace a point in the x and y direction
    def displaced(self, vector: Vector, times=1):
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

    # override "=" so that a point with the same x and y coordinates would be defined as the same
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Point):
            return False
        return nums.are_close_enough(self.x, other.x) and \
            nums.are_close_enough(self.y, other.y)

    # return the x and y coordinates of the string when invoked
    def __str__(self):
        return f'({self.x}, {self.y})'

    # format the point x and y coordinates to desired decimal
    def to_formatted_str(self, decimals: int):
        x = round(self.x, decimals)
        y = round(self.y, decimals)