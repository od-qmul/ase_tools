import sys
from ase import io
import ase.io.cif
import ase.io.espresso
from ase import Atoms
from ase.visualize import view
cif_infile = str(sys.argv[1])
print(cif_infile)
#Reads structure from .cif file and creates Atoms object. Sometimes a newline is required after the citation section ;
struc_input = ase.io.read(cif_infile)
view(struc_input)
fo = open("qe_struc.data","w+")
focrys = open("qe_struc_crys.data","w+")
ase.io.espresso.write_espresso_in(fo,atoms=struc_input)
ase.io.espresso.write_espresso_in(focrys,atoms=struc_input,crystal_coordinates=True)
