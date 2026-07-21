# def linear_search(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return -1

# p = int(input("Enter the number of elements in the array: "))
# arr = []

# for i in range(p):
#     n = int(input("Enter the element: "))
#     arr.append(n)

# target = int(input("Enter the element to search: "))

# result = linear_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")



# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2

#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         # Merge the two halves
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         # Copy remaining elements of left
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         # Copy remaining elements of right
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1


# p = int(input("Enter the number of elements: "))
# arr = []

# for i in range(p):
#     n = int(input("Enter element: "))
#     arr.append(n)

# merge_sort(arr)

# print("Sorted array:", arr)



def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left    
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


p = int(input("Enter the number of elements: "))
arr = []
for i in range(p):
    n = int(input("Enter element: "))
    arr.append(n)
heap_sort(arr)
print("Sorted array:", arr)

