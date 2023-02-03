import uproot
import awkward
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy

with uproot.open("test_out.root") as f:
	tree = f["T"]
	xdat = tree["Earm.BBGEM.hit.vx"].array()
	ydat = tree["Earm.BBGEM.hit.vy"].array()
	zdat = tree["Earm.BBGEM.hit.vz"].array()
	pdat = tree["Earm.BBGEM.hit.p"].array()
	ddat = tree["Earm.BBGEM.hit.edep"].array()
	piddat = tree["Earm.BBGEM.hit.pid"].array()

fig = plt.figure()

x = []
y = []
z = []
p = []
pid = []


for i in range(len(pdat)):
	for j in range(len(pdat[i])):
		x.append(xdat[i][j])
		y.append(ydat[i][j])
		z.append(zdat[i][j])
		p.append(pdat[i][j] - ddat[i][j])
		pid.append(piddat[i][j])


gs = fig.add_gridspec(2, 1, hspace=0, wspace=0)
axs = gs.subplots(sharex='col', sharey='row')
plts = axs.flat

(mu, sigma) = norm.fit(x)
n, bins, patches = plts[0].hist(x, 20, density=True, facecolor='green', alpha=0.75)
y = scipy.stats.norm.pdf(bins, mu, sigma)
plts[0].plot(bins, y, 'r', linewidth=2)
plts[0].set_yscale('log')


(mu, sigma) = norm.fit(p)
n, bins, patches = plts[1].hist(p, 20, density=True, facecolor='green', alpha=0.75)
y = scipy.stats.norm.pdf(bins, mu, sigma)
plts[1].plot(bins, y, 'r', linewidth=2)
plts[1].set_yscale("log")


plt.show()

