import re

#open the data which contains the average income per zip
averageInc = open("ZIPIncomeData.txt", "r")

#and the data which contains the ratio of EMS calls per zip
EMSdata = open("yearRatioDict.txt", "r")

output = open("finalDataCoords.txt", "w")

#put all of the average incomes into a dictionary 
#with zip as key and average income as data
avgIncs = {}
INC = averageInc.readline()
while INC:
    split = INC.split("|")
    avgIncs[split[0]]=split[1][:-1]
    INC = averageInc.readline()

#go through all of the EMS data
#if the zip code is in the average income dictionary as well
#output average income | the ratio of EMS calls for that zip 
EMS = EMSdata.readline()
while EMS:
    split = EMS.split("|")
    if split[0] in avgIncs:
        output.write(avgIncs[split[0]]+"|"+split[1])
    EMS = EMSdata.readline()

output.close()
EMSdata.close()
averageInc.close()
