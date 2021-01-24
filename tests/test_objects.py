from unittest import TestCase
from artapsegment.objects import Node
from math import pi


class TestNodeOperations(TestCase):

    def test_node_init(self):
        # initialize without an id number
        self.assertEqual((1., 1.), Node(1., 1.).as_tuple())

    def test_rotate_a_node(self):
        a = Node(1.0, 0.0)
        c = a.rotate(pi / 2)
        self.assertEqual((0., 1.), c.as_tuple())

    def test_rotate_node_around_a_point(self):
        a = Node(1.0, 0.0)
        b = Node(0.5, 0.0)

        d = a.rotate_about(b, pi / 2)
        self.assertEqual((0.5, 0.5), d.as_tuple())

    def test_strings(self):
        a = Node(1.0, 0.0)
        self.assertEqual('(1.0, 0.0, id=None,label=None)', str(a))

    def test_distance(self):
        a = Node(1.0, 0.0)
        b = Node(0.5, 0.0)
        c = a + b
        d = a - b
        e = a*2.
        self.assertEqual((1.5, 0.0), c.as_tuple())
        self.assertEqual((0.5, 0.0), d.as_tuple())
        self.assertEqual((2.0, 0.0), e.as_tuple())
