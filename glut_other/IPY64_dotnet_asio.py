import clr
clr.AddReference("DotNetOpenASIO")

from DotNetOpenASIO import ASIO
from System import Array, IntPtr

ret = ASIO.CreateOpenAsio()