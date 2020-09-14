#----------------------------------------------------------
# File export_simple_obj.py
# Simple obj exporter which writes only verts, faces, and texture verts
#----------------------------------------------------------
import bpy, os

def export_simple_obj(filepath, ob, rot90, scale):
    name = os.path.basename(filepath)
    realpath = os.path.realpath(os.path.expanduser(filepath))
    fp = open(realpath, 'w')    
    print('Exporting %s' % realpath)

    if not ob or ob.type != 'MESH':
        raise NameError('Cannot export: active object %s is not a mesh.' % ob)
    me = ob.data

    for v in me.vertices:
        x = scale*v.co
        if rot90:
            fp.write("v %.5f %.5f %.5f\n" % (x[0], x[2], -x[1]))
        else:
            fp.write("v %.5f %.5f %.5f\n" % (x[0], x[1], x[2]))

    if len(me.uv_textures) > 0:
        uvtex = me.uv_textures[0]
        for f in me.faces:
            data = uvtex.data[f.index]
            fp.write("vt %.5f %.5f\n" % (data.uv1[0], data.uv1[1]))
            fp.write("vt %.5f %.5f\n" % (data.uv2[0], data.uv2[1]))
            fp.write("vt %.5f %.5f\n" % (data.uv3[0], data.uv3[1]))
            if len(f.vertices) == 4:
                fp.write("vt %.5f %.5f\n" % (data.uv4[0], data.uv4[1]))

        vt = 1
        for f in me.faces:
            vs = f.vertices
            fp.write("f %d/%d %d/%d %d/%d" % (vs[0]+1, vt, vs[1]+1, vt+1, vs[2]+1, vt+2))
            vt += 3
            if len(f.vertices) == 4:
                fp.write(" %d/%d\n" % (vs[3]+1, vt))
                vt += 1        
            else:
                fp.write("\n")
    else:
        for f in me.faces:
            vs = f.vertices
            fp.write("f %d %d %d" % (vs[0]+1, vs[1]+1, vs[2]+1))
            if len(f.vertices) == 4:
                fp.write(" %d\n" % (vs[3]+1))
            else:
                fp.write("\n")
    
    print('%s successfully exported' % realpath)
    fp.close()
    return
