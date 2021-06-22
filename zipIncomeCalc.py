import re
import gzip

#import file with IRS data    
IRS = gzip.open("IRS2018.csv.gz", "rt")
output = open("ZIPIncomeData.txt", "w")

#makes a dict that will decide the average income for each zip code
zip_AGI = {}


#read in all the IRS data
info =  IRS.read()

#keeps track of the current zip
zipCode = "00000"

#keeps track of total made in each zip
total = 0

#records number of returns per zip-- used to computer average income per zip
numReturns = 0     

#go through all of the AGI zip data
if info:
    NY = re.findall(r'..,(NY,[0-9]+,[0-9],[^,]+).+', info)
    for area in NY:
        fields = area.split(",")
        fields[3] = int(fields[3][:-5])
        
        #if its the first line of a new zip code (and not the first zipCode)
        #save the average from the previous zip code
        if fields[1]!= zipCode:
           zip_AGI[zipCode] = (total/numReturns)

           #get the new zipcode
           zipCode = fields[1]

           #and reset the variable counters
           total, numReturns = 0, 0
                  
        #check which category income the line belongs in
        #and add the median of that field multiplied by the number
        #of returns for that field to the total
        #add number of returns to total numReturns for this zip
        if fields[2] =="1":
            total += 12500*fields[3]
            numReturns += fields[3]
        elif fields[2] == "2":
            total += 37500*fields[3]
            numReturns += fields[3]
        elif fields[2] == "3":
            numReturns += fields[3]
            total += 62500*fields[3]
        elif fields[2] =="4":
            total += 87500*fields[3]
            numReturns += fields[3]
        elif fields[1] == "5":
            total += 150000*fields[3]
        else:
            total += 300000*fields[3]
     



#output a concatonation of the zipCode|
#and the computed average income for that zip
for a in zip_AGI:
    out = (a+"|"+str(zip_AGI[a]))
    output.write(out)
    output.write("\n")
