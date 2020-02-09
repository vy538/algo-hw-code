import math 

def getlist(lists):
    if len(lists) == 0:
        return "no lists"
    finalList = []
    finalList.append(lists[0])
    for li in lists:
        i = 0
        while i+1 <len(finalList) and finalList[i] != li:
            i += 1 
        if finalList[i] != li:
            finalList.append(li)  
    return finalList

def getListRec(lists):
    def mergeList(l1,l2):
        finList = []
        for _l1 in l1:
            j = 0
            while j < len(l2):
                if _l1 == l2[j]:
                    l2.remove(l2[j])
                else:
                    j += 1
            finList.append(_l1)
        finList += l2
        return finList
    if len(lists) <= 1:
       return lists
    split = math.floor(len(lists)/2)
    list1 = getListRec(lists[:split])
    list2 = getListRec(lists[split:])
    finalList = mergeList(list1,list2)
    return finalList
    
lists = ["a","b","c","c","d","e","f","g","h","a","b","c"]
print(lists)
l_non = getlist(lists)
print(l_non)
l_rec = getListRec(lists)
print(l_rec)
