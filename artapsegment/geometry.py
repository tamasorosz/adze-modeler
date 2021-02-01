"""
This class realize a layer, where the different elements of the geometry can be stored.
A general geometrical shape can defined by the following objects:
    Nodes (Points), Lines, Circle Arcs, Cubic Bezeirs
"""

from artapsegment.objects import Node, Line, CubicBezier


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
        mesh = mesh_strategy(self.nodes, self.lines)
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
