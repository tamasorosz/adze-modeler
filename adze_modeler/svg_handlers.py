import svgpathtools as svg
import pygmsh
import adze_modeler.geometry as geo
import adze_modeler.objects as obj
import cmath


def import_svg(svg_img, *args):
    """ Imports the svg file into a new geo object. The function gives an automatic id to the function

    svg_img: the name of the file, which contains the imported svg image
    return: gives back a new geometry
    """

    # reads the main objects from an svg file
    paths = svg.svg2paths(svg_img)
    imported_geo = geo.Geometry()

    # id start from the given number
    id = 0

    for path in paths:
        for seg in path:
            if isinstance(seg, svg.Path):
                for element in seg:
                    if isinstance(element, svg.Line):
                        start = obj.Node(element.start.real, element.start.imag, id)
                        end = obj.Node(element.end.real, element.end.imag, id + 1)
                        imported_geo.add_line(obj.Line(start, end, id + 2))
                        id += 3

                    if isinstance(element, svg.CubicBezier):
                        start = obj.Node(element.start.real, element.start.imag, id)
                        control1 = obj.Node(element.control1.real, element.control1.imag, id + 1)
                        control2 = obj.Node(element.control2.real, element.control2.imag, id + 2)
                        end = obj.Node(element.end.real, element.end.imag, id + 3)
                        imported_geo.add_cubic_bezier(obj.CubicBezier(start, control1, control2, end, id + 4))
                        id += 5

    imported_geo.merge_points()

    # print(imported_geo)
    return imported_geo


if __name__ == "__main__":
    with pygmsh.geo.Geometry() as geom:
        lcar = 0.1
        p1 = geom.add_point([0.0, 0.0], lcar)
        p2 = geom.add_point([1.0, 0.0], lcar)
        p3 = geom.add_point([1.0, 0.5], lcar)
        p4 = geom.add_point([1.0, 1.0], lcar)
        s1 = geom.add_bspline([p1, p2, p3, p4])

        p2 = geom.add_point([0.0, 1.0], lcar)
        p3 = geom.add_point([0.5, 1.0], lcar)
        s2 = geom.add_spline([p4, p3, p2, p1])

        ll = geom.add_curve_loop([s1, s2])
        pl = geom.add_plane_surface(ll)

        mesh = geom.generate_mesh()
        mesh.write("test.vtk")
