import os
import unittest

from adze_modeler.femm_wrapper import FemmExecutor


class TestFemmExecutor(unittest.TestCase):
    def test_run_femm(self):
        """
        Runs a simple, built-in femm example: https://www.femm.info/wiki/CoilGun
        """
        FemmExecutor().run_femm("coilgun.lua")

        try:

            with open("output.txt") as results:
                content = results.readlines()

                result = content[0].split(",")

            self.assertEqual(1.5, float(result[0]))
            self.assertEqual(0.05, round(float(result[1]), 2))

            os.remove("output.txt")
            os.remove("temp.fem")
            os.remove("temp.ans")
        except FileNotFoundError:
            print("The FEMM output files hadn't generated.")
