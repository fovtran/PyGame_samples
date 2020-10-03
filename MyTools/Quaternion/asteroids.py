import bpy
from mathutils import Vector
from numpy import pi,sin,cos,tan,tanh,linspace,random,vectorize
import random

pi2 = pi * 2

def create_Vertices (name, verts, faces):
    #me = bpy.data.meshes.new(name+'Mesh')
    #ob = bpy.data.objects.new(name, me)
    #ob.show_name = False
    #bpy.context.scene.objects.link(ob)
    #me.from_pydata(verts, [], faces)
    #me.update(calc_edges=True, calc_tessface=False)
    #return ob
	pass

def gen_vert(origin):
    r = 1.5
    r1 = 0.05
    v1 = []
    rad = pi2
    for j in linspace(0, rad, 13):
        x,y = (r * sin(j), r * cos(j))
        v1.append( (x,y,1) )

        for i in linspace(0,rad,7):
            r1 = 0.1
            x1, y1 = (x + r1 * sin(i), y + r1 * cos(i))
            v1.append( (x1,y1,1) )

            for t in range(1,4):
                x2, y2 = ( x1 + r1 * sin(i), y1 + r1 * cos(i))
                v1.append( (x2,y2,1) )
                #bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(x2,y2,1+random.random()/5), rotation=(random.random(), random.random(), 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
                #bpy.ops.transform.resize(value=(random.random()/50,random.random()/50,random.random()/50), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)

                #bpy.ops.mesh.rocks(preset_values='0', num_of_rocks=1, scale_X=(t/50, t/50), skew_X=0, scale_Y=(t/50, t/50), skew_Y=0, scale_Z=(1, 1), skew_Z=0, use_scale_dis=False, scale_fac=(1, 1, 1), deform=5, rough=2.5, detail=3, display_detail=2, smooth_fac=0, smooth_it=0, mat_enable=True, mat_color=(random.random()+.2,random.random()+.2,random.random()+.2), mat_bright=0.85, mat_rough=1, mat_spec=0.2, mat_hard=50, mat_use_trans=True, mat_alpha=0, mat_cloudy=0, mat_IOR=1, mat_mossy=0, use_generate=True, use_random_seed=True, user_seed=1)


                r1 += t/10
    return v1

origo = (0,0,0)
origin = Vector(origo)
verts = gen_vert(origin)
faces = ()
create_Vertices("cosa", verts, faces)
print(verts)
print(faces)
