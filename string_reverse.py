
phrase = ["h", "e", "l", "l", "o"]


def reverse_list(phrase):
    left_index = 0
    right_index = len(phrase)-1

    while left_index < right_index:
        phrase[left_index], phrase[right_index] = phrase[right_index], phrase[left_index]

        left_index += 1
        right_index -= 1

    print phrase





if __name__=="__main__":
    reverse_list(phrase)