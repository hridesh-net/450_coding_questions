def divide(arr, small, large):
    pivot = arr[large]
    
    index = small - 1
    
    for i in range(small, large):
        if arr[i] <= pivot:
            index = index + 1
            
            (arr[index], arr[i]) = (arr[i], arr[index])
    
    (arr[index + 1], arr[large]) = (arr[large], arr[index + 1])
    
    return index + 1


def quick_sort(arr, small, large):
    if small < large:
        pivot_index = divide(arr, small, large)
        
        quick_sort(arr, small, pivot_index - 1)
        
        quick_sort(arr, pivot_index + 1, large)


def quicksort(arr):
    quick_sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = []
    n = int(input("enter array range: "))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    
    quicksort(arr)
    
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()