"""
The goal of this module is to write out the given geometry into a FEMM's lua script.
The code generated one snapshot from the created model, which can be run during the Optimization.
"""

from adze_modeler.geometry import Geometry
from string import Template

fields = {'electrostatic', 'magnetic', 'thermal'}


class FemmWriter():

    def write(self, model, file_name):
        """ Generate a runnable lua-script for a FEMM calculation.

        :param model: represents a geometry in the adze-modeler
        :param file_name: the code (re)writes the snapshot from the created geometry to the given code
        """

        with open(file_name, 'w') as writer:
            ...

    # object add remove commnads from FEMM MANUAL page 84.

    @staticmethod
    def add_node(x, y, field='magnetic'):
        """ adds a node to the given point (x,y)"""
        if field == 'magnetic':
            cmd = Template('mi_addnode($x_coord, $y_coord)')

        if field == 'electrostatic':
            cmd = Template('ei_addnode($x_coord, $y_coord)')

        if field == 'heat_flow':
            cmd = Template('hi_addnode($x_coord, $y_coord)')

        if field == 'current_flow':
            cmd = Template('ci_addnode($x_coord, $y_coord)')

        return cmd.substitute(x_coord=x, y_coord=y)

    @staticmethod
    def add_segment(x1, y1, x2, y2, field='magnetic'):
        """ Add a new line segment from node closest to (x1,y1) tonode closest to (x2,y2) """
        if field == 'magnetic':
            cmd = Template('mi_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        if field == 'electrostatic':
            cmd = Template('ei_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        if field == 'heat_flow':
            cmd = Template('hi_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        if field == 'current_flow':
            cmd = Template('ci_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        return cmd.substitute(x1_coord=x1, y1_coord=y1, x2_coord=x2, y2_coord=y2)

    @staticmethod
    def add_blocklabel(x, y, field='magnetic'):
        """ Add a new block label at (x,y) """

        if field == 'magnetic':
            cmd = Template('mi_addblocklabel($x_coord, $y_coord)')

        if field == 'electrostatic':
            cmd = Template('ei_addblocklabel($x_coord, $y_coord)')

        if field == 'heat_flow':
            cmd = Template('hi_addblocklabel($x_coord, $y_coord)')

        if field == 'current_flow':
            cmd = Template('ci_addblocklabel($x_coord, $y_coord)')

        return cmd.substitute(x_coord=x, y_coord=y)

    @staticmethod
    def add_arc(x1, y1, x2, y2, angle, maxseg, field='magnetic'):
        """
        Add a new arc segment from the nearest nodeto (x1,y1) to the nearest node to (x2,y2)
        with angle ‘angle’ divided into ‘maxseg’ segments.
        """
        if field == 'magnetic':
            cmd = Template('mi_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        if field == 'electrostatic':
            cmd = Template('ei_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        if field == 'heat_flow':
            cmd = Template('hi_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        if field == 'current_flow':
            cmd = Template('ci_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        return cmd.substitute(x_1=x1, y_1=y1, x_2=x2, y_2=y2, angle=angle, maxseg=maxseg)

    @staticmethod
    def delete_selected(field='magnetic'):
        """Delete all selected objects """

        if field == 'magnetic':
            cmd = 'mi_deleteselected'

        if field == 'electrostatic':
            cmd = 'ei_deleteselected'

        if field == 'heat_flow':
            cmd = 'hi_deleteselected'

        if field == 'current_flow':
            cmd = 'ci_deleteselected'

        return cmd

    @staticmethod
    def delete_selected_nodes(field='magnetic'):
        """Delete all selected nodes, the object should be selected the node selection command. """

        if field == 'magnetic':
            cmd = 'mi_deleteselectednodes'

        if field == 'electrostatic':
            cmd = 'ei_deleteselectednodes'

        if field == 'heat_flow':
            cmd = 'hi_deleteselectednodes'

        if field == 'current_flow':
            cmd = 'ci_deleteselectednodes'

        return cmd

    @staticmethod
    def delete_selected_labels(field='magnetic'):
        """Delete all selected labels """

        if field == 'magnetic':
            cmd = 'mi_deleteselectedlabels'

        if field == 'electrostatic':
            cmd = 'ei_deleteselectedlabels'

        if field == 'heat_flow':
            cmd = 'hi_deleteselectedlabels'

        if field == 'current_flow':
            cmd = 'ci_deleteselectedlabels'

        return cmd

    @staticmethod
    def delete_selected_segments(field='magnetic'):
        """Delete all selected segments. """

        if field == 'magnetic':
            cmd = 'mi_deleteselectedlabels'

        if field == 'electrostatic':
            cmd = 'ei_deleteselectedlabels'

        if field == 'heat_flow':
            cmd = 'hi_deleteselectedlabels'

        if field == 'current_flow':
            cmd = 'ci_deleteselectedlabels'

        return cmd

    @staticmethod
    def delete_delete_selected_arc_segments(field='magnetic'):
        """Delete all selected arc segments. """

        if field == 'magnetic':
            cmd = 'mi_deleteselectedarcsegments'

        if field == 'electrostatic':
            cmd = 'ei_deleteselectedarcsegments'

        if field == 'heat_flow':
            cmd = 'hi_deleteselectedarcsegments'

        if field == 'current_flow':
            cmd = 'ci_deleteselectedarcsegments'

        return cmd

    # object selection commnads from FEMM MANUAL page 84.

    @staticmethod
    def clear_selected(field='magnetic'):
        """ Clear all selected nodes, blocks, segments and arc segments. """

        if field == 'magnetic':
            cmd = 'mi_clearselected()'

        if field == 'electrostatic':
            cmd = 'ei_clearselected()'

        if field == 'heat_flow':
            cmd = 'hi_clearselected()'

        if field == 'current_flow':
            cmd = 'ci_clearselected()'

        return cmd

    @staticmethod
    def select_segment(x, y, field='magnetic'):
        """Select the line segment closest to (x,y) """

        if field == 'magnetic':
            cmd = Template('mi_selectsegment($xp, $yp)')

        if field == 'electrostatic':
            cmd = Template('ei_selectsegment($xp, $yp)')

        if field == 'heat_flow':
            cmd = Template('hi_selectsegment($xp, $yp)')

        if field == 'current_flow':
            cmd = Template('ci_selectsegment($xp, $yp)')

        return cmd.substitute(xp=x, yp=y)

    @staticmethod
    def select_node(x, y, field='magnetic'):
        """Select node closest to (x,y), Returns the coordinates ofthe se-lected node """

        if field == 'magnetic':
            cmd = Template('mi_selectnode($xp, $yp)')

        if field == 'electrostatic':
            cmd = Template('ei_selectnode($xp, $yp)')

        if field == 'heat_flow':
            cmd = Template('hi_selectnode($xp, $yp)')

        if field == 'current_flow':
            cmd = Template('ci_selectnode($xp, $yp)')

        return cmd.substitute(xp=x, yp=y)

    @staticmethod
    def select_label(x, y, field='magnetic'):
        """ Select the label closet to (x,y). Returns the coordinates of the selected label. """

        if field == 'magnetic':
            cmd = Template('mi_selectlabel($xp, $yp)')

        if field == 'electrostatic':
            cmd = Template('ei_selectlabel($xp, $yp)')

        if field == 'heat_flow':
            cmd = Template('hi_selectlabel($xp, $yp)')

        if field == 'current_flow':
            cmd = Template('ci_selectlabel($xp, $yp)')

        return cmd.substitute(xp=x, yp=y)

    @staticmethod
    def select_group(n, field='magnetic'):
        """
        Select the n th group of nodes, segments, arc segments and block labels.
        This function will clear all previously selected elements and leave the edit mode in 4(group)
        """

        if field == 'magnetic':
            cmd = Template('mi_selectgroup($np)')

        if field == 'electrostatic':
            cmd = Template('ei_selectgroup($np)')

        if field == 'heat_flow':
            cmd = Template('hi_selectgroup($np)')

        if field == 'current_flow':
            cmd = Template('ci_selectgroup($np)')

        return cmd.substitute(np=n)

    @staticmethod
    def select_circle(x, y, R, editmode, field='magnetic'):
        """
        Select circle selects objects within a circle of radius R centered at(x, y).If only x, y, and R paramters
        are given, the current edit mode is used.If the editmode parameter is used, 0 denotes nodes, 2 denotes block
        labels, 2 denotes segments, 3 denotes arcs, and 4 specifies that all entity types are to be selected.
        """

        if field == 'magnetic':
            cmd = Template('mi_selectcircle($xp, $yp, $Rp, $Editmode)')

        if field == 'electrostatic':
            cmd = Template('ei_selectcircle($xp, $yp, $Rp, $Editmode)')

        if field == 'heat_flow':
            cmd = Template('hi_selectcircle($xp, $yp, $Rp, $Editmode)')

        if field == 'current_flow':
            cmd = Template('ci_selectcircle($xp, $yp, $Rp, $Editmode)')

        return cmd.substitute(xp=x, yp=y, Rp=R, Editmode=editmode)

    @staticmethod
    def select_rectangle(x1, y1, x2, y2, editmode, field='magnetic'):
        """
        This command selects objects within a rectangle definedby points (x1,y1) and (x2,y2).
        If no editmode parameter is supplied, the current edit mode isused. If the editmode parameter is used,
        0 denotes nodes, 2 denotes block labels, 2 denotessegments, 3 denotes arcs, and 4 specifies that all
        entity types are to be selected.
        """

        if field == 'magnetic':
            cmd = Template('mi_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        if field == 'electrostatic':
            cmd = Template('ei_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        if field == 'heat_flow':
            cmd = Template('hi_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        if field == 'current_flow':
            cmd = Template('ci_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        return cmd.substitute(x1p=x1, y1p=y1, x2p=x2, y2p=y2, Editmode=editmode)

    # Gmsh ASCII output uses `%.16g` for floating point values,
    # meshio uses same precision but exponential notation `%.16e`.
    # def write(filename, mesh, fmt_version="4.1", binary=True, float_fmt=".16e"):
    #     """Writes a Gmsh msh file."""
    #     try:
    #         writer = _writers[fmt_version]
    #     except KeyError:
    #         try:
    #             writer = _writers[fmt_version]
    #         except KeyError:
    #             raise WriteError(
    #                 "Need mesh format in {} (got {})".format(
    #                     sorted(_writers.keys()), fmt_version
    #                 )
    #             )


"""
-- Analysis parameters
radius = 300 -- mm
iterations = 1
displacement_inc = 10/50 -- mm
mydir = "./"
open(mydir .. "AF_AntiPeriodic.fem")

file_out = openfile(mydir .. "output.txt" , "w")

for i = 0, iterations do
    mi_analyze()
    mi_loadsolution()
    mo_groupselectblock(2)
    fx = mo_blockintegral(18)
    torque = fx*radius/1000*14
    displ = i*displacement_inc
    write(file_out, i, ",", displ, "," , torque, ",", radius, ",", a, ",", b, "\n")
    if (i < iterations) then
        mi_selectgroup(2)
        mi_movetranslate(displacement_inc, 0)
    end
end

closefile(file_out)

mo_close()
mi_close()
quit()
"""
