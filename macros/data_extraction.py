import uproot
import awkward
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy

with uproot.open("gep_12GeV2.root") as f:
	tree = f["T"]
	sdtrid = tree["Earm.CDET_Scint.hit.sdtridx"].array()
	testz = tree["Earm.CDET_Scint.hit.zhitg"].array()
	zvert = tree["SDTrack.vz"].array()
	PID = tree["SDTrack.PID"].array()
	TID = tree["SDTrack.TID"].array()
	posx = tree["SDTrack.posx"].array()
	posy = tree["SDTrack.posy"].array()
	posz = tree["SDTrack.posz"].array()
	momx = tree["SDTrack.momx"].array()
	momy = tree["SDTrack.momy"].array()
	momz = tree["SDTrack.momz"].array()
	etot = tree["SDTrack.Etot"].array()

dat_for_tree = {"X_vtx":[], "Y_vtx":[], "Z_vtx":[], "Px_p":[], "Py_p":[], "Pz_p":[], "En_p":[], "PDG":[]}

#for eventi in range(len(sdtrid)):
#	print(posx[sdtrid[eventi]])

for event in range(len(sdtrid)):
	for index in set(sdtrid[event]):
		# need to translate into the coordinate frame (and units) of the CDet simulation
		dat_for_tree["X_vtx"].append(-posy[event][index] * 100)
		dat_for_tree["Y_vtx"].append(-(posz[event][index] - 4.5) * 100)
		dat_for_tree["Z_vtx"].append(posx[event][index] * 100)
		dat_for_tree["Px_p"].append(-momy[event][index] * 1000)
		dat_for_tree["Py_p"].append(-momz[event][index] * 1000)
		dat_for_tree["Pz_p"].append(momx[event][index] * 1000)
		dat_for_tree["En_p"].append(etot[event][index] * 1000)
		dat_for_tree["PDG"].append(PID[event][index])

'''print(dat_for_tree["X_vtx"][0], dat_for_tree["Y_vtx"][0], dat_for_tree["Z_vtx"][0], dat_for_tree["Px_p"][0], dat_for_tree["Py_p"][0], dat_for_tree["Pz_p"][0], dat_for_tree["En_p"][0], dat_for_tree["PDG"][0])
print(dat_for_tree["X_vtx"][13], dat_for_tree["Y_vtx"][13], dat_for_tree["Z_vtx"][13], dat_for_tree["Px_p"][13], dat_for_tree["Py_p"][13], dat_for_tree["Pz_p"][13], dat_for_tree["En_p"][13], dat_for_tree["PDG"][13])'''


file = uproot.recreate("proccessed_demonstration.root")
file["h1"] = dat_for_tree
file.close()



'''for i in range(len(TID)):
	for j in range(len(TID[i])):
		if TID[i][j]:
			x.append(posx[i][j])
			y.append(posy[i][j])
			z.append(posz[i][j])
			px.append(momx[i][j])
			py.append(momy[i][j])
			px.append(momz[i][j])
			e.append(etot[i][j])
			pid.append(PID[i][j])
			cdettid.append(sdtrid[i][j])

print(len(cdettid))

pids = {}
print(len(pid))
print(pid[0])

for id in pid:
	if id not in pids:
		pids[id] = 1
	else:
		pids[id] += 1

print(pids)'''


'''fig = plt.figure()
gs = fig.add_gridspec(2, 1, hspace=0, wspace=0)
axs = gs.subplots(sharex='col', sharey='row')
plts = axs.flat

(mu, sigma) = norm.fit(x)
n, bins, patches = plts[0].hist(x, 20, density=True, facecolor='green', alpha=0.75)
y = scipy.stats.norm.pdf(bins, mu, sigma)
plts[0].plot(bins, y, 'r', linewidth=2)
plts[0].set_yscale('log')


(mu, sigma) = norm.fit(e)
n, bins, patches = plts[1].hist(e, 20, density=True, facecolor='green', alpha=0.75)
y = scipy.stats.norm.pdf(bins, mu, sigma)
plts[1].plot(bins, y, 'r', linewidth=2)
plts[1].set_yscale("log")


plt.show()'''

