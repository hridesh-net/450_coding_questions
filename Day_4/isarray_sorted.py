def isarray_sorted(arr):
    if len(arr) <= 1:
        return True
    
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    
    return True


if __name__ == "__main__":
    arr = []
    n = int(input('enter size of array: '))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    
    bool = isarray_sorted(arr)
    print(bool)