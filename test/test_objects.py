from unittest import TestCase
from artapsegment.objects import Node


class TestNodeOperations(TestCase):

    def test_node_init(self):
        # initialize without an id number
        self.assertEqual((1., 1.), Node(1., 1.).as_tuple())

        # initialize with an id number
