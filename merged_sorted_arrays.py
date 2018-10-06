

# merged_list

def merge_lists(first_list, second_list):
    # set up merged list
    merged_list_size = len(first_list) + len(second_list)
    merged_list = [None] * merged_list_size

    first_index = 0
    second_index = 0
    merged_index = 0

    while merged_index < merged_list_size:


        first_done = first_index >= len(first_list)
        second_done = second_index >= len(second_list)

        if (not first_done and (second_done or first_list[first_index] < second_list[second_index])):
            merged_list[merged_index] = first_list[first_index]
            first_index += 1
        elif(not second_done and (first_done or second_list[second_index] < first_list[first_index])):
            merged_list[merged_index] = second_list[second_index]
            second_index += 1
        merged_index += 1

    print merged_list

if __name__ == "__main__":
    my_list = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 20, 24]



    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    merge_lists(my_list, alices_list)