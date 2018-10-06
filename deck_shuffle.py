


def optimizedRecursiveRif(half1, half2, deck, deck_index, h1_index, h2_index):

    if deck_index == len(deck):
        return True

    if((h1_index < len(half1)) and half1[h1_index] == deck[deck_index]):
        h1_index += 1
    elif((h2_index < len(half2)) and half2[h2_index] == deck[deck_index]):
        h2_index += 1
    else:
        return False

    deck_index += 1

    return optimizedRecursiveRif(half1, half2, deck, deck_index, h1_index, h2_index)


def isRifRecursive(half1, half2, deck):

    #deck[0] should be top of half1 or half 2

    if len(deck) == 0:
        return True

    if len(half1) and half1[0] == deck[0]:
        return isRifRecursive(half1[1:], half2, deck[1:])

    elif len(half2) and half2[0] == deck[0]:
        return isRifRecursive(half1, half2[1:], deck[1:])

    return False

if __name__ == "__main__":
    half1 = [1, 3, 4]
    half2 = [10, 5, 2]
    deck = [10, 1, 5, 3, 2, 4, 10]
    # print isRifRecursive(half1, half2, deck)
    print optimizedRecursiveRif(half1, half2, deck, 0, 0, 0)