
all: RatioEMSCallsVSIncome.pdf  #pdf of my scatter plot

clean:  #get rid of all the text and pdf files that are outputted by my code
	rm ZIPIncomeData.txt yearRatioDict.txt \
	finalDataCoords.txt RatioEMSCallsVSIncome.pdf
#this is the pdf that contains my final graph
#is created by createGraph.py and uses the pre-formatted data from finalDataCoords.txt
RatioEMSCallsVSIncome.pdf: finalDataCoords.txt createGraph.py
	python3 ./createGraph.py

#this is a pipe-delimited set of income and ratio of calls per zipcode
#it is created in createDataColumns.py
#and it takes as input the file with the ratio of calls per zip
#and the file with the average income per zip
finalDataCoords.txt: yearRatioDict.txt ZIPIncomeData.txt createDataColumns.py
	python3 ./createDataColumns.py

#this is a pipe-delimited file of zipcode to ratio of noncritical calls
#its created by the getYearRatio.py and takes as input the EMS data
yearRatioDict.txt: EMS_Incident_Dispatch_Data.tsv.gz getYearRatio.py
	python3 ./getYearRatio.py

#this is a pipe-delimited file of zipcode and average income for that zip
#its created by zipIncomeCalc.py and takes as input the IRS2018 data
ZIPIncomeData.txt: IRS2018.csv.gz zipIncomeCalc.py
	python3 ./zipIncomeCalc.py


