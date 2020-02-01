#!/usr/bin/python3
import math   

class allTime:
    def __init__(self,time,timeName):
        self.timeName = timeName
        self.time = time
        self.maxRunTime = 1
    def __str__(self):
        ret = self.timeName+": "+str(self.maxRunTime)
        return ret


hour = 3600
day = hour * 24
month = day * 31
year = day * 366
century = year * 100
# currentT = [allTime(1,"1 sec"),allTime(60,"1 min"),allTime(3600,"1 hour")] 
currentT = [allTime(1,"1 sec"),allTime(60,"1 min"),allTime(hour,"1 hour"),allTime(day,"1 day"),allTime(month,"1 month"),allTime(year,"1 year"),allTime(century,"1 century")] 

for cT in currentT:
    _a = cT.time/pow(10,-6)
    _b = 0
    while _a/10 >= 1:
        _a /= 10
        _b += 1
    print(cT.timeName+" => "+str(_a)+"*10^"+str(_b))

print("\nn^2")
for cT in currentT:
    maxT= cT.time/pow(10,-6)
    ansT = 1
    while pow(ansT+1,2) <= maxT:
        ansT += 1
    cT.maxRunTime = ansT
    print(cT)

print("\nn^3")
for cT in currentT:
    maxT= cT.time/pow(10,-6)
    ansT = 1
    while pow(ansT+1,3) <= maxT:
        ansT += 1
    cT.maxRunTime = ansT
    print(cT)

print("\n2^n")
for cT in currentT:
    maxT= cT.time/pow(10,-6)
    ansT = 1
    while pow(2,ansT+1) <= maxT:
        ansT += 1
    cT.maxRunTime = ansT
    print(cT)