from ase import io
import sys

name_infile = str(sys.argv[1])
dl_infile = io.read(name_infile,format='dlp4')
print(dl_infile)
print("Converting %s to REVCON.xyz" % (name_infile))
io.write("REVCON.xyz",images = dl_infile, format='extxyz')