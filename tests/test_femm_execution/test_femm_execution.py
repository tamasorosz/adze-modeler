import unittest

from adze_modeler.femm_wrapper import FemmExecutor


class TestFemmExecutor(unittest.TestCase):

    def test_run_femm(self):
        """
        Runs a simple, built-in femm example: https://www.femm.info/wiki/CoilGun
        """
        FemmExecutor().run_femm('coilgun.lua')
