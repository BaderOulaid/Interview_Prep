
numbers = [3,4,2,12,10,5]

def findFactors(numbers):

    numbers_seen = set()

    for number in numbers:
        #see if complimentary nubmer exists..
        comp_number = total // number
        if comp_number in numbers_seen:
            return True




    return
if __name__ == "__main__":
    print(findFactors(numbers))