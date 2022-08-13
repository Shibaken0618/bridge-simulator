from geom2d.point import Point
from geom2d.polygon import Polygon

# create polygon by inputting x,y coordinates in a 2d plane
def make_polygon_from_coords(coords: [float]):
    if len(coords) % 2 != 0:
        raise ValueError('Need an even number of coordinates')
    indices = range(0, len(coords), 2)
    return Polygon(
        [Point(coords[i], coords[i+1]) for i in indices]
    )