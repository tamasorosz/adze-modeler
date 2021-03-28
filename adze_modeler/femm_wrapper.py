"""
The goal of this module is to write out the given geometry into a FEMM's lua script.
The code generated one snapshot from the created model, which can be run during the Optimization.
"""

from adze_modeler.geometry import Geometry


class FemmWriter():

    def write(self, model, file_name):
        """ Generate a runnable lua-script for a FEMM calculation.

        :param model: represents a geometry in the adze-modeler
        :param file_name: the code (re)writes the snapshot from the created geometry to the given code
        """

        with open(file_name, 'w') as writer:
            ...



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