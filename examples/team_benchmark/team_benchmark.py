from adze_modeler.geometry import Geometry
from adze_modeler.model import Model, Material, Label


if __name__ == "__main__":
    cu = Material(
        name="copper",
        mu_x=1,
        mu_y=1,
        Hc=0,
        J=1e6,
        C_duct=0,
        L_amd=0,
        Phi_hmax=0,
        lam_fill=1.0,
        Phi_hx=0,
        Phi_hy=0.0,
        N_strands=1.0,
        WireD=1.0,
    )

    print(cu)
