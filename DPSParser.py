class DPSCase:
    def __init__(self, casenbr, information, ccClass, ccDescription):
        self.casenbr = casenbr
        self.information = information
        self.ccClass = ccClass
        self.ccDescription = ccDescription


def DPSParser():
    with open("DPS_text.txt","r") as fileob:
        resultlist = []
        for line in fileob:
            casetext = line.split(';')
            if casetext[0] and casetext[2] and casetext[3] and len(casetext[1])>2:
                resultlist.append(DPSCase(casetext[0], casetext[1], casetext[2], casetext[3]))
    return resultlist
