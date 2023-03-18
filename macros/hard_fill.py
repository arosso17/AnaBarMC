import uproot
import particle
import numpy as np
import awkward as ak

# Loop over each event in the tree
dat_for_tree = {"X_vtx": [-2.0079112 for _ in range(100)], "Y_vtx": [25.0 for _ in range(100)], "Z_vtx": [-145.18832 for _ in range(100)], "Px_p": [103.960754 for _ in range(100)], "Py_p": [-3303.7065 for _ in range(100)], "Pz_p": [-0.16867667 for _ in range(100)], "En_p": [3307.03 for _ in range(100)], "Mass": [105.658 for _ in range(100)], "PDG": [13 for _ in range(100)]}

# Create a new ROOT file with the extracted information
file = uproot.recreate("hard100.root")
file["h1"] = dat_for_tree
file.close()

