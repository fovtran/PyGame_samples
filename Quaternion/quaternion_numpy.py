import numpy as np
import quaternion

#i2 = j2 = k2 = ijk = -1

quaternion(1, 0, 0, 0)

q1 = np.quaternion(1,2,3,4)
q2 = np.quaternion(5,6,7,8)
q1 * q2
quaternion(-60, 12, 30, 24)
a = np.array([q1, q2])
a
array([quaternion(1, 2, 3, 4), quaternion(5, 6, 7, 8)],dtype=quaternion)
exp(a)
array([quaternion(1.69392, -0.78956, -1.18434, -1.57912),
        quaternion(138.909, -25.6861, -29.9671, -34.2481)], dtype=quaternion)

# The following ufuncs are implemented:
# add, subtract, multiply, divide, log, exp, power, negative, conjugate,
# copysign, equal, not_equal, less, less_equal, isnan, isinf, isfinite,
# absolute

# Quaternion components are stored as doubles. The package could be extended
# to support e.g. qfloat, qdouble, qlongdouble
