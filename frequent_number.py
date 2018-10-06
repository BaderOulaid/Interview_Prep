

def most_frequent(numbers):

    max_count = 0
    max_item = None

    if numbers == []:
        return None

    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
            if counts[number] > max_count:
                max_count = counts[number]
            max_item = number
        else:
            counts[number] = 1

    return max_item, max_count


if __name__ == "__main__":
    numbers = [1, 3, 1, 3, 2, 1]
    # NOTE: The following input values will be used for testing your solution.
    # most_frequent(list1) should return 1
    list1 = [1, 3, 1, 3, 2, 1]
    # most_frequent(list2) should return 3
    list2 = [3, 3, 1, 3, 2, 1]
    # most_frequent(list3) should return None
    list3 = []
    # most_frequent(list4) should return 0
    list4 = [0]
    # most_frequent(list5) should return -1
    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

    print(most_frequent(numbers))


