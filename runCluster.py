from DPSParser import *
from sklearnCluster import *


dpsc = DPSParser()
myDict = {}
myclassDict = {}
dictify(dpsc, myDict, myclassDict)
myclassInfo = []
myClassList = []
dicttolist(myclassDict, myclassInfo, myClassList)

nclusters= 6
clusters = cluster_classes(myclassInfo, nclusters)
for cluster in range(nclusters):
    print("cluster "+str(cluster)+":")
    for i,sentence in enumerate(clusters[cluster]):
        print("\tclass "+str(i)+": "+myClassList[sentence])

"""
output should be:
cluster 0:
        class 0: SERVICE
        class 1: ALCOHOL
        class 2: PROPERTY
        class 3: TRAFFIC
        class 4: VEHICLE CODE
        class 5: HOMICIDE
        class 6: EH&S
        class 7: ASSAULT
        class 8: SUICIDE
        class 9: DEATH
        class 10: OFFICER STATUS
cluster 1:
        class 0: FRAUD
        class 1: THEFT-GRAND PERSON
        class 2: ROBBERY
        class 3: IDENTITY THEFT
        class 4: THEFT-TRICK
        class 5: KIDNAPPING
        class 6: FALSE PERSONATION
cluster 2:
        class 0: THEFT-PETTY
        class 1: BURGLARY-MOTOR VEHICLE
        class 2: THEFT-GRAND
        class 3: THEFT-GRAND AUTO
        class 4: ADMINISTRATIVE
        class 5: BURGLARY
        class 6: THEFT-MOTOR VEHICLE
cluster 3:
        class 0: BATTERY
        class 1: LA MUNICIPAL CODE
        class 2: DISTURBANCE
        class 3: CRIMINAL THREATS
        class 4: SEX OFFENSE
        class 5: OBSCENE ACTIVITY
        class 6: DOMESTIC VIOLENCE
        class 7: HARASSMENT
        class 8: EXTORTION
        class 9: INCIDENT
        class 10: THEFT-ACCESS
        class 11: ASSAULT-OTHER
        class 12: HEALTH & SAFETY
        class 13: HATE INCIDENT
cluster 4:
        class 0: FIRE
        class 1: ALARM RESPONSE
        class 2: ARSON
cluster 5:
        class 0: VANDALISM
        class 1: WARRANT
        class 2: DISORDERLY CONDUCT
        class 3: WEAPONS
        class 4: NARCOTICS
        class 5: TRESPASS
        class 6: BURGLARY-OTHER
        class 7: CHILD NEGLECT
        class 8: THEFT-FRAUD
        class 9: HOMELAND SECURITY
        class 10: FIELD INTERVIEW
        class 11: HOSPITAL
"""