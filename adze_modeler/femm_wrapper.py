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
