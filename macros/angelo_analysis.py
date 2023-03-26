import uproot
import particle
import numpy as np
import awkward as ak
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def one():
	# Open the G4SBS root file and navigate to the tree containing the event data
	file = uproot.open("gep_12Gev1mil.root")
	tree = file["T"]


	bb_angle = np.radians(29)
	bb_dist = 4.0735
	max_events = 100


	# Get the arrays for the variables of interest
	cdet_hit = tree["Earm.CDET_Scint.hit.nhits"].array()
	cdet_plane = tree["Earm.CDET_Scint.hit.plane"].array()
	cdet_row = tree["Earm.CDET_Scint.hit.row"].array()
	cdet_col = tree["Earm.CDET_Scint.hit.col"].array()
	cdet_cell = tree["Earm.CDET_Scint.hit.cell"].array()
	track_indexes = tree["Earm.CDET_Scint.hit.sdtridx"].array()
	pid = tree["SDTrack.PID"].array()
	xpos = tree["SDTrack.posx"].array()
	ypos = tree["SDTrack.posy"].array()
	zpos = tree["SDTrack.posz"].array()

	#xpos = tree["Earm.CDET_Scint.hit.xhitg"].array()
	#ypos = tree["Earm.CDET_Scint.hit.yhitg"].array()
	#zpos = tree["Earm.CDET_Scint.hit.zhitg"].array()

	xmomentum = tree["SDTrack.momx"].array()
	ymomentum = tree["SDTrack.momy"].array()
	zmomentum = tree["SDTrack.momz"].array()
	energy = tree["SDTrack.Etot"].array()

	dat_for_tree = {"X_vtx": [], "Y_vtx": [], "Z_vtx": [], "Px_p": [], "Py_p": [], "Pz_p": [], "En_p": [], "Mass": [], "PDG": []}
	for event in range(len(cdet_hit)):
		if len(dat_for_tree["X_vtx"]) > max_events:
			break
		for hit in range(cdet_hit[event]):
			if True: #cdet_plane[event][hit] == 2:
				track_idx = track_indexes[event][hit]
				#y_pos = -((zpos[event][track_idx] * np.cos(bb_angle) + xpos[event][track_idx] * np.sin(bb_angle)) - bb_dist) * 100
				#if y_pos < 20:
				#    print(cdet_plane[event][hit], cdet_row[event][hit], cdet_col[event][hit], cdet_cell[event][hit], y_pos)

				dat_for_tree["X_vtx"].append(xpos[event][track_idx])
				dat_for_tree["Y_vtx"].append(ypos[event][track_idx])
				dat_for_tree["Z_vtx"].append(zpos[event][track_idx])

				#dat_for_tree["X_vtx"].append(xpos[event][hit])
				#dat_for_tree["Y_vtx"].append(ypos[event][hit])
				#dat_for_tree["Z_vtx"].append(zpos[event][hit])

				dat_for_tree["Px_p"].append(xmomentum[event][track_idx])
				dat_for_tree["Py_p"].append(ymomentum[event][track_idx])
				dat_for_tree["Pz_p"].append(zmomentum[event][track_idx])
				dat_for_tree["En_p"].append(energy[event][track_idx])
				dat_for_tree["Mass"].append(particle.Particle.from_pdgid(pid[event][track_idx]).mass)
				dat_for_tree["PDG"].append(pid[event][track_idx])


	tx = np.array(dat_for_tree["Z_vtx"])
	ty = np.array(dat_for_tree["X_vtx"])
	txp = np.array(dat_for_tree["Pz_p"])
	typ = np.array(dat_for_tree["Px_p"])

	newx = -(-tx * np.sin(bb_angle) + ty * np.cos(bb_angle)) * 100
	newy = -((tx * np.cos(bb_angle) + ty * np.sin(bb_angle)) - bb_dist) * 100
	newz = -np.array(dat_for_tree["Y_vtx"]) * 100
	newxp = -(-txp * np.sin(bb_angle) + typ * np.cos(bb_angle))
	newyp = -(txp * np.cos(bb_angle) + typ * np.sin(bb_angle))
	newzp = -np.array(dat_for_tree["Py_p"])

	'''
	plt.hist2d(newx, newz, bins=50, cmap='Blues', range=[[-100, 125], [-200, 200]])

	plt.colorbar()

	plt.xlabel('X')
	plt.ylabel('Z')
	plt.title('CDet Hits')
	'''

	fig1, ax1 = plt.subplots()

	ax1.plot(newx,newz,'.')

	import matplotlib.patches as patches
	rect = patches.Rectangle((-45, -50), 100, 50, linewidth=1, edgecolor='r', facecolor='none')
	ax1.add_patch(rect)
	rect = patches.Rectangle((-45, 0), 100, 50, linewidth=1, edgecolor='r', facecolor='none')
	ax1.add_patch(rect)
	rect = patches.Rectangle((-30, -150), 100, 50, linewidth=1, edgecolor='r', facecolor='none')
	ax1.add_patch(rect)
	rect = patches.Rectangle((-30, 100), 100, 50, linewidth=1, edgecolor='r', facecolor='none')
	ax1.add_patch(rect)
	rect = patches.Rectangle((-38, -100), 100, 50, linewidth=1, edgecolor='r', facecolor='none')
	ax1.add_patch(rect)
	rect = patches.Rectangle((-38, 50), 100, 50, linewidth=1, edgecolor='r', facecolor='none')
	ax1.add_patch(rect)


	################# 3D stuff ############################
	#fig = plt.figure()
	#ax = fig.add_subplot(111, projection='3d')
	#ax.scatter(newx, newy, newz)
	#ax.scatter(dat_for_tree["X_vtx"], dat_for_tree["Y_vtx"], dat_for_tree["Z_vtx"])

	# Set the axis labels
	#ax.set_xlabel('X')
	#ax.set_ylabel('Y')
	#ax.set_zlabel('Z')

	#ax.set_ylim([22.3, 22.5])

	plt.show()

