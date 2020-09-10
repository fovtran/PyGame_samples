
from ctypes import *
import numpy as np

polylib = cdll.LoadLibrary("libpolylib64.dll")

class Matrix(Structure):
    _fields_ = [
        ("NbRows", c_uint32),
        ("NbColumns", c_uint32),
        ("p", POINTER(POINTER(c_int64))),
        ("p_Init", POINTER(c_int64)),
        ("p_Init_size", c_int32)
    ]

def smith_normal_form(A):
    pM0 = polylib.Matrix_Alloc(3, 3)
    M0 = Matrix.from_address(pM0);
    pM = pointer(M0)
    pU = POINTER(Matrix)()
    pV = POINTER(Matrix)()
    pP = POINTER(Matrix)()
    M = np.ctypeslib.as_array(M0.p_Init, shape=(3,3))
    M[:] = A
    polylib.Smith.argtypes=[POINTER(Matrix), POINTER(POINTER(Matrix)), POINTER(POINTER(Matrix)), POINTER(POINTER(Matrix))]
    polylib.Smith(pM, pointer(pU), pointer(pV), pointer(pP))
    U = np.ctypeslib.as_array(pU.contents.p_Init, shape=(3,3))
    V = np.ctypeslib.as_array(pV.contents.p_Init, shape=(3,3))
    P = np.ctypeslib.as_array(pP.contents.p_Init, shape=(3,3))

    return U, P, V
