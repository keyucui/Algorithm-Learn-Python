#encoding=utf-8
#递归实现快速排序

def quickSort(arr, firstIndex, lastIndex):
    if firstIndex >= lastIndex:
        return
    else:
        divIndex = Partition(arr, firstIndex, lastIndex)
        quickSort(arr, firstIndex, divIndex)
        quickSort(arr, divIndex + 1, lastIndex)

def Partition(arr, firstIndex, lastIndex):
    print arr
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i

arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]

print "initial array:\n", arr
quickSort(arr, 0, len(arr) - 1)
print "result array:\n", arr
