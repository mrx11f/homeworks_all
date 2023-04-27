def binary_search(search_element, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == search_element:
            print(f"{search_element} found at index {mid}")
            return
        elif arr[mid] < search_element:
            left = mid + 1
        else:
            right = mid - 1
    print(f"{search_element} not found in the list")
arr = [2, 3, 5, 6, 8, 10, 12, 15]
binary_search(85, arr)



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [64, 25, 12, 22, 11, 29, 98]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                return arr