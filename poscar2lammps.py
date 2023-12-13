import sys
import numpy as np
import ase.io.vasp
import ase.io.lammpsdata
from ase import Atoms
from ase.visualize import view
from ase import build

vasp_infile = str(sys.argv[1])
#Reads structure from .cif file and creates Atoms object
struc_input = ase.io.vasp.read_vasp(vasp_infile)
view(struc_input)

trans_mat = np.zeros((3,3))
print(trans_mat)
trans_mat[0][0] = 5
trans_mat[1][1] = 5
trans_mat[2][2] = 5
print(trans_mat)

#struc_scell = ase.build.make_supercell(struc_input,trans_mat)
#view(struc_scell)
ase.io.lammpsdata.write_lammps_data("data.structure",atoms=struc_input,units="metal")




