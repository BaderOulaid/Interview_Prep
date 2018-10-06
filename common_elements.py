# Implement your function below.
# o(m+n) and sorted
def common_elements(list1, list2):


    index_one = 0
    index_two = 0
    result = []

    while index_one < len(list1) and index_two < len(list2):
        if list1[index_one] < list2[index_two]:
            # increment one
            index_one += 1

        elif list1[index_one] > list2[index_two]:
            # increment other
            index_two += 1
        else:
            # increment both
            #add to result
            result.append(list1[index_one])
            index_one += 1
            index_two += 1
    print result
    return result


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
common_elements(list_a1, list_a2) #should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
common_elements(list_b1, list_b2) #should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
common_elements(list_c1, list_c2) #should return [] (an empty list).