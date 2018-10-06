# same arrays, same order, but starts at different indices

# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    index_one = 0
    index_two = 0


    key = list1[0]
    key_index = -1

    for i in range(0,len(list2)-1):
        if list2[i] == key:
            key_index = i
            break

    if key_index == -1:
        return False

    return False

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
is_rotation(list1, list2a) #should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.