
def find_common(names1, names2):

    common = []

    if len(names1) > len(names2):
        common = helper_common(names1, names2)
    else:
        common = helper_common(names2, names1)

    return common

def helper_common(longer_list, shorter_list):
    found_names = {}
    common = []
    for name in longer_list:
        found_names[name] = name

    for name in shorter_list:
        if name in found_names:
            common.append(name)
    return common


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(find_common(names1, names2))  # should print Ava, Emma, Olivia, Sophia