def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            print('index of k element is: ', i)
            break
         

if __name__ == "__main__":
    arr = []
    n = int(input('enter size of array: '))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    
    k = int(input('enter element which needs to be find: '))
    linear_search(arr, k)