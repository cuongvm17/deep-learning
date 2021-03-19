def buddleSort(arr):
    if isinstance(arr, list):
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp
        return arr

    return "Invalid input data"

def inserionSort(arr):
    if isinstance(arr, list):
        for i in range(1, len(arr)):
            j = i - 1
            current = arr[i]
            while j >= 0 and current < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
        return arr

    return "Invalid input data"


def divide(arr, start, end):
    if isinstance(arr, list):
        if start == end:
            return [arr[start]]
        else:
            middle = (start + end) // 2
            leftArr = divide(arr, start, middle)
            rightArr = divide(arr, middle + 1, end)

            return conquer(arr, leftArr, rightArr)

    print("Invalid input data")

def conquer(arr, leftArr, rightArr):
    newArr = []
    i = 0
    j = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            newArr.append(leftArr[i])
            i += 1
        else: 
            newArr.append(rightArr[j])
            j += 1
    if i < len(leftArr):
        newArr += leftArr[i:]
    if j < len(rightArr):
        newArr += rightArr[j:]
    
    return newArr

arr = [100, 20, 10, 16, 56, 44]
print("Input:", arr)

print("......")
print("==============================")

print("Start test bubble sort ...")
print("Algorithms complexity is O(n^2)")
print("Output:", buddleSort(arr))
print("==============================")

print("Start test for insertion sort ...")
print("Algorithms complexity is O(n^2)")
print("Output:", inserionSort(arr))
print("==============================")

print("Start test for merge sort ...")
print("Algorithms complexity is O(nlog(n))")
print("Output:", divide(arr, 0, len(arr) - 1))