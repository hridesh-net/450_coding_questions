def binary_search(arr, l, r, k):
    if r >= 1:
        mid = l + (r - 1) // 2
        
        if arr[mid] == k:
            return mid
        
        elif arr[mid] > k:
            return binary_search(arr, l, mid - 1, k)
        
        else:
            return binary_search(arr, mid + 1, r, k)
    else:
        return -1


if __name__ == "__main__":
    arr = []
    n = int(input('enter size of array: '))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    
    k = int(input('enter element which needs to be find: '))
    binary_search(arr, 0, len(arr) - 1, k)