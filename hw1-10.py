import math

def maximum(array,motherNum,decostr):
    print(decostr+"First called: My level:"+str(motherNum+1))
    
    if len(array) == 1:
        print(decostr+"Return Self "+str(array[0]))
        return array[0]
    split = math.floor(len(array)/2)
    _decorStr = decostr + "\t"
    lMax = maximum(array[:split],motherNum+1,_decorStr)
    rMax = maximum(array[split:],motherNum+1,_decorStr)
    _str = decostr+"Retrive\tlMax: "+str(lMax)+"\trMax: "+str(rMax)
    print(_str)
    if lMax < rMax:
        print(decostr+"Return Right "+str(rMax))
        return rMax
    else:
        print(decostr+"Return Left "+str(lMax))
        return lMax

_array = [2,4,1,7,8,9,4]
print("final:",maximum(_array,0,""))