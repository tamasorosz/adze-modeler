from unittest import TestCase
from artapsegment.dxf_handlers import import_dxf
from importlib_resources import files


class TestDXFImport(TestCase):

    def test_owl_import_to_geometry(self):
        eml = files('examples.electrical_machine').joinpath('Prius2004_Rotor.dxf')
        print(eml)
        geo = import_dxf(eml.as_posix())
        print(geo)