def getlist(lists):
    finalList = []
    finalList.append(lists[0])
    for li in lists:
        i = 0
        while i+1 <len(finalList) and finalList[i] != li:
            i += 1 
        if finalList[i] != li:
            finalList.append(li)  
    return finalList

lists = ["a","b","c","c","d","e","f","g","h","a","b","c"]
print(lists)
print(getlist(lists))
