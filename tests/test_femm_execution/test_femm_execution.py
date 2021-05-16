import unittest
import os
from adze_modeler.femm_wrapper import FemmExecutor


class TestFemmExecutor(unittest.TestCase):

    def test_run_femm(self):
        """
        Runs a simple, built-in femm example: https://www.femm.info/wiki/CoilGun
        """
        FemmExecutor().run_femm('coilgun.lua')

        with open('output.txt', 'r') as results:
            content = results.readlines()

            result = content[0].split(',')

        self.assertEqual(1.5, float(result[0]))
        self.assertEqual(0.05, round(float(result[1]), 2))

        try:
            os.remove('output.txt')
            os.remove('temp.fem')
            os.remove('temp.ans')
        except FileExistsError:
            print("The FEMM output files hadn't generated.")
