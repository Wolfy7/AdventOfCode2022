with open('13/input') as f:
    packets = [packet.split() for packet in f.read().split('\n\n')]

big_list = [eval(x) for x in sum(packets, [])] + [[[2]]] + [[[6]]]


def is_in_right_order(left, right):

    # get the range of possible element comparison
    n_left, n_right = len(left), len(right)
    n = max(n_left, n_right)

    # for each possible element comparison
    for idx in range(n):

        # this is true if left has less elements than right
        if idx >= n_left: return True
        # this is true if right has less elements than left
        if idx >= n_right: return False

        # get the elements we are comparing in this iteration
        left_v, right_v = left[idx], right[idx]
        # and the types of those elements
        left_typ, right_typ = type(left_v), type(right_v)

        # simple situation where both ints
        if (left_typ is int) & (right_typ is int):
            if left_v < right_v: return True
            elif left_v > right_v: return False

        # otherwise at least one is a list
        else:
            # if one is an int, we convert to single element list
            if (left_typ is int): left_v = [left_v]
            if (right_typ is int): right_v = [right_v]
            # then recursively run this function on these lists
            res = is_in_right_order(left_v, right_v)
            # only return a value if it was True or False
            # (if None was returned we move to next element comparison)
            if res is not None: return res

sum = 0
for i, packet in enumerate(packets, 1):
    left = eval(packet[0])
    right = eval(packet[1])
    if is_in_right_order(left, right):
        sum += i

print(sum)

def bubble_sort(big_list):
    n = len(big_list)
    for i in range(n-1): # for each element
        for j in range(0, n-i-1): # compare to all of those to the left
            # use our custom function to determine if j+1 is smaller than j
            if is_in_right_order(big_list[j + 1], big_list[j]):
                # if so we swap
                big_list[j], big_list[j + 1] = big_list[j + 1], big_list[j]

bubble_sort(big_list)
for idx, elem in enumerate(big_list):
    if elem == [[2]]: x = idx+1
    if elem == [[6]]: y = idx+1
print(x*y)


