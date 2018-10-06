
# O(nlogn)

# We can divide a list in half log2 n times where n is the length of the list.
# The second process is the merge. Each item in the list will eventually be
# processed and placed on the sorted list. So the merge operation which results in a
# list of size n requires n operations. The result of this analysis is that log2 n
# splits, each of which costs n for a total of nlog2 n operations.

def merge(left, right):
    merged = []
    i, j = 0, 0 # i is left j is right

    print "merging", left, right

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1


    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    print i, j, merged

    return merged


def merge_sort(alist):
    print "merge sort", alist
    if len(alist) == 0 or len(alist) == 1:
        return alist
    else:
        midpoint = len(alist)//2
        left_half = merge_sort(alist[:midpoint])
        right_half = merge_sort(alist[midpoint:])

        return merge(left_half, right_half)




alist = [54,26,93,17,77,31,44,55,20]
print merge_sort(alist)
