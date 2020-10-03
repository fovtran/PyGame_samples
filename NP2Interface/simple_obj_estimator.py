import numpy as np
from NP2Interface.simple_obj_import import *

verts, faces, texverts, texfaces, uvtex = import_simple_obj('media/column2/column2.obj', 0, 1)

print("Vert count: {}".format(int(len(verts)/3)))
print("Face count: {}".format(len(faces)))

vv = [None, None, None, None]
for f in faces:
    vv[0] = verts[f[0]]
    vv[1] = verts[f[1]]
    vv[2] = verts[f[2]]
    vv[3] = verts[f[3]]
    print(vv)
