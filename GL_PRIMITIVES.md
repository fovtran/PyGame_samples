GL_POINTS, GL_LINE_STRIP, GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY,
GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY and GL_PATCHES

CalculateDist — wiki
Get the distance between two (x,y) format locations using the Pythagorean theorem

In a right triangle, (x1-x2) being the horizontal distance between the two points (The change in x) and (y1-y2) being the vertical distance between the two points (The change in y),

(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) == distance*distance. So the distance is the square root of (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2).

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2))
You can also used the math function hypot:

dist = math.hypot(x1-x2, y1-y2)