def two():
	file = uproot.open("../data/AnaBarMC_1000.root")
	tree = file["T"]

	# Get the arrays for the variables of interest
	hits = tree["Detector_Nhits"].array()
	photons = tree["PMT_Nphotons"].array()
	ed = tree["Detector_Ed"].array()
	detector_id = tree["Detector_id"].array()
	pmt_id = tree["PMT_id"].array()
	detector_pdg = tree["Detector_pdg"].array()
	primary_pdg = tree["Prim_pdg"].array()
	energy = tree["Prim_E"].array()
	theta = tree["Prim_Th"].array()
	phi = tree["Prim_Ph"].array()
	num_photons = []
	energy_dep = []
	for event_i in range(len(hits)):
		if sum(ed[event_i]) > 0:
			e = []
			for hit_i in range(hits[event_i]):
				mass = particle.Particle.from_pdgid(primary_pdg[event_i]).mass
				mom = np.sqrt(energy[event_i]*energy[event_i] - mass*mass)
				momy = mom*np.sin(theta[event_i])*np.sin(phi[event_i])
				new_theta = np.arccos(momy/mom)
				if detector_id[event_i][hit_i] >= 30000 and detector_id[event_i][hit_i] <= 32352 and detector_pdg[event_i][hit_i] == primary_pdg[event_i] and new_theta > 2.524:
				
					e.append(ed[event_i][hit_i])
			if sum(e) > 0:
				num_photons.append(sum(photons[event_i][: 2352]))
				energy_dep.append(sum(e))


	fig1, ax1 = plt.subplots()

	ax1.plot(energy_dep, num_photons,'.')
	energy_dep = np.array(energy_dep)
	num_photons = np.array(num_photons)
	print(len(energy_dep))
	coefficients = np.polyfit(energy_dep, num_photons, 1)
	m = coefficients[0]
	b = coefficients[1]
	print('Slope:', m)
	print('Intercept:', b)

	ax1.plot(energy_dep, m*energy_dep + b, color='red')

	plt.show()


if __name__ == "__main__":
	two()



