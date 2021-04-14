"""
The goal of this module is to write out the given geometry into a FEMM's lua script.
The code generated one snapshot from the created model, which can be run during the Optimization.

The original FEMM code has separate scripting commands for the geometry generation in different subfields

"""

from adze_modeler.geometry import Geometry
from string import Template

# keywords

kw_current_flow = 'current_flow'
kw_electrostatic = 'electrostatic'
kw_magnetic = 'magnetic'
kw_heat_flow = 'heat_flow'

fields = [kw_electrostatic, kw_magnetic, kw_current_flow, kw_heat_flow]


class FemmWriter:
    field = kw_magnetic

    def write(self, model, file_name):
        """ Generate a runnable lua-script for a FEMM calculation.

        :param model: represents a geometry in the adze-modeler
        :param file_name: the code (re)writes the snapshot from the created geometry to the given code
        """

        with open(file_name, 'w') as writer:
            ...

    # object add remove commnads from FEMM MANUAL page 84.
    def add_node(self, x, y):
        """ adds a node to the given point (x,y)"""

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_addnode($x_coord, $y_coord)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_addnode($x_coord, $y_coord)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_addnode($x_coord, $y_coord)')

        if self.field == kw_current_flow:
            cmd = Template('ci_addnode($x_coord, $y_coord)')

        return cmd.substitute(x_coord=x, y_coord=y)

    def add_segment(self, x1, y1, x2, y2):
        """ Add a new line segment from node closest to (x1,y1) tonode closest to (x2,y2) """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        if self.field == kw_current_flow:
            cmd = Template('ci_addsegment($x1_coord, $y1_coord, $x2_coord, $y2_coord)')

        return cmd.substitute(x1_coord=x1, y1_coord=y1, x2_coord=x2, y2_coord=y2)

    def add_blocklabel(self, x, y):
        """ Add a new block label at (x,y) """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_addblocklabel($x_coord, $y_coord)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_addblocklabel($x_coord, $y_coord)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_addblocklabel($x_coord, $y_coord)')

        if self.field == kw_current_flow:
            cmd = Template('ci_addblocklabel($x_coord, $y_coord)')

        return cmd.substitute(x_coord=x, y_coord=y)

    def add_arc(self, x1, y1, x2, y2, angle, maxseg):
        """
        Add a new arc segment from the nearest nodeto (x1,y1) to the nearest node to (x2,y2)
        with angle ‘angle’ divided into ‘maxseg’ segments.
        """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        if self.field == kw_current_flow:
            cmd = Template('ci_addarc($x_1, $y_1, $x_2, $y_2, $angle, $maxseg)')

        return cmd.substitute(x_1=x1, y_1=y1, x_2=x2, y_2=y2, angle=angle, maxseg=maxseg)

    def delete_selected(self):
        """Delete all selected objects """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = 'mi_deleteselected'

        if self.field == kw_electrostatic:
            cmd = 'ei_deleteselected'

        if self.field == kw_heat_flow:
            cmd = 'hi_deleteselected'

        if self.field == kw_current_flow:
            cmd = 'ci_deleteselected'

        return cmd

    def delete_selected_nodes(self):
        """Delete all selected nodes, the object should be selected the node selection command. """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = 'mi_deleteselectednodes'

        if self.field == kw_electrostatic:
            cmd = 'ei_deleteselectednodes'

        if self.field == kw_heat_flow:
            cmd = 'hi_deleteselectednodes'

        if self.field == kw_current_flow:
            cmd = 'ci_deleteselectednodes'

        return cmd

    def delete_selected_labels(self):
        """Delete all selected labels """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = 'mi_deleteselectedlabels'

        if self.field == kw_electrostatic:
            cmd = 'ei_deleteselectedlabels'

        if self.field == kw_heat_flow:
            cmd = 'hi_deleteselectedlabels'

        if self.field == kw_current_flow:
            cmd = 'ci_deleteselectedlabels'

        return cmd

    def delete_selected_segments(self):
        """Delete all selected segments. """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = 'mi_deleteselectedsegments'

        if self.field == kw_electrostatic:
            cmd = 'ei_deleteselectedsegments'

        if self.field == kw_heat_flow:
            cmd = 'hi_deleteselectedsegments'

        if self.field == kw_current_flow:
            cmd = 'ci_deleteselectedsegments'

        return cmd

    def delete_delete_selected_arc_segments(self):
        """Delete all selected arc segments. """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = 'mi_deleteselectedarcsegments'

        if self.field == kw_electrostatic:
            cmd = 'ei_deleteselectedarcsegments'

        if self.field == kw_heat_flow:
            cmd = 'hi_deleteselectedarcsegments'

        if self.field == kw_current_flow:
            cmd = 'ci_deleteselectedarcsegments'

        return cmd

    # object selection commnads from FEMM MANUAL page 84.
    def clear_selected(self):
        """ Clear all selected nodes, blocks, segments and arc segments. """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = 'mi_clearselected()'

        if self.field == kw_electrostatic:
            cmd = 'ei_clearselected()'

        if self.field == kw_heat_flow:
            cmd = 'hi_clearselected()'

        if self.field == kw_current_flow:
            cmd = 'ci_clearselected()'

        return cmd

    def select_segment(self, x, y):
        """Select the line segment closest to (x,y) """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_selectsegment($xp, $yp)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_selectsegment($xp, $yp)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_selectsegment($xp, $yp)')

        if self.field == kw_current_flow:
            cmd = Template('ci_selectsegment($xp, $yp)')

        return cmd.substitute(xp=x, yp=y)

    def select_node(self, x, y):
        """Select node closest to (x,y), Returns the coordinates ofthe se-lected node """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_selectnode($xp, $yp)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_selectnode($xp, $yp)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_selectnode($xp, $yp)')

        if self.field == kw_current_flow:
            cmd = Template('ci_selectnode($xp, $yp)')

        return cmd.substitute(xp=x, yp=y)

    def select_label(self, x, y):
        """ Select the label closet to (x,y). Returns the coordinates of the selected label. """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_selectlabel($xp, $yp)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_selectlabel($xp, $yp)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_selectlabel($xp, $yp)')

        if self.field == kw_current_flow:
            cmd = Template('ci_selectlabel($xp, $yp)')

        return cmd.substitute(xp=x, yp=y)

    def select_group(self, n):
        """
        Select the n th group of nodes, segments, arc segments and block labels.
        This function will clear all previously selected elements and leave the edit mode in 4(group)
        """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_selectgroup($np)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_selectgroup($np)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_selectgroup($np)')

        if self.field == kw_current_flow:
            cmd = Template('ci_selectgroup($np)')

        return cmd.substitute(np=n)

    def select_circle(self, x, y, R, editmode):
        """
        Select circle selects objects within a circle of radius R centered at(x, y).If only x, y, and R paramters
        are given, the current edit mode is used.If the editmode parameter is used, 0 denotes nodes, 2 denotes block
        labels, 2 denotes segments, 3 denotes arcs, and 4 specifies that all entity types are to be selected.
        """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_selectcircle($xp, $yp, $Rp, $Editmode)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_selectcircle($xp, $yp, $Rp, $Editmode)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_selectcircle($xp, $yp, $Rp, $Editmode)')

        if self.field == kw_current_flow:
            cmd = Template('ci_selectcircle($xp, $yp, $Rp, $Editmode)')

        return cmd.substitute(xp=x, yp=y, Rp=R, Editmode=editmode)

    def select_rectangle(self, x1, y1, x2, y2, editmode):
        """
        This command selects objects within a rectangle definedby points (x1,y1) and (x2,y2).
        If no editmode parameter is supplied, the current edit mode isused. If the editmode parameter is used,
        0 denotes nodes, 2 denotes block labels, 2 denotessegments, 3 denotes arcs, and 4 specifies that all
        entity types are to be selected.
        """

        cmd = None
        if self.field not in fields:
            raise ValueError('The physical field is not defined!')

        if self.field == kw_magnetic:
            cmd = Template('mi_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        if self.field == kw_electrostatic:
            cmd = Template('ei_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        if self.field == kw_heat_flow:
            cmd = Template('hi_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        if self.field == kw_current_flow:
            cmd = Template('ci_selectrectangle($x1p,$y1p,$x2p,$y2p,$Editmode)')

        return cmd.substitute(x1p=x1, y1p=y1, x2p=x2, y2p=y2, Editmode=editmode)

    def magnetic_problem(self, freq, units, type, precision=1e-6, depth=None, minangle=None, acsolver=None):
        """
         Definition of the magnetic problem, like probdef(0,'inches','axi',1e-8,0,30);

         :param freq: Frequency in Hertz (required)
         :param units: "inches","millimeters","centimeters","mils","meters, and"micrometers" (required)
         :param type: "planar", "axi" (required)
         :param precision: 1e-8 (required)
         :param depth: depth of the analysis (not mandatory)
         :param minangle: sent to the mesh generator to define the minimum angle of the meshing triangles(not mandatory)
         :param acsolver: the selected acsolver for the problem (not mandatory)


        The generated lua command has the following role:

         miprobdef(frequency,units,type,precision,(depth),(minangle),(acsolver) changes the problem definition.
         Set frequency to the desired frequency in Hertz. The units parameter specifies the units used for measuring
         length in the problem domain. Valid"units"en-tries are"inches","millimeters","centimeters","mils","meters,
         and"micrometers".Set the parameter problem type to"planar"for a 2-D planar problem, or to"axi"for
         anaxisymmetric problem. The precision parameter dictates the precision required by the solver.
         For example, entering 1E-8 requires the RMS of the residual to be less than 10−8.A fifth parameter,
         representing the depth of sthe problem in the into-the-page direction for2-D planar problems, can also also be
         specified. A sixth parameter represents the minimumangle constraint sent to the mesh generator.
         A seventh parameter specifies the solver type tobe used for AC problems.
        """

        return

    # eiprobdef(units,type,precision,(depth),(minangle))changes the problem defi-nition.
    # The units parameter specifies the units used for measuring length in the problemdomain.
    # Valid"units"entries are"inches","millimeters","centimeters","mils","meters, and"micrometers".
    # Setproblemtypeto"planar"for a 2-D planar problem,or to"axi"for an axisymmetric problem.
    # The precisionparameter dictates the precisionrequired by the solver. For example, entering 1.E-8 requires the
    # RMS of the residual to beless than 10−8. A fourth parameter, representing the depth of the problem in the
    # into-the-page direction for 2-D planar problems, can also be specifiedfor planar problems.
    # A sixthparameter represents the minimum angle constraint sent to the mesh generator.

    # hiprobdef(units,type,precision,(depth),(minangle),(prevsoln),(timestep))changes the problem definition.
    # Theunits parameter specifies the units used for measur-ing length in the problem domain.
    # Valid "units"entries are"inches","millimeters","centimeters","mils","meters, and"micrometers".
    # Setproblemtypeto"planar"for a 2-D planar problem, or to"axi"for an axisymmetric problem.
    # The precision parameter dictates the precision required by the solver. For example, entering 1.E-8 requires the
    # RMS of the residual to be less than 10−8. A fourth parameter, representing the depthof the problem in the
    # into-the-page direction for 2-D planarproblems, can also be specifiedfor planar problems.
    # A fifth parameter represents the minimum angle constraint sent to themesh generator. The sixth parameter
    # indicates the solutionfrom the previous time step to beused in time-transient problems. The seventh parameter
    # is the time step assumed for timetransient problems.

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
