import math as m
import cmath as c
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np

def Cos(a): return cos(radians(a))
def Sin(a): return sin(radians(a))
def Tan(a): return tan(radians(a))
def ArcTan(a):  return degrees(arctan(a))
def ArcSin(a):  return degrees(arcsin(a))
def ArcCos(a):  return degrees(arccos(a))

point = lambda x,y: tuple((x, y))
mid = lambda x,x1: (x-x1)/2  # x - x'
midpoint = lambda __a,__b: ( (__b[0] - __a[0])/2, (__b[1] - __a[1])/2 )
def midpoint(A,B):
    AMB = ( ( (A[0]+B[0])/2 ), (A[1]+B[1])/2 )
    return AMB

def radius(x,y):
    r = mth.sqrt(x**2+y**2)
    return r

def max_rad(x, y):
    return max(x) - min(x), max(y) - min(y)

def distance(A,B):
    d = mth.sqrt( (B[0] - A[0])**2 + (B[1] - A[1])**2 )
    return d

def semiperimeter(a,b,c):
    # Semiperimeter of triangle
    s = (a+b+c) / 2
    return s

def area(a,b,c):
    # Area of triangle
    A = np.sqrt(s* (s-a) * (s-b) * (s-c), dtype=np.float64)
    return A

def length(u):
    """Calculates the length of u."""
    return math.sqrt(numpy.dot(u, u), dtype=np.float64)

def normalize(u):
    """Returns the normalized vector along u."""
    return u/math.sqrt(numpy.dot(u, u), dtype=np.float64)

def cross(u, v):
    """Cross product of u and v:
    Cross[u,v] = {-u3 v2 + u2 v3, u3 v1 - u1 v3, -u2 v1 + u1 v2}
    """
    return numpy.array([ u[1]*v[2] - u[2]*v[1],
                         u[2]*v[0] - u[0]*v[2],
                         u[0]*v[1] - u[1]*v[0] ], dtype=np.float64)

decomp = lambda _P,order: [_P[n][order] for n in range(len(_P))] # ejes i
decomp2d = lambda p, order: decomp(p,order)
conjugate2d = lambda P: [decomp2d(P,0), decomp2d(P,1)]  # ejes XY
conjugate3d = lambda P: [decomp2d(P,0), decomp2d(P,1), decomp2d(P,3)] #ejes XY
inverse = lambda P: [x for x in zip(decomp2d(A,0), decomp2d(A,1))] # lista de ejes a point

def phase(z): # Calculates the phase of a complex number
	r = numpy.absolute(z)
	return (z.real/r + 1j * z.imag/r)

def P2R(radii, angles):
	return radii * exp(1j*angles)

def R2P(x):
	return abs(x), angle(x)

def P2R(A, phi):
	return A * ( np.cos(phi) + np.sin(phi)*1j )

DegToRad = lambda deg: deg* np.pi/180    # degrees to radian
RadToDeg = lambda rad: rad* 180/np.pi    # radians to degrees
DegToPi = lambda deg: np.pi*deg / 180    # degrees to pi (more complex)
PiToDeg = lambda _pi: np.pi*_pi  * 1/180 # interesting complexity

# Trigonometric Unit tests
np.sin(-np.pi) == -1.22464679915e-16
np.sin(np.pi) == 1.22464679915e-16
np.sin(2*np.pi) == -2.4492935982947064e-16

np.cos(-np.pi) == -1.0
np.cos(0*np.pi) == 1.0
np.cos(1/2*np.pi) == 6.123233995736766e-17
np.cos(np.pi) == -1.0
np.cos(2/3*np.pi) == -1.8369701987210297e-16
np.cos(2*np.pi) == 1.0

np.radians(-360) == -6.2831853071795862
np.radians(-270) == -4.7123889803846897
np.radians(-180) == -3.1415926535897931
np.radians(-90)  == -1.5707963267948966
np.radians(0)    == 0.0   # zero pi radian
np.radians(90)   == 1.5707963267948966  # pi/2 radian
np.radians(180)  == 3.1415926535897931  # pi radian
np.radians(270)  == 4.7123889803846897
np.radians(360)  == 6.2831853071795862

np.degrees(0*np.pi)   == 0
np.degrees(1/2*np.pi) == 90
np.degrees(np.pi)     == 180.0
np.degrees(3/2*np.pi) == 270.0
np.degrees(2*np.pi)   == 360.0

np.cos(np.radians(0)) == 1.0
np.cos(np.radians(90)) == 6.123233995736766e-17
np.cos(np.radians(180)) == -1.0
np.cos(np.radians(270)) == -1.8369701987210297e-16
np.cos(np.radians(360)) == 1.0

X = complex(0, 0j)
Y = complex(0, 1j)
Z = complex(0, 2j)
W = complex(-1, 3j)
S = [X,Y,Z, W]

# Vec2
a = point(0,0)
b = point(10,10)
A = [None, None]
A[0] = a
A[1] = b

#Vec2 w/midpoint
a = point(0,0)
b = point(10,10)
A = [None, None, None]
A[0] = a
A[1] = midpoint(a,b)
A[2] = b

