if __name__ == "__main__":
    arr = []
    n = int(input('enter size of array: '))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    
    second = largest = -2147483648
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
    for i in range(len(arr)):
        if arr[i] > second and arr[i] != largest:
            second = arr[i]
    
    print('second largest in the array is: ', second)