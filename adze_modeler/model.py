from abc import abstractmethod, ABCMeta
from adze_modeler.geometry import Geometry
from types import SimpleNamespace


class Model(metaclass=ABCMeta):
    """This class contains the full model = geometry + boundary conditions + material parameters """

    def __init__(self):
        self.geometry = Geometry
        self.materials = []
        self.labels = []
        self.bcs = []
        self.epsilon = 1.e-5

    @abstractmethod
    def create_model(self):
        pass


class PhysicalModel():
    materials = []
    boundary_conditions = []


class Label(SimpleNamespace):

    def __init__(self, node_id, label_id, material):
        self.node_id = node_id
        self.label_id = label_id
        self.material = material


class Material(SimpleNamespace):
    pass


class FemObjects(SimpleNamespace):
    @abstractmethod
    def write_geometry(self):
        pass


class Rectangle(FemObjects):

    def __init__(self, bottom_left: tuple, width, height, material):
        self.width = width
        self.height = height
        self.material = material


class BoundaryCondition(SimpleNamespace):

    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value


if __name__ == "__main__":
    cu = Material(name="copper", mu_x=1, mu_y=1, Hc=0, J=1e6, C_duct=0, L_amd=0, Phi_hmax=0, lam_fill=1., Phi_hx=0,
                  Phi_hy=0., N_strands=1., WireD=1.)

    print(cu)
    # mi_addmaterial("materialname", mux, muy, Hc, J, Cduct, Lamd, Phihmax,lamfill, LamType, Phihx, Phihy,NStrands,WireD)
