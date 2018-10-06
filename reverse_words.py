message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']


def reverse_list(phrase, left_index, right_index):

    while left_index < right_index:
        phrase[left_index], phrase[right_index] = phrase[right_index], phrase[left_index]

        left_index += 1
        right_index -= 1

def reverse(phrase):
    reverse_list(phrase, 0, len(phrase)-1)
    current_word_start = 0
    for i in xrange(len(phrase)+1):
        if (i == len(phrase) or phrase[i] == ' '):
            reverse_list(phrase, current_word_start, i-1)
            current_word_start = i + 1



if __name__ == "__main__":
    reverse(message)
    print message