import math as m
def BuildMaxHeap(array):
    for i in range(m.floor(len(array)/2),0,-1):
        MaxHeapify(array,i)
    return array

def MaxHeapify(array,pos):
    left = (pos+1)*2-1
    right = left+1
    big = pos
    if left <len(array) and array[left]>array[pos]:
        big = left
    if right <len(array) and array[right]>array[big]:
        big = right
    if big != pos:
        temp = array[pos]
        array[pos] = array[big]
        array[big] = temp
        MaxHeapify(array,big)
    return

def HeapExtractMax(array):
    ans = array[0]
    array[0] = array[-1]
    array.pop()
    MaxHeapify(array,0)
    return ans

def Parent(i):
    return m.floor((i+1)/2)-1

def HeapIncreaseKey(array,key):
    if key < array[-1]:
        return
    array[-1] = key
    i = len(array)-1
    while i >1 and array[Parent(i)]<array[i]:
        temp = array[Parent(i)]
        array[Parent(i)] = array[i]
        array[i] = temp
        i = Parent(i)
    return


def MaxHeapInsert(array,key):
    array.append(key-1)
    HeapIncreaseKey(array,key)
    return

arr = [27,6,2,19,0,17]
print("orginal: "+str(arr))
BuildMaxHeap(arr)
print("max-heap: "+str(arr))
largest = HeapExtractMax(arr)
print("largest: "+str(largest)+" => "+str(arr))
ins = 5
MaxHeapInsert(arr,ins)
print("insert "+str(ins)+" => "+str(arr))