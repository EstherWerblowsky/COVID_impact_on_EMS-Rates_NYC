import re
import gzip

#import file with NYCEMS data
EMS = gzip.open("EMS_Incident_Dispatch_Data.tsv.gz", "rt")
output = open("yearRatioDict.txt", "w")

#make 2 dicts for each year                                                                                                                               
#hold the number of calls for specified symptoms                                                                                                          #for each zipcode                                                                                                                                        
EMS19 = {}
EMS20 = {}


#regexes needed in the code                                                                                                                               
d20 = re.compile(r'0[4-5]/../2020')
d19 = re.compile(r'0[4-5]/../2019')
symp = re.compile(r'ARREFC|ARREFT|ARREST|ASTHFC|ASTHFT|ASTHMA|ASTHMB|BACKPN|BITE|BLEED|BURN|BURNMI|CARD|CARDC|EYEINJ|GYN|GYNHEM|GYNMAJ|GYNMIN|HDACHE|HEAD\
PN|HEART|HEARTC|HEAT|INJMIN|INJURY|INTBLD')

                                                                                          
lEMS = EMS.readline()

#create a total for number of relevant calls per zipcode
#within the specified time and date
while lEMS:

    #split on tab                                                                                                                                         
    sub = lEMS.split("\t")

    #check if the line fits into either dictionary
    #if so, make the zipcode the key and add one to the data

    #check if it has appropriate symptoms and is within date in 2020
    if re.search(symp, sub[2]) and re.search(d20, sub[1]):
        if sub[21] and not sub[21] in  EMS20:
            
            #only working with valid entries
            try: EMS20[sub[21]] =1
            except: pass

        else:
            try: EMS20[sub[21]] +=1
            except: pass

    #check it has appropriate symptoms and is within date in 2019
    elif re.search(d19, sub[1]) and re.search(symp, sub[2]):
        if sub[21] and not sub[21] in EMS19:
            try: EMS19[sub[21]] =1 
            except: pass
        else:
            try: EMS19[sub[21]] +=1
            except: pass
            
    lEMS = EMS.readline()


#output the data as a concatnation of the zip code|
#with the ratio of calls in 2020 to 2019
for d in EMS20:
    #make sure that we count for discrepencies in the zipcodes
    #betweent the EMS and IRS data
    if d in EMS20 and d in EMS19:
        out = (d +"|"+str(EMS20[d]/EMS19[d]))
        output.write(out)
        output.write("\n")

output.close()
EMS.close()
