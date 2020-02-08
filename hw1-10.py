import math

def maximum(array,motherNum,decostr):
    print(decostr+"First called level:"+str(motherNum+1)+"\t"+str(array))
    if len(array) == 1:
        print(decostr+"Return Self "+str(array[0]))
        return array[0],1
    split = math.floor(len(array)/2)
    _decorStr = decostr + "\t"
    lMax,lRun = maximum(array[:split],motherNum+1,_decorStr)
    rMax,rRun = maximum(array[split:],motherNum+1,_decorStr)
    _str = decostr+"Retrive\tlMax: "+str(lMax)+"\trMax: "+str(rMax)
    totalRuntime = lRun+rRun
    print(_str)
    if lMax < rMax:
        print(decostr+"Return Right "+str(rMax)+"\tTotal RunTime: "+str(totalRuntime))
        return rMax,totalRuntime
    else:
        print(decostr+"Return Left "+str(lMax)+"\tTotal RunTime: "+str(totalRuntime))
        return lMax, totalRuntime

_array = [10, 8, 6, 4, 2, 0]
_max,_rt = maximum(_array,0,"")
print("final:",_max,_rt)