"""
This class realize a layer, where the different elements of the geometry can be stored.
A general geometrical shape can defined by the following objects:
    Nodes (Points), Lines, Circle Arcs, Cubic Bezeirs
"""

from artapsegment.objects import Node, Line, CubicBezier
import pygmsh.geo as gmsh


class Geometry():

    def __init__(self):
        self.nodes = []
        self.lines = []
        self.circle_arcs = []
        self.cubic_beziers = []

    def add_object(self):
        return

    def add_node(self, node):
        self.nodes.append(node)

    def add_line(self, line):
        self.lines.append(line)
        # save every start and end points for the geoemtry
        self.nodes.append(line.start_pt)
        self.nodes.append(line.end_pt)

    def add_cubic_bezier(self, cb):
        self.cubic_beziers.append(cb)

        self.nodes.append(cb.start_pt)
        self.nodes.append(cb.control1)
        self.nodes.append(cb.control2)
        self.nodes.append(cb.end_pt)

    def meshi_it(self, mesh_strategy):
        mesh = mesh_strategy(self.nodes, self.lines, self.circle_arcs, self.cubic_beziers)
        return mesh

    def __repr__(self):
        msg = ""
        msg += str("\n Nodes: \n -----------------------\n")
        for node in self.nodes:
            msg += str(node) + "\n"

        msg += str("\n Lines: \n -----------------------\n")
        for line in self.lines:
            msg += str(line) + "\n"

        msg += str("\n CubicBezier: \n -----------------------\n")
        for cubicbezier in self.cubic_beziers:
            msg += str(cubicbezier) + "\n"

        return msg


def gmsh_strategy(nodes, lines, arcs, cubic_beziers):
    lcar = 0.011
    with gmsh.Geometry() as geom:
        # add lines
        for line in lines:
            start_pt = geom.add_point([line.start_pt.x, line.start_pt.y], lcar)
            end_pt = geom.add_point([line.end_pt.x, line.end_pt.y], lcar)
            geom.add_line(p0=start_pt, p1=end_pt)


        # add cubic beziers
        #for cb in cubic_beziers:
        #    geom.add_bspline([cb.start_pt.id, cb.control1.id, cb.control2.id, cb.end_pt.id])

        # add nodes
        # points = []
        # for node in nodes:
        #    points.append(geom.add_point([node.x, node.y, node.id], lcar))

        # mesh = geom.generate_mesh()
        geom.save_geometry("test.geo_unrolled")
        #mesh.write("test.vtk")

    # with pygmsh.geo.Geometry() as geom:
    #     lcar = 0.1
    #     p1 = geom.add_point([0.0, 0.0], lcar)
    #     p2 = geom.add_point([1.0, 0.0], lcar)
    #     p3 = geom.add_point([1.0, 0.5], lcar)
    #     p4 = geom.add_point([1.0, 1.0], lcar)
    #     s1 = geom.add_bspline([p1, p2, p3, p4])
    #
    #     p2 = geom.add_point([0.0, 1.0], lcar)
    #     p3 = geom.add_point([0.5, 1.0], lcar)
    #     s2 = geom.add_spline([p4, p3, p2, p1])
    #
    #     ll = geom.add_curve_loop([s1, s2])
    #     pl = geom.add_plane_surface(ll)
    #
    #     mesh = geom.generate_mesh()
    #     mesh.write("test.vtk")
