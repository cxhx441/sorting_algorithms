# TODO try implementing in place https://www.youtube.com/watch?v=Hoixgm4-P4M
def median_of_three(arr, low, high):
    mid = low + (high - low) // 2
    sorted_three = sorted([arr[low], arr[mid], arr[high]])
    arr[low], arr[mid], arr[high] = sorted_three
    return mid
def quick_sort_in_place(arr):
    def helper(left, right):
        if left >= right:
            return
        i = left
        j = right
        # pivot = ((j-i) // 2) + i
        pivot = median_of_three(arr, left, right)
        # swap element at pivot and end, to get it out of the way
        arr[pivot], arr[j] = arr[j], arr[pivot]
        pivot = j
        j -= 1 # i, j are the left, right of unsorted section.
        while i < j:
            if arr[i] <= arr[pivot]:
                i += 1
            elif arr[j] > arr[pivot]:
                j -= 1
            else:
                # swap element at left and right
                arr[i], arr[j] = arr[j], arr[i]

        # left and right are on same index
        # if arr[pivot] < arr[left], swap
        if arr[pivot] < arr[i]:
            arr[pivot], arr[i] = arr[i], arr[pivot]
            pivot = i
            helper(left, pivot-1)
            helper(pivot+1, right)
        else:
            helper(left, pivot-1)

    helper(0, len(arr)-1)
    return arr

# arr = [7, 3, 1, 4, 2, 6, 5]
# arr = [5, 4, 3, 2, 1]
# arr = [0, 0, 0, 0, 0]
# arr = [1, 2, 3, 4, 5]
# arr = [-1, -2, -3, -4, -5]
# arr = [100, -2, 40, -800, 1]
# arr = [10, 100, 5, 200, 1]
# print(arr)
# quick_sort_in_place(arr)
# print(arr)


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    # pivot = len(arr)//2
    pivot = median_of_three(arr, 0, len(arr)-1)
    below, above = [], []
    for i in range(len(arr)):
        if i == pivot:
            continue

        if arr[i] <= arr[pivot]:
            below.append(arr[i])
        else:
            above.append(arr[i])

    return quick_sort(below) + [arr[pivot]] + quick_sort(above)

def quick_sort_iterative_in_place(arr):
    pass
