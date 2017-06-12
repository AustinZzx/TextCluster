from DPSParser import *
from sklearnCluster import *

dpsc = DPSParser()
simlist = []

newcase = input("Please enter your case: ")

for case in dpsc:
	simlist.append(get_similarity(newcase, case.information))

resultlist = sorted(range(len(simlist)), key=lambda i: simlist[i], reverse=True)[:5]

print("Top five similar case:")
for i in range(len(resultlist)):
	index = resultlist[i]
	print("No. ", i+1, ": ", dpsc[index].information, "\nsimilarity: ", simlist[index], sep="")