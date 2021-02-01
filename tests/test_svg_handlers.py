from unittest import TestCase
from artapsegment.svg_handlers import import_svg
import os


class TestSvgImport(TestCase):

    def test_owl_import_to_geometry(self):
        # path = os.path.join(ROOT_DIR, "examples/owl", "owl-svgrepo-com.svg")
        geo = import_svg("test.svg")

        # checks the first coordinate of the first node
        self.assertEqual(82.020832, geo.nodes[0].x)

        # the number of lines and cubicbeziers should be larger than 0
        self.assertTrue(len(geo.lines) > 0)
        self.assertTrue(len(geo.cubic_beziers) == 0)
        self.assertTrue(len(geo.circle_arcs) == 0)
