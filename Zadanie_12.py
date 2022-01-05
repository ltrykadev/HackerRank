from collections import namedtuple

point = namedtuple('point','x,y')
pt1 = point(1,2)
pt2 = point(3,4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot_product)