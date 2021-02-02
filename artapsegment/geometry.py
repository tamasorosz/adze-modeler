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
        self.epsilon = 1.e-5

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

    def merge_points(self):

        for i in range(len(self.nodes) - 1):
            for j in range(len(self.nodes) - 1, i, -1):
                if self.nodes[i].distance_to(self.nodes[j]) < self.epsilon:

                    # renumber the start/end points of the different shape elements
                    for line in self.lines:
                        if line.start_pt.id == self.nodes[j].id:
                            line.start_pt.id = self.nodes[i].id

                        if line.end_pt.id == self.nodes[j].id:
                            line.end_pt.id = self.nodes[i].id

                    del self.nodes[j]
            # if node_1.distance_to(node_2) < self.epsilon:
            #    print(i)

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


def node_gmsh_point_distance(node, point):
    dx = node.x - point.x[0]
    dy = node.y - point.x[1]

    return (dx ** 2. + dy ** 2.) ** 0.5


def gmsh_strategy(nodes, lines, arcs, cubic_beziers):
    lcar = 5.
    epsilon = 1e-6
    with gmsh.Geometry() as geom:
        # add nodes
        points = []
        for node in nodes:
            temp = geom.add_point([node.x, node.y], lcar)
            # temp._id = node.id
            points.append(temp)

        # add lines
        glines = []
        for line in lines:
            for i in range(len(points)):
                if node_gmsh_point_distance(line.start_pt, points[i]) < epsilon:
                    start_pt = points[i]

                if node_gmsh_point_distance(line.end_pt, points[i]) < epsilon:
                    end_pt = points[i]

            temp = geom.add_line(p0=start_pt, p1=end_pt)
            glines.append(temp)

        ll = geom.add_curve_loop(glines)
        pl = geom.add_plane_surface(ll)

        # add cubic beziers
        # for cb in cubic_beziers:
        #    geom.add_bspline([cb.start_pt.id, cb.control1.id, cb.control2.id, cb.end_pt.id])

        geom.save_geometry("test.geo_unrolled")
        mesh = geom.generate_mesh()
        mesh.write("test.vtk")

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
