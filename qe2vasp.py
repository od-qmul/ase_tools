import sys
import ase.io.espresso
import ase.io.vasp
QE_infile = str(sys.argv[1])
print(QE_infile)
QE_infile_atoms = ase.io.espresso.read_espresso_in(QE_infile)
print("Converting %s to POSCAR" % (QE_infile))
fout = open("POSCAR","w+")
#ase.io.vasp.write_vasp("POSCAR",atoms = QE_infile_atoms)
ase.io.vasp.write_vasp(fout,atoms = QE_infile_atoms)
