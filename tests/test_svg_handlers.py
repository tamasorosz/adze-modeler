from unittest import TestCase
from artapsegment.svg_handlers import import_svg
from importlib_resources import files


# Reads contents with UTF-8 encoding and returns str.
# eml = files('email.tests.data').joinpath('message.eml').read_text()


class TestSvgImport(TestCase):

    def test_owl_import_to_geometry(self):
        eml = files('examples.triangle').joinpath('triangle.svg')
        print(eml)
        geo = import_svg(eml.as_posix())

        # checks the first coordinate of the first node
        self.assertEqual(82.020832, geo.nodes[0].x)

        # the number of lines and cubicbeziers should be larger than 0
        self.assertTrue(len(geo.lines) > 0)
        self.assertTrue(len(geo.cubic_beziers) == 0)
        self.assertTrue(len(geo.circle_arcs) == 0)
