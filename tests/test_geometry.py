from unittest import TestCase
from artapsegment.geometry import Geometry
from artapsegment.objects import Node, Line, CubicBezier


class TestGeometry(TestCase):

    def test_initialization(self):
        geo = Geometry()

        self.assertEqual([], geo.lines)
