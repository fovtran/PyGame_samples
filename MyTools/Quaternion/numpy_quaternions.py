import numpy as np

q = [0, 1, 0, 0] # 180 degree rotation around axis 0
M = quat2mat(q) # from this module
vec = np.array([1, 2, 3]).reshape((3,1)) # column vector
tvec = np.dot(M, vec)

q = angle_axis2quat(np.pi, [1, 0, 0])
np.allclose(q, [0, 1, 0,  0])
# True

import numpy as np
wxyz = fillpositive([0,0,0])
np.all(wxyz == [1, 0, 0, 0])
# True
wxyz = fillpositive([1,0,0]) # Corner case; w is 0
np.all(wxyz == [0, 1, 0, 0])
# True
np.dot(wxyz, wxyz)
# 1.0

import numpy as np
q = mat2quat(np.eye(3)) # Identity rotation
np.allclose(q, [1, 0, 0, 0])
# True
q = mat2quat(np.diag([1, -1, -1]))
np.allclose(q, [0, 1, 0, 0]) # 180 degree rotn around axis 0
# True

q1 = [1, 0, 0, 0]
nearly_equivalent(q1, [0, 1, 0, 0])
# False
nearly_equivalent(q1, [1, 0, 0, 0])
# True
nearly_equivalent(q1, [-1, 0, 0, 0])
# True

theta, vec = quat2angle_axis([0, 1, 0, 0])
np.allclose(theta, np.pi)
# True
vec
# array([ 1.,  0.,  0.])

quat2angle_axis([1, 0, 0, 0])
# (0.0, array([ 1.,  0.,  0.]))

import numpy as np
M = quat2mat([1, 0, 0, 0]) # Identity quaternion
np.allclose(M, np.eye(3))
# True
M = quat2mat([0, 1, 0, 0]) # 180 degree rotn around axis 0
np.allclose(M, np.diag([1, -1, -1]))
# True
