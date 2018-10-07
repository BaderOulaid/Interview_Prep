# worst case is n^2
# avg is nlogn
# depends on pivot selection (sorted or reverse sorted)
# good for arrays -> caching benefits

# quick sort works by selecting the pivot, iterating through the list
# divided by the pivot, and seeing if the item is less then the
# current number that is being looked at. the goal
# is to have the data to the left of the pivot
# be smaller, and the data to the right to be bigger.
# this is recrusively called until its sorted.

# compare numbers to pivot
import random

def quick_sort_driver(data):
    quick_sort(data, 0, len(data) - 1)


def quick_sort(data, low, hi):
    if low < hi:
        p = partition(data, low, hi)
        quick_sort(data, low, p - 1)  # items left
        quick_sort(data, p + 1, hi)  # items right


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(data, low, hi):
    pivot_index = get_pivot(data, low, hi)
    pivot_value = data[pivot_index]
    data[pivot_index], data[low] = data[low], data[pivot_index]

    border = low

    for element in range(low, hi + 1):
        if data[element] < pivot_value:
            border += 1
            data[element], data[border] = data[border], data[element]
    data[low], data[border] = data[border], data[low]

    return border


def get_pivot(data, low, hi):
    return random.randint(low,hi)





data = [54,26,93,17,77,31,44,55,20]
quick_sort_driver(data)
print data