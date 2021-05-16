from unittest import TestCase

from adze_modeler.femm_wrapper import FemmWriter
from adze_modeler.femm_wrapper import kw_current_flow
from adze_modeler.femm_wrapper import kw_electrostatic
from adze_modeler.femm_wrapper import kw_heat_flow


class FemmTester(TestCase):

    def test_not_defined_writer(self):
        writer = FemmWriter()
        writer.field = None

        self.assertRaises(ValueError)

    def test_addnode(self):
        x = 1.0
        y = 0.0

        # magnetic field
        res = FemmWriter().add_node(x, y)
        self.assertEqual("mi_addnode(1.0, 0.0)", res)

        # current flow
        fmw = FemmWriter()
        fmw.field = kw_current_flow
        res = fmw.add_node(x, y)
        self.assertEqual("ci_addnode(1.0, 0.0)", res)

        # electrostatic
        fmw = FemmWriter()
        fmw.field = kw_electrostatic
        res = fmw.add_node(x, y)
        self.assertEqual("ei_addnode(1.0, 0.0)", res)

        fmw = FemmWriter()
        fmw.field = kw_heat_flow
        res = fmw.add_node(x, y)
        self.assertEqual("hi_addnode(1.0, 0.0)", res)

    def test_add_segment(self):
        x1 = 1.0
        y1 = 0.0

        x2 = 1.0
        y2 = 1.0

        res = FemmWriter().add_segment(x1, y1, x2, y2)
        self.assertEqual("mi_addsegment(1.0, 0.0, 1.0, 1.0)", res)

        # current field
        fmw = FemmWriter()
        fmw.field = kw_current_flow
        res = fmw.add_segment(x1, y1, x2, y2)
        self.assertEqual("ci_addsegment(1.0, 0.0, 1.0, 1.0)", res)

        # electrostatic field
        fmw = FemmWriter()
        fmw.field = kw_electrostatic
        res = fmw.add_segment(x1, y1, x2, y2)
        self.assertEqual("ei_addsegment(1.0, 0.0, 1.0, 1.0)", res)

        # heat flow
        fmw = FemmWriter()
        fmw.field = kw_heat_flow
        res = fmw.add_segment(x1, y1, x2, y2)
        self.assertEqual("hi_addsegment(1.0, 0.0, 1.0, 1.0)", res)

    def test_addblocklabel(self):
        x = 1.0
        y = 0.0

        res = FemmWriter().add_blocklabel(x, y)
        self.assertEqual("mi_addblocklabel(1.0, 0.0)", res)

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        res = fmw.add_blocklabel(x, y)
        self.assertEqual("ci_addblocklabel(1.0, 0.0)", res)

        fmw.field = kw_heat_flow
        res = fmw.add_blocklabel(x, y)
        self.assertEqual("hi_addblocklabel(1.0, 0.0)", res)

        fmw.field = kw_electrostatic
        res = fmw.add_blocklabel(x, y)
        self.assertEqual("ei_addblocklabel(1.0, 0.0)", res)

    def test_addarc(self):
        x1, x2 = 1.0, 1.0
        y1, y2 = 0.0, 1.0

        res = FemmWriter().add_arc(x1, y1, x2, y2, 90.0, 1)
        self.assertEqual("mi_addarc(1.0, 0.0, 1.0, 1.0, 90.0, 1)", res)

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        res = fmw.add_arc(x1, y1, x2, y2, 90.0, 1)
        self.assertEqual("ci_addarc(1.0, 0.0, 1.0, 1.0, 90.0, 1)", res)

        fmw.field = kw_electrostatic
        res = fmw.add_arc(x1, y1, x2, y2, 90.0, 1)
        self.assertEqual("ei_addarc(1.0, 0.0, 1.0, 1.0, 90.0, 1)", res)

        fmw.field = kw_heat_flow
        res = fmw.add_arc(x1, y1, x2, y2, 90.0, 1)
        self.assertEqual("hi_addarc(1.0, 0.0, 1.0, 1.0, 90.0, 1)", res)

    def test_delete_selected(self):
        self.assertEqual("mi_deleteselected", FemmWriter().delete_selected())

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_deleteselected", fmw.delete_selected())

        fmw.field = kw_heat_flow
        self.assertEqual("hi_deleteselected", fmw.delete_selected())

        fmw.field = kw_electrostatic
        self.assertEqual("ei_deleteselected", fmw.delete_selected())

    def test_delete_selected_nodes(self):
        self.assertEqual("mi_deleteselectednodes", FemmWriter().delete_selected_nodes())

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_deleteselectednodes", fmw.delete_selected_nodes())

        fmw.field = kw_heat_flow
        self.assertEqual("hi_deleteselectednodes", fmw.delete_selected_nodes())

        fmw.field = kw_electrostatic
        self.assertEqual("ei_deleteselectednodes", fmw.delete_selected_nodes())

    def test_delete_selected_labels(self):
        self.assertEqual("mi_deleteselectedlabels", FemmWriter().delete_selected_labels())

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_deleteselectedlabels", fmw.delete_selected_labels())

        fmw.field = kw_heat_flow
        self.assertEqual("hi_deleteselectedlabels", fmw.delete_selected_labels())

        fmw.field = kw_electrostatic
        self.assertEqual("ei_deleteselectedlabels", fmw.delete_selected_labels())

    def test_delete_selected_segments(self):
        self.assertEqual("mi_deleteselectedsegments", FemmWriter().delete_selected_segments())

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_deleteselectedsegments", fmw.delete_selected_segments())

        fmw.field = kw_heat_flow
        self.assertEqual("hi_deleteselectedsegments", fmw.delete_selected_segments())

        fmw.field = kw_electrostatic
        self.assertEqual("ei_deleteselectedsegments", fmw.delete_selected_segments())

    def test_delete_selected_arc_segments(self):
        self.assertEqual("mi_deleteselectedarcsegments", FemmWriter().delete_delete_selected_arc_segments())

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_deleteselectedarcsegments", fmw.delete_delete_selected_arc_segments())

        fmw.field = kw_heat_flow
        self.assertEqual("hi_deleteselectedarcsegments", fmw.delete_delete_selected_arc_segments())

        fmw.field = kw_electrostatic
        self.assertEqual("ei_deleteselectedarcsegments", fmw.delete_delete_selected_arc_segments())

    def test_clear_seelcted(self):
        self.assertEqual("mi_clearselected()", FemmWriter().clear_selected())

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_clearselected()", fmw.clear_selected())

        fmw.field = kw_heat_flow
        self.assertEqual("hi_clearselected()", fmw.clear_selected())

        fmw.field = kw_electrostatic
        self.assertEqual("ei_clearselected()", fmw.clear_selected())

    def test_select_segment(self):
        self.assertEqual("mi_selectsegment(1.0, 1.0)", FemmWriter().select_segment(1.0, 1.0))

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_selectsegment(1.0, 1.0)", fmw.select_segment(1.0, 1.0))

        fmw.field = kw_heat_flow
        self.assertEqual("hi_selectsegment(1.0, 1.0)", fmw.select_segment(1.0, 1.0))

        fmw.field = kw_electrostatic
        self.assertEqual("ei_selectsegment(1.0, 1.0)", fmw.select_segment(1.0, 1.0))

    def test_select_node(self):
        self.assertEqual("mi_selectnode(1.0, 1.0)", FemmWriter().select_node(1.0, 1.0))

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_selectnode(1.0, 1.0)", fmw.select_node(1.0, 1.0))

        fmw.field = kw_heat_flow
        self.assertEqual("hi_selectnode(1.0, 1.0)", fmw.select_node(1.0, 1.0))

        fmw.field = kw_electrostatic
        self.assertEqual("ei_selectnode(1.0, 1.0)", fmw.select_node(1.0, 1.0))

    def test_select_label(self):
        self.assertEqual("mi_selectlabel(1.0, 1.0)", FemmWriter().select_label(1.0, 1.0))

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_selectlabel(1.0, 1.0)", fmw.select_label(1.0, 1.0))

        fmw.field = kw_heat_flow
        self.assertEqual("hi_selectlabel(1.0, 1.0)", fmw.select_label(1.0, 1.0))

        fmw.field = kw_electrostatic
        self.assertEqual("ei_selectlabel(1.0, 1.0)", fmw.select_label(1.0, 1.0))

    def test_select_group(self):
        self.assertEqual("mi_selectgroup(4)", FemmWriter().select_group(4))

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_selectgroup(4)", fmw.select_group(4))

        fmw.field = kw_heat_flow
        self.assertEqual("hi_selectgroup(4)", fmw.select_group(4))

        fmw.field = kw_electrostatic
        self.assertEqual("ei_selectgroup(4)", fmw.select_group(4))

    def test_select_circle(self):
        self.assertEqual("mi_selectcircle(1.0, 2.0, 0.4, 3)", FemmWriter().select_circle(1.0, 2.0, 0.4, 3))

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_selectcircle(1.0, 2.0, 0.4, 3)", fmw.select_circle(1.0, 2.0, 0.4, 3))

        fmw.field = kw_heat_flow
        self.assertEqual("hi_selectcircle(1.0, 2.0, 0.4, 3)", fmw.select_circle(1.0, 2.0, 0.4, 3))

        fmw.field = kw_electrostatic
        self.assertEqual("ei_selectcircle(1.0, 2.0, 0.4, 3)", fmw.select_circle(1.0, 2.0, 0.4, 3))

    def test_select_rectangle(self):
        self.assertEqual("mi_selectrectangle(1.0,2.0,3.0,4.0,3)", FemmWriter().select_rectangle(1.0, 2.0, 3.0, 4.0, 3))

        fmw = FemmWriter()
        fmw.field = kw_current_flow
        self.assertEqual("ci_selectrectangle(1.0,2.0,3.0,4.0,3)", fmw.select_rectangle(1.0, 2.0, 3.0, 4.0, 3))

        fmw.field = kw_heat_flow
        self.assertEqual("hi_selectrectangle(1.0,2.0,3.0,4.0,3)", fmw.select_rectangle(1.0, 2.0, 3.0, 4.0, 3))

        fmw.field = kw_electrostatic
        self.assertEqual("ei_selectrectangle(1.0,2.0,3.0,4.0,3)", fmw.select_rectangle(1.0, 2.0, 3.0, 4.0, 3))

    def test_magnetic_problem(self):
        self.assertEqual("mi_probdef(50,millimeters,axi,1e-08, 1, 30, 0)", FemmWriter().magnetic_problem(50, 'millimeters', 'axi'))