# Proof pythagorean theorem

# a/np.sin(angle_A) == b/np.sin(angle_B) == c/np.sin(angle_C)  # sines law
# Note: angle A is opposite side a, B is opposite b, and C is opposite c
# c**2 == a**2 + b**2 - 2*a*b * np.cos(C)  # cosines law. where C is the opposite angle

# Right triangle angles
# example angles
A = 13   # a = 180 - c - b # existiendo c, b
B = 90   # b = 180 - a - c # existiendo a, c
C = 180 - b - a # opposite angle, existiendo a, b
A**2+B**2==C**2 == True

#sides equation
alpha_rad = np.arccos( (B**2 + C**2 - A**2) / (2*B*C), dtype=np.float64)  # calcular angula A from B and C
beta_rad = np.arccos( (A**2 + C**2 - B**2) / (2*A*C), dtype=np.float64)   # calcular angula B from A and C
gamma_rad = np.arccos( (A**2 + B**2 - C**2) / (2*A*B), dtype=np.float64)  # calcular gamma = np.pi - alpha - beta

# Verificacion
alpha_rad*180/np.pi + beta_rad*180/np.pi + gamma_rad*180/np.pi  # similar a 180 grados
alpha_rad + beta_rad + gamma_rad == np.pi  # deberia dar la suma de angulos osea 1 pi
A_degrees = C * np.sin(alpha_rad) / np.sin(gamma_rad)  # angulo a inverso en grados
B_degrees = C * np.sin(beta_rad) / np.sin(gamma_rad)   # angulo b inverso en grados
C_degrees = A * np.sin(gamma_rad) / np.sin(alpha_rad)  # angulo c inverso en grados

# Proof 1 of pythagorean postulate
a == A_degrees, b == B_degrees, c == C_degrees  # (True, True, True) (degrees cmp)

# Angle functions in degrees
# angles from opposite angles
angle_a = lambda _b, _c: 180 - _c - _b
angle_b = lambda _a,_c: 180 - _a - _c
angle_c = lambda _a,_b: 180 - _a - _b
# degrees from segment + opposite angles
angle_a_deg = lambda _C, _alpha_rad, _gamma_rad: _C * np.sin(_alpha_rad) / np.sin(_gamma_rad)
angle_b_deg = lambda _C, _beta_rad, _gamma_rad: _C * np.sin(_beta_rad) / np.sin(_gamma_rad)
angle_c_deg = lambda _A, _alpha_rad, _gamma_rad: _A * np.sin(_gamma_rad) / np.sin(_alpha_rad)
# radian from angles ABC
angle_alpha_rad = lambda _A,_B,_C: np.arccos( (_B**2 + _C**2 - _A**2) / (2*_B*_C), dtype=np.float64)  # calcular angula A from B and C
angle_beta_rad = lambda _A,_B,_C: np.arccos( (_A**2 + _C**2 - _B**2) / (2*_A*_C), dtype=np.float64)   # calcular angula B from A and C
angle_gamma_rad = lambda _A,_B,_C: np.arccos( (_A**2 + _B**2 - _C**2) / (2*_A*_B), dtype=np.float64)  # calcular gamma = np.pi - alpha - beta

# from sides
x = 5
y = 5
hypot = m.hypot(x,y)  # ISO C
bbeta = np.arcsin(hypot/inv_adj)
bbeta = np.arccos(alpha/inv_adj) # ??
adj = np.sin(delta)*np.hypot(x,y) #where delta is the opposite of alpha

angle = np.arctan2(x,y)  # ISO C
para a =x, b=y, alpha=A
c = np.sqrt(a**2+b**2 - 2*a*b*np.cos(alpha)) #hypotenuse length


C = np.sqrt(a**2+b**2)

rho = np.cos(alpha)
phi = np.sin(alpha)
rho**2 + phi**2 == True


# Proof 2 of pythagorean postulate
np.cos(np.radians(60))**2 + np.sin(np.radians(60))**2 == True

# spheric coords
rho = 1    # angle
phi = 1    # elevation
theta = 1  # azimuth

rho  # valor referente a X
phi # valor referente a Y
polar_angle = theta

#rectangular coords
center_x = x0
center_y = y0
distance = x1  # cos(rho)
elevation = y1 # sin(rho)





# Z=X+iY
z = complex(rho,phi) #rho is the real component and phi the imaginary.
Z == z.real + z.imag*1j

c.phase(complex(-1.0,0.0))   == 3.141592653589793
c.phase(complex(-1.0,-0.0))  == -3.141592653589793

c.polar(complex(-1.0, 0.0))  == (1.0, 3.141592653589793)
c.polar(complex(-1.0, -0.0)) == (1.0, -3.141592653589793)
c.polar(complex(1.0, -0.0))  == (1.0, -0.0)
c.polar(complex(1.0, 0.0))   == (1.0, 0.0)

c.rect(1.0, -3.141592653589793) == (-1-1.2246467991473532e-16j) # ???