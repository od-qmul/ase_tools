import sys
import ase.io
from ase import Atoms
from ase.visualize import view
from ase.calculators.espresso import Espresso
#Reads structure from .cif file and creates Atoms object
struc_input = ase.io.read("ICSD_CollCode153941.cif")
print(struc_input)
#Defines the pseudopotentials for the atoms
pseudopotentials = {'Ti': 'Ti.pbe-spn-kjpaw_psl.1.0.0.UPF',
                    'O': 'O.pbe-n-kjpaw_psl.1.0.0.UPF'}
#Defines the QE input parameters
input_params = {"ecutwfc" : 60, # The plane-wave wave-function cutoff
               "ecutrho": 240, # The density wave-function cutoff,
               "conv_thr": 1e-6, # The convergence for the DFT self-consistency
               "pseudo_dir" : "/home/ubc_oadicks/pslibrary.1.0.0/pbe/PSEUDOPOTENTIALS/", # The directory of the pseudo potentials
               }
#Sets up calc
calc = Espresso(input_data=input_params,pseudopotentials=pseudopotentials,
                tstress=True, tprnfor=True, kpts=(3, 3, 3))
struc_input.calc = calc
#Actually performs the calculation to retrieve the potential energy
en = struc_input.get_potential_energy()
