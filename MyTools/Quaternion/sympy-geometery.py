from sympy import Ellipse, Point, Line, sqrt
e = Ellipse(Point(0, 0), 5, 7)

e.intersection(Ellipse(Point(1, 0), 4, 3))
e.intersection(Ellipse(Point(5, 0), 4, 3))
e.intersection(Ellipse(Point(100500, 0), 4, 3))
e.intersection(Ellipse(Point(0, 0), 3, 4))
e.intersection(Ellipse(Point(-1, 0), 3, 4))
