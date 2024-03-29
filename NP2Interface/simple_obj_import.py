#----------------------------------------------------------
# File import_simple_obj.py
# Simple obj importer which reads only verts, faces, and texture verts
#----------------------------------------------------------
import os

def import_simple_obj(filepath, rot90, scale):
    name = os.path.basename(filepath)
    realpath = os.path.realpath(os.path.expanduser(filepath))
    fp = open(realpath, 'rU')    # Universal read
    print('Importing %s' % realpath)

    verts = []
    faces = []
    texverts = []
    texfaces = []
    uvtex = {}

    for line in fp:
        words = line.split()
        if len(words) == 0:
            pass
        elif words[0] == 'v':
            (x,y,z) = (float(words[1]), float(words[2]), float(words[3]))
            if rot90:
                verts.append( (scale*x, -scale*z, scale*y) )
            else:
                verts.append( (scale*x, scale*y, scale*z) )
        elif words[0] == 'vt':
            texverts.append( (float(words[1]), float(words[2])) )
        elif words[0] == 'f':
            (f,tf) = parseFace(words)
            faces.append(f)
            if tf:
                texfaces.append(tf)
        else:
            pass
    print('%s successfully imported' % realpath)
    fp.close()

    if texverts:
        uvtex[name] = [None,None,None,None]
        for n in range(len(texfaces)):
            tf = texfaces[n]
            uvtex[name][0] = texverts[tf[0]]
            uvtex[name][1] = texverts[tf[1]]
            uvtex[name][2] = texverts[tf[2]]
            if len(tf) == 4:
                uvtex[3] = texverts[tf[3]]

    return verts, faces, texverts, texfaces, uvtex

def parseFace(words):
    face = []
    texface = []
    for n in range(1, len(words)):
        li = words[n].split('/')
        face.append( int(li[0])-1 )
        try:
            texface.append( int(li[1])-1 )
        except:
            pass
    return (face, texface)
