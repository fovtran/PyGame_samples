import math
import sys

def open_obj(fil):
	_faces = []
	groups = []
	faces = {}
	verts = []
	vertstex = []
	normals = []

	newgroup = False
	with open(fil, 'r+') as r:
		for line in r.readlines():
			if line[0]=='v':
				verts.append(line.strip('v ').replace('\n','').split(' '))

			if line[0]=='g':
				groups.append(line.strip('g ').replace('\n',''))
				newgroup=True

			if line[0]=='f':
				_faces.append(line.strip('f ').replace('\n','').split(' '))

	for _f in _faces:
		for x in _f:
			faces[x]= verts[int(x)-1]

	return faces, verts, normals

faces, verts = open_obj('media/ggg.obj')
for i,v in enumerate(verts): print("{} -> {}".format(i,v))
for i,f in enumerate(faces): print("{} -> {}".format(i,f))
