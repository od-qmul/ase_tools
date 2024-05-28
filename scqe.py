import sys
import ase.io.espresso
import numpy as np
from ase import Atoms
from ase.visualize import view
from ase import build
QE_infile = str(sys.argv[1])
print(QE_infile)
QE_infile_atoms = ase.io.espresso.read_espresso_in(QE_infile)

trans_mat = np.zeros((3,3))
print(trans_mat)
trans_mat[0][0] = int(sys.argv[2])
trans_mat[1][1] = int(sys.argv[3])
trans_mat[2][2] = int(sys.argv[4])
struc_scell = ase.build.make_supercell(QE_infile_atoms,trans_mat)

print("Converting %s to supercell" % (QE_infile))
print(trans_mat)
fout = open("sc_qe.in","w+")
ase.io.espresso.write_espresso_in(fout,atoms=struc_scell)


