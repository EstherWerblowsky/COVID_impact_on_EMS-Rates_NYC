import matplotlib.pyplot as plt
import math
import random

N= 20
data = open("finalDataCoords.txt")
incomes, callRatios= [], []

line = data.readline()
while line:
    fields = line.split("|")
    incomes.append(float(fields[0]))
    callRatios.append(float(fields[1][:-1]))
    line = data.readline()

print(incomes)
print(callRatios)
f = plt.figure(figsize = (10,5) )

colors = [random.random() for i in range(len(incomes))]
areas = [math.pi * random.random() *50 for i in range(len(incomes))]

plt.scatter(incomes, callRatios, c= colors, s= areas, alpha = 0.5)
plt.ylim(0.0, 1.7)
plt.xlim(0.0, 400000)
plt.xlabel("Average Incomes")
plt.ylabel("Ratio EMS calls 2020:2019")
plt.title("Ratio of Non-Criical EMS calls in 2020 vs 2019 According to Average Income")

f.savefig("RatioEMSCallsVSIncome.pdf")
