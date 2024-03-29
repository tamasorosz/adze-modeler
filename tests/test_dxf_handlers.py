from unittest import TestCase

from adze_modeler.dxf_handlers import import_dxf
from importlib_resources import files


class TestDXFImport(TestCase):
    def test_dxf_import_to_geometry(self):
        eml = files("examples.motor").joinpath("motor_geometry.dxf")
        print(eml)
        geo = import_dxf(eml.as_posix())
        print(geo)
