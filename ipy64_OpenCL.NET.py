import clr
clr.AddReference("DotNetOpenCL")
#clr.AddReference("mtrand")

import sys
# http://code.enthought.com/.iron/eggs/index.html>>>
#sys.path.append("D:/binr/ironpython 2.7/lib")
#sys.path.append("D:/binr/ironpython 2.7/lib/site-packages")
#clr.AddReference("NumpyDotNet")
#import numpy as np
#import scipy as sc


import DotNetOpenCL as cl

all_platforms = cl.clGetPlatformIDs()
print(all_platforms)
my_gpu_devices = platform.get_devices(device_type=cl.device_type.CPU)
context = cl.Context(devices=my_gpu_devices)

class NaiveTranspose:
    def __init__(self, ctx):
        self.kernel = cl.Program(ctx, """
        __kernel
        void transpose(
          __global float *a_t, __global float *a,
          unsigned a_width, unsigned a_height)
        {
          int read_idx = get_global_id(0) + get_global_id(1) * a_width;
          int write_idx = get_global_id(1) + get_global_id(0) * a_height;

          a_t[write_idx] = a[read_idx];
        }
        """).build().transpose


X = NaiveTranspose()
print(x)
