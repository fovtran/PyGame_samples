#Allows the laminate to get exported as a DAE.
def toDAE(self):
    """
    Exports the current lamiante to a DAE file format
    """
    import collada
    mesh = collada.Collada()
    layerdef = self.layerdef
    nodes = [] # Each node of the mesh scene. Typically one per layer.
    for layer in layerdef.layers:
        layer_thickness = layer.thickness
        shapes = self.geoms[layer]
        zvalue = layerdef.z_values[layer]
        height = float(zvalue) #* 100 #*
        if (len(shapes) == 0) : #In case there are no shapes.
            continue
        for s in shapes:
            geom = self.createDAEFromShape(s, height, mesh, layer_thickness)
            mesh.geometries.append(geom)
            effect = collada.material.Effect("effect", [], "phone", diffuse=(1,0,0), specular=(0,1,0))
            mat = collada.material.Material("material", "mymaterial" + str(s.id), effect)
            matnode = collada.scene.MaterialNode("materialref" + str(s.id), mat, inputs=[])
            mesh.effects.append(effect)
            mesh.materials.append(mat)
            geomnode = collada.scene.GeometryNode(geom, [matnode])
            node = collada.scene.Node("node" + str(s.id), children=[geomnode])
            nodes.append(node)
    myscene = collada.scene.Scene("myscene", nodes)
    mesh.scenes.append(myscene)
    mesh.scene = myscene
    filename = popupcad.exportdir + os.path.sep +  str(self.id) + '.dae' #
    mesh.write(filename)


def createDAEFromShape(self, s, layer_num, mesh, thickness): #TODO Move this method into the shape class.
    import collada
    vertices = s.extrudeVertices(thickness, z0=layer_num)

    #This scales the verticies properly. So that they are in millimeters.
    vert_floats = [float(x)/(popupcad.SI_length_scaling) for x in vertices]
    vert_src_name = str(self.id) + '|' + str(s.id) + "-array"
    vert_src = collada.source.FloatSource(vert_src_name, numpy.array(vert_floats), ('X', 'Y', 'Z'))
    geom = collada.geometry.Geometry(mesh, "geometry-" + str(s.id), str(self.id), [vert_src])
    input_list = collada.source.InputList()
    input_list.addInput(0, 'VERTEX', "#" + vert_src_name)
    indices = numpy.array(range(0,(len(vertices) // 3)));
    triset = geom.createTriangleSet(indices, input_list, "materialref" + str(s.id))
    triset.generateNormals()
    geom.primitives.append(triset)
    return geom
    
#Allows the laminate to get exported as a DAE.
def toDAE(self):
    """
    Exports the current lamiante to a DAE file format
    """
    import collada
    mesh = collada.Collada()
    layerdef = self.layerdef
    nodes = [] # Each node of the mesh scene. Typically one per layer.
    for layer in layerdef.layers:
        layer_thickness = layer.thickness
        shapes = self.geoms[layer]
        zvalue = layerdef.z_values[layer]
        height = float(zvalue) #* 100 #*
        if (len(shapes) == 0) : #In case there are no shapes.
            continue
        for s in shapes:
            geom = self.createDAEFromShape(s, height, mesh, layer_thickness)
            mesh.geometries.append(geom)
            effect = collada.material.Effect("effect", [], "phone", diffuse=(1,0,0), specular=(0,1,0))
            mat = collada.material.Material("material", "mymaterial" + str(s.id), effect)
            matnode = collada.scene.MaterialNode("materialref" + str(s.id), mat, inputs=[])
            mesh.effects.append(effect)
            mesh.materials.append(mat)
            geomnode = collada.scene.GeometryNode(geom, [matnode])
            node = collada.scene.Node("node" + str(s.id), children=[geomnode])
            nodes.append(node)
    myscene = collada.scene.Scene("myscene", nodes)
    mesh.scenes.append(myscene)
    mesh.scene = myscene
    filename = popupcad.exportdir + os.path.sep +  str(self.id) + '.dae' #
    mesh.write(filename)


def createDAEFromShape(self, s, layer_num, mesh, thickness): #TODO Move this method into the shape class.
    import collada
    vertices = s.extrudeVertices(thickness, z0=layer_num)

    #This scales the verticies properly. So that they are in millimeters.
    vert_floats = [float(x)/(popupcad.SI_length_scaling) for x in vertices]
    vert_src_name = str(self.id) + '|' + str(s.id) + "-array"
    vert_src = collada.source.FloatSource(vert_src_name, numpy.array(vert_floats), ('X', 'Y', 'Z'))
    geom = collada.geometry.Geometry(mesh, "geometry-" + str(s.id), str(self.id), [vert_src])
    input_list = collada.source.InputList()
    input_list.addInput(0, 'VERTEX', "#" + vert_src_name)
    indices = numpy.array(range(0,(len(vertices) // 3)));
    triset = geom.createTriangleSet(indices, input_list, "materialref" + str(s.id))
    triset.generateNormals()
    geom.primitives.append(triset)
    return geom
