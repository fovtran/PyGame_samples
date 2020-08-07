import math
import sys

def open_obj(fil):
	_faces = []
	faces = {}
	verts = []
	with open('head_normalization/head1.obj', 'r+') as r:
		for line in r.readlines():

			if line[0]=='v':
				verts.append(line.strip('v ').replace('\n','').split(' '))

			if line[0]=='f':
				_faces.append(line.strip('f ').replace('\n','').split(' '))

	for _f in _faces:
		for x in _f:
			faces[x]= verts[int(x)-1]

	return faces, verts
