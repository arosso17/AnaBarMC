import uproot
import particle

# Open the G4SBS root file and navigate to the tree containing the event data
myfile = uproot.open("new100.root")
mytree = myfile["h1"]

bfile = uproot.open("../batch/data/AnaBarMC_Gen_7001.root")
btree = bfile["h1"]

print("\nnew100:")
print(mytree.typenames())

print("\nAnaBarMC_Gen_7001:")
print(btree.typenames())

for branch in btree:
	print(branch.name)
	print(branch.array()[0])

'''
for branch in mytree:
	print()
	print()
	print(branch.name)
	print(branch.values())
	myx = mytree[branch.name].array()
	print("mine:")
	print(type(myx))
	print(myx[0])
	print(type(myx[0]))
	
	print()
	
	bx = btree[branch.name].array()
	print("his:")
	print(type(bx))
	print(bx[0])
	print(type(bx[0]))
'''
