#!env python.exe
# -*- coding: utf-8 -*-
__doc__ = """
make_lamp.py
Rev 1.0

This script generates a lamp from cdrom/harddrive plates

This script is executed at the command line by:
>blender -P make_lamp.py
"""
__author__ = "dmc"
__version__ = "1.0 2013/07/16"
__url__="Website, sphericsf.herokuapp.com"

import bpy
import math

pi = 3.141592653589793

t="hdd"
cyl_dia = 10
hole = 3

if type=="hdd":
    cyl_dia = 9.5
    hole = 3
if type=="cdrom":
    cyl_dia = 12
    hole = 1.5

cyl_h = 0.1

rad_from_dia = lambda dia: dia/2
rad_from_degree = lambda deg: (deg*pi)/180


def make_cdrom():
    rad = rad_from_dia(cyl_dia);
    bpy.ops.mesh.primitive_cylinder_add(radius = rad, depth = cyl_h,  location=(0, 0, 0.2), rotation=(0,0,0))
    cdrom = bpy.data.objects['Cylinder']
    cdrom.name = "cdrom"
    return cdrom

def paint_color(obj):
    obj_material = bpy.data.materials.new('Object Material')
    obj_material.diffuse_color = 0.375, 0.75, 0.0
    mesh = obj.data
    mesh.materials.append(obj_material)
    return {"FINISHED"}

def difference( target, inner ):
    sce = bpy.context.scene
    obja = sce.objects.active = target
    mod = obja.modifiers.new('hole', 'BOOLEAN')
    # Apply modifier
    mod.object = hole
    mod.operation= 'DIFFERENCE'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='hole')
    sce.objects.unlink(hole)
    return {"FINISHED"}

def make_hole(h):
    hole = rad_from_dia(h)
    bpy.ops.mesh.primitive_cylinder_add(radius = hole, depth = cyl_h, location=(0,0,0.2))
    hole = bpy.data.objects['Cylinder']
    hole.name = "hole"
    bpy.ops.object.select_all(action='DESELECT')
    return hole

def make_plane():
    long = rad_from_degree(90)
    lat = rad_from_degree(90)
    bpy.ops.mesh.primitive_plane_add(location=(0,0,0), rotation=(long,0,lat))
    long = rad_from_degree(90)
    lat = rad_from_degree(180)
    bpy.ops.mesh.primitive_plane_add(location=(0,0,0), rotation=(long,0,lat))

cdrom = make_cdrom()
paint_color(cdrom)
hole = make_hole(hole)
difference( cdrom, hole )
make_plane()
