import numpy as np

q * Vector3(x, y, z)
# Vector3(x', y', z')

# You can think of quaternions (for our purposes) as a scalar plus a 3-d vector -- abstractly, w + xi + yj + zk, here represented by a simple tuple (w, x, y, z). The space of 3-d rotations is represented in full by a sub-space of the quaternions, the space of unit quaternions, so you want to make sure that your quaternions are normalized. You can do so in just the way you would normalize any 4-vector (i.e. magnitude should be close to 1; if it isn't, scale down the values by the magnitude):

def normalize(v, tolerance=0.00001):
mag2 = sum(n * n for n in v)
if abs(mag2 - 1.0) > tolerance:
    mag = sqrt(mag2)
    v = tuple(n / mag for n in v)
return v

# Please note that for simplicity, the following functions assume that quaternion values are already normalized. In practice, you'll need to renormalize them from time to time, but the best way to deal with that will depend on the problem domain. These functions provide just the very basics, for reference purposes only.
# Every rotation is represented by a unit quaternion, and concatenations of rotations correspond to multiplications of unit quaternions. The formula1 for this is as follows:

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

# To rotate a vector by a quaternion, you need the quaternion's conjugate too. That's easy:
def q_conjugate(q):
    w, x, y, z = q
    return (w, -x, -y, -z)

# Now quaternion-vector multiplication is as simple as converting a vector into a quaternion (by setting w = 0 and leaving x, y, and z the same) and then multiplying q * v * q_conjugate(q):
def qv_mult(q1, v1):
    q2 = (0.0,) + v1
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[1:]

# Finally, you need to know how to convert from axis-angle rotations to quaternions. Also easy! It makes sense to "sanitize" input and output here by calling normalize.
def axisangle_to_q(v, theta):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = cos(theta)
    x = x * sin(theta)
    y = y * sin(theta)
    z = z * sin(theta)
    return w, x, y, z

# And back:
def q_to_axisangle(q):
    w, v = q[0], q[1:]
    theta = acos(w) * 2.0
    return normalize(v), theta

# Here's a quick usage example. A sequence of 90-degree rotations about the x, y, and z axes will return a vector on the y axis to its original position. This code performs those rotations:
x_axis_unit = (1, 0, 0)
y_axis_unit = (0, 1, 0)
z_axis_unit = (0, 0, 1)
r1 = axisangle_to_q(x_axis_unit, numpy.pi / 2)
r2 = axisangle_to_q(y_axis_unit, numpy.pi / 2)
r3 = axisangle_to_q(z_axis_unit, numpy.pi / 2)

v = qv_mult(r1, y_axis_unit)
v = qv_mult(r2, v)
v = qv_mult(r3, v)

print v
# output: (0.0, 1.0, 2.220446049250313e-16)

# Keep in mind that this sequence of rotations won't return all vectors to the same position;
# for example, for a vector on the x axis, it will correspond to a 90 degree rotation about the y axis. 
# (Keep the right-hand-rule in mind here; 
# a positive rotation about the y axis pushes a vector on the x axis into the negative z region.)

v = qv_mult(r1, x_axis_unit)
v = qv_mult(r2, v)
v = qv_mult(r3, v)

print v
# output: (4.930380657631324e-32, 2.220446049250313e-16, -1.0)

# As always, please let me know if you find any problems here.

# 1. The quaternion multiplication formula looks like a crazy rat's nest, 
# but the derivation is simple (if tedious). 
# Just note first that 
# ii = jj = kk = -1; then that ij = k, jk = i, ki = j; 
# and finally that ji = -k, kj = -i, ik = -j. 
# Then multiply the two quaternions, distributing out the terms and rearranging them 
# based on the results of each of the 16 multiplications. 
# This also helps to illustrate why you can use quaternions to represent rotation; 
# the last six identities follow the right-hand rule, 
# creating bijections between rotations 
# from i to j and rotations around k, and so on.
