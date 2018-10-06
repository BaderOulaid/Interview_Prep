# Implement your function below.
def is_one_away(s1, s2):
    #abs or do an or
    if(len(s1) - len(s2) > 2):
        return False

    # call the other functions


def same_length_dif_char(s1, s2):
    count_dif = 0
    for index in range(0, len(s1) - 1):
        if s1[index] != s2[index]:
            count_dif += 1
        if count_dif > 1:
            return False
    return True

# assumption:
def one_off_diff_lengths(s1, s2):
    s2_index = 0
    count_dif = 0

    while s2_index < len(s2):
        if s1[i+count_dif] == s2[i]:
            s2_index += 1
        else:
            count_dif += 1
            if count_dif > 1:
                return False

    return True



# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
