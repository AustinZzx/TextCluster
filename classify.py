from DPSParser import *
from sklearnCluster import *

dpsc = DPSParser()
myDict = {}
myclassDict = {}
dictifyDescription(dpsc, myDict, myclassDict)
myclassInfo = []
myClassList = []
dicttolist(myclassDict, myclassInfo, myClassList)

case = input("Please enter your case: ")
N = int(input("How many suggestions do you like to see: "))
result = classify(case, myclassInfo, N)
"""print(result)
print(type(result))
print(type(result[0]))
"""
for index in result:
	print(myClassList[index])