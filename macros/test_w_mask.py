import uproot
import particle
import numpy as np
import awkward as ak

# Open the G4SBS root file and navigate to the tree containing the event data
file = uproot.open("gep_12Gev100.root")
tree = file["T"]

# Get the arrays for the variables of interest
cdet_hit = tree["Earm.CDET_Scint.hit.nhits"].array()
pid = tree["SDTrack.PID"].array()
xpos = tree["SDTrack.posx"].array()
ypos = tree["SDTrack.posy"].array()
zpos = tree["SDTrack.posz"].array()
xmomentum = tree["SDTrack.momx"].array()
ymomentum = tree["SDTrack.momy"].array()
zmomentum = tree["SDTrack.momz"].array()
energy = tree["SDTrack.Etot"].array()

# Loop over each event in the tree
dat_for_tree = {"X_vtx": [], "Y_vtx": [], "Z_vtx": [], "Px_p": [], "Py_p": [], "Pz_p": [], "En_p": [], "Mass": [], "PDG": []}
for event_idx in range(len(cdet_hit)):
    # Loop over each hit in CDet for the current event
    for hit_idx in range(cdet_hit[event_idx]):
        # Get the index of the hit in the SDTrack arrays
        sdtrack_idx = tree["Earm.CDET_Scint.hit.sdtridx"].array()[event_idx][hit_idx]
        # Append the information for the current hit to the dictionary
        dat_for_tree["X_vtx"].append(np.float32(-ypos[event_idx][sdtrack_idx] * 100))
        dat_for_tree["Y_vtx"].append(np.float32(-zpos[event_idx][sdtrack_idx] * 100))
        dat_for_tree["Z_vtx"].append(np.float32(xpos[event_idx][sdtrack_idx] * 100))
        dat_for_tree["Px_p"].append(np.float32(-ymomentum[event_idx][sdtrack_idx] * 1000))
        dat_for_tree["Py_p"].append(np.float32(-zmomentum[event_idx][sdtrack_idx] * 1000))
        dat_for_tree["Pz_p"].append(np.float32(xmomentum[event_idx][sdtrack_idx] * 1000))
        dat_for_tree["En_p"].append(np.float32(energy[event_idx][sdtrack_idx] * 1000))
        dat_for_tree["Mass"].append(np.float32(particle.Particle.from_pdgid(pid[event_idx][sdtrack_idx]).mass))
        dat_for_tree["PDG"].append(pid[event_idx][sdtrack_idx])

# Create a new ROOT file with the extracted information
file = uproot.recreate("new100.root")
file["h1"] = dat_for_tree
file.close()

