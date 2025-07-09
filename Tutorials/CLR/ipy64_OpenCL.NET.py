# http://code.enthoplatught.com/.iron/eggs/index.html>>>
import sys
#sys.path.append("D:/binr/ironpython 2.7/lib/site-packages")
import clr
#clr.AddReference("./.NuGet/packages/OpenCL.Net.2.2.9.0/lib/net40/OpenCL.Net.dll")
clr.AddReferenceToFileAndPath("./.NuGet/packages/OpenCL.Net.2.2.9.0/lib/net40/OpenCL.Net.dll")
import OpenCL.Net as cl

def Vprint(a):
	a.reverse()
	for c in a:
		if not c.startswith("__"):
			print c
#print dir(cl)
#print dir(cl.DeviceType))
print dir(cl.Platform().__class__)
#print dir(cl.Device)
#Vprint(dir(cl.Cl))
dev = cl.Device()
plat = cl.Platform()
platform = cl.Cl.GetPlatformIDs()
print cl.Cl.GetDeviceIDs(plat, cl.DeviceType.Default)

#plat = cl.DeviceType.GetNames()
print dir(plat)

my_gpu_devices = plat.get_devices(device_type=cl.DeviceType.Cpu)
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
