import svgpathtools as svg
import os
import artapsegment.geometry as geo
import cmath


def import_svg(svg_img):
    """
    Imports the svg file into a new geo object.

    svg_img: the name of the file, which contains the imported svg image
    return: gives back a new geometry
    """

    # reads the main objects from an svg file
    paths = svg.svg2paths(svg_img)
    imported_geo = geo.Geometry()

    for path in paths:
        for seg in path:
            if isinstance(seg, svg.Path):
                for element in seg:
                    if isinstance(element, svg.Line):
                        start = geo.Node(element.start.real, element.start.imag)
                        end = geo.Node(element.end.real, element.end.imag)
                        imported_geo.add_line(geo.Line(start, end))
                    if isinstance(element, svg.CubicBezier):
                        start = geo.Node(element.start.real, element.start.imag)
                        control1 = geo.Node(element.control1.real, element.control1.imag)
                        control2 = geo.Node(element.control2.real, element.control2.imag)
                        end = geo.Node(element.end.real, element.end.imag)
                        imported_geo.add_cubic_bezier(geo.CubicBezier(start, control1, control2, end))

    #print(imported_geo)
    return imported_geo


if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(ROOT_DIR)

    path = os.path.join(ROOT_DIR, "examples/owl", "owl-svgrepo-com.svg")
    # path = os.path.join(ROOT_DIR, "examples/triangle", "triangle.svg")
    import_svg(path)
    # paths, attributes = svg2paths(path)
    #
    # # Let's print out the first path object and the color it was in the SVG
    # # We'll see it is composed of two CubicBezier objects and, in the SVG file it
    # # came from, it was red
    # redpath = paths[0]
    # redpath_attribs = attributes[0]
    # print(paths)
    # #print(redpath_attribs)
    # #sprint(attributes)
