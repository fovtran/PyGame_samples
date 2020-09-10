# Meshing file formats 1

## Configurando Meshing file formats en Python 3.8


- Loader
  >>> pip install pywavefront wavefront_reader objloader moderngl.ext.obj objdem wvflib

- Imports
  >>> import meshtool
  >>> import bpy
  >>> import collada
  >>> import bmesh
  >>> import bge,bgl
  >>> import bpy_extras
  >>> import mathutils
  >>> import ode
  >>> import osim
  >>> import pybullet
  pybullet build time: Aug 17 2020 02:58:51
  >>> import pyopencl
  >>> import shapefile
  >>> import pyodesys
  >>> import wavefront_reader
  >>> import pywavefront
  >>> import objloader
  >>> import objdem
  >>> import moderngl.ext.obj

### Usando Python Collada para DAE
´´´Python
import collada
import numpy as np

reference_file = 'head3.dae'
mesh = collada.Collada(reference_file, ignore=[collada.DaeUnsupportedError, collada.DaeBrokenRefError])

mesh.scenes
# [<Scene id=myscene nodes=1>]

mesh.nodes
# []

mesh.geometries
# [<Geometry id=geometry0, 1 primitives>]

mesh.materials
# [<Material id=material0 effect=effect0>]

mesh.effects
# [<Effect id=effect0 type=phong>]

# triangle_list
[[prim for prim in g.primitives[t]] for t in range(len(g.primitives)) for g in mesh.geometries][0]
[[[prim for prim in g.primitives[t]] for t in range(len(g.primitives))] for g in mesh.geometries]

# primitive attributes
mesh.geometries[0].primitives[0].vertex
mesh.geometries[0].primitives[0].vertex_index
mesh.geometries[0].primitives[0].normal
mesh.geometries[0].primitives[0].normal_index

X = mesh.geometries[0].primitives[0].vertex
Y = mesh.geometries[1].primitives[0].vertex
´´´
#### Listo por ahora. 
