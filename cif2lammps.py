import sys
from ase import io
import ase.io.cif
import ase.io.lammpsdata
from ase import Atoms
from ase.visualize import view
#Reads structure from .cif file and creates Atoms object. Sometimes a newline is required after the citation section ;
struc_input = io.read("ICSD_CollCode9161.cif")
view(struc_input)
fo = open("lammps_struc.data","w+")
ase.io.lammpsdata.write_lammps_data(fo,atoms=struc_input,units="metal")
