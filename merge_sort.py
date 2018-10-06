
# O(nlogn)



def merge(left, right):
    merged = []

    print "merging", left, right
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])


    if len(left) == 0:
        print "left == 0" , right
        merged += right
    else:
        print "right == 0", left
        merged += left

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
