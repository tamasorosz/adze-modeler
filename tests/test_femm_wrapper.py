from unittest import TestCase
from adze_modeler.femm_wrapper import FemmWriter
from importlib_resources import files


class FemmTester(TestCase):

    def test_addnode(self):
        x = 1.0
        y = 0.0

        res = FemmWriter.add_node(x, y)
        self.assertEqual('mi_addnode(1.0, 0.0)', res)

    def test_add_segment(self):
        x1 = 1.0
        y1 = 0.0

        x2 = 1.0
        y2 = 1.0

        res = FemmWriter.add_segment(x1, y1, x2, y2)
        self.assertEqual('mi_addsegment(1.0, 0.0, 1.0, 1.0)', res)

    def test_addblocklabel(self):
        x = 1.0
        y = 0.0

        res = FemmWriter.add_blocklabel(x, y)
        self.assertEqual('mi_addblocklabel(1.0, 0.0)', res)

    def test_addarc(self):
        x1, x2 = 1.0, 1.0
        y1, y2 = 0.0, 1.0

        res = FemmWriter.add_arc(x1, y1, x2, y2, 90.0, 1)
        self.assertEqual('mi_addarc(1.0, 0.0, 1.0, 1.0, 90.0, 1)', res)

    def test_delete_selected(self):
        self.assertEqual('mi_deleteselected', FemmWriter.delete_selected())

    def test_delete_selected_nodes(self):
        self.assertEqual('mi_deleteselectednodes', FemmWriter.delete_selected_nodes())

    def test_delete_selected_labels(self):
        self.assertEqual('mi_deleteselectedlabels', FemmWriter.delete_selected_labels())

    def test_delete_selected_segments(self):
        self.assertEqual('mi_deleteselectedsegments', FemmWriter.delete_selected_labels())

    def test_delete_selected_arc_segments(self):
        self.assertEqual('mi_deleteselectedarcsegments', FemmWriter.delete_delete_selected_arc_segments())
