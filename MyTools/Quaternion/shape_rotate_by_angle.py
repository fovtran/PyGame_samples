import numpy as np
from numpy import cos, sin, linspace, concatenate
import matplotlib.pyplot as plt


def rotate(x, y, alpha):
    """
    Rotate the shape by an angle alpha (given in degrees)
    """
    # Get the center of the shape
    x_center = (x.max() + x.min()) / 2.0
    y_center = (y.max() + y.min()) / 2.0

    # Shifting the center of the shape to the origin of coordinates
    x0 = x - x_center
    y0 = y - y_center
    angle_rad = np.deg2rad(alpha)
    rot_mat = np.array([
    [cos(angle_rad), -sin(angle_rad)],
    [sin(angle_rad), cos(angle_rad)]
    ])
    xy = np.vstack((x0, y0))
    xnew, ynew = rot_mat @ xy

    # translate it back to its original location
    xnew += x_center
    ynew += y_center

    return xnew, ynew

z0, z1, z2, z3 = 4 + 0.6*1j, 4 + 0.8*1j, 8 + 0.8*1j, 8 + 0.6*1j
xy = concatenate((
                linspace(z0, z1, 10, endpoint=False),
                linspace(z1, z2, 10, endpoint=False),
                linspace(z2, z3, 10, endpoint=False),
                linspace(z3, z0, 10, endpoint=True)
          ))

x = xy.real
y = xy.imag

xrot, yrot = rotate(x, y, alpha=-45.0)

# The x and y limits
xlow, xup = 0, 10
ylow, yup = -1.5, 3.0


plt.gca().set_aspect('equal')
plt.plot(x, y, label='original shape')
plt.plot(xrot, yrot, label='rotated shape')
plt.xlim((xlow, xup))
plt.ylim((ylow, yup))
plt.legend()
plt.show()
