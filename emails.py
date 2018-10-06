# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(L):
    # write your code in Python 3.6
    results = {}
    for address in L:
        simplified_address = simplify_string(address)

        simplified_string = simplified_address[0] + simplified_address[1]

        if simplified_string in results:
            results[simplified_string].append(address)
        else:
            results[simplified_string] = [address]

    count = 0
    for key, value in results.items():
        if len(value) > 1:
            count += 1
    return count


def simplify_string(address):
    address_list = address.split('@')
    local_name = address_list[0]
    domain = address_list[-1]
    # first simplify local name
    # remove dots
    local_name = local_name.replace(".", "")
    # split after + in local
    plus_index = local_name.find('+')
    if plus_index >= 0:
        local_name = local_name[:plus_index]

    return [local_name, domain]
