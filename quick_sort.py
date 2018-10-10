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







# the idea of quick sort, is to pick a pivot. put everything
# that is less then the pivot to the left, and greater to the right. and
# recursively call on the left and right until sorted.
# in addition to the pivot, there is a value that i'll call
# the border value

# pick a pivot
# partition : re order the array so left is < and right is >
# recursively apply to sub arrays until size of one.





def quick_sort_driver_adam(data):
    quick_adam(data, 0, len(data) - 1)

def quick_adam(data, low, hi):
    if low < hi:
        p = partition_adam(data, low, hi)
        quick_adam(data, low, p - 1)
        quick_adam(data, p + 1, hi)

def partition_adam(data, low, hi):
    pivot_index = random.randint(low, hi)

    pivot_value = data[pivot_index]

    data[pivot_index], data[low] = data[low], data[pivot_index]
    border_index = low

    for element in range(low, hi):
        if data[element] < pivot_value:
            border_index += 1
            # swap the element with the element to the right of the border
            data[element], data[border_index] = data[border_index], data[element]
    data[low], data[border_index] = data[border_index], data[low]
    return border_index


data = [54,26,93,17,77,31,44,55,20]
quick_sort_driver_adam(data)
print data