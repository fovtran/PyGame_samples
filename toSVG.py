from IPython.display import SVG

def tosvg(polygons,border=0):
    import xml.etree.ElementTree as ET

    colors = ['aqua','blue','fuchsia','gray','green','lime','maroon',  'navy','olive','purple','red','silver','teal','yellow']

    xmin,xmax,ymin,ymax = bbox(polygons,border)
    width = xmax-xmin
    height = ymax-ymin

    svg = ET.Element('svg', xmlns="http://www.w3.org/2000/svg", version="1.1",
                    height="%s" % height, width="%s" % width)
    for i,polygon in enumerate(polygons):
        point_list = " ".join(["%d,%d" % (x-xmin,y-ymin) for (x,y) in polygon])
        ET.SubElement(svg,"polygon",fill=colors[i%len(colors)],
                      stroke="black",points=point_list)
    #ET.dump(svg)
    return ET.tostring(svg)

def bbox(polygons,border=0,BIG=1e10):
    xmin=ymin = BIG
    xmax=ymax = -BIG
    for polygon in polygons:
        for x,y in polygon:
            xmax = max(xmax,x)
            xmin = min(xmin,x)
            ymax = max(ymax,y)
            ymin = min(ymin,y)
    return xmin-border,xmax+border,ymin-border,ymax+border

polygons = [
    [(-20,0),(0,100),(5,100),(5,0)],
    [(1,1),(1,10),(10,10),(10,1)],
    [(10,10),(10,50),(50,50),(50,10)],
    [(50,50),(50,150),(150,150),(150,50)],
    ]


SVG(tosvg(polygons))
