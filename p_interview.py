# Adam Rosenberg
# Wednesday, September 19


# routing numbers, account number
# pass a test to validate
# :
#

# create function that takes in routing number
# and returns if it is valid or not

import math


# routing number passed in as string
# 3(d1 + d4 + d7) + 7(d2 + d5 + d8) + (d3 + d6 + d9) % 10 == 0
def validate_routing_number(routing):

    if type(routing) != str:
        return False

    if len(routing) != 9:
        return False

    for char in routing:
        try:
            test = int(char)
        except:
            return False


    group_one = adder(routing[0],  routing[3],  routing[6])
    group_two = adder(routing[1], routing[4],  routing[7])
    group_three = adder(routing[2], routing[5], routing[8])

    result = 3*group_one + 7 *group_two + group_three
    return result % 10 == 0


def adder(first, second, third):
    return int(first) + int(second) + int(third)

# example_number = "111000025"
# example_number = "111000026"
# example_number = 123
# example_number = "112_45676"



# 1 + 0 + 0
# 1 + 0 + 2
# 1 + 0 + 5
# total = 30

print validate_routing_number(example_number)





