"""Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees."""


def sort_by_height(a):
    """Input: array.integer a. If a[i] = -1, then the ith position is occupied by a tree.
    Otherwise a[i] is the height of a person standing in the ith position.
    Guaranteed constraints: 5 ≤ a.length ≤ 15, -1 ≤ a[i] ≤ 200.
    Output: Returns height sorted array with trees in the same positions."""
    tree_locations = []
    i, t = 0, 0

    while i < len(a):
        if a[i] == -1:
            tree_locations.append(t)
            a.remove(a[i])
        else:
            i += 1
        t += 1

    a.sort()

    while tree_locations:
        # This insert will never be beyond the currently last element of a,
        # because tree location is in increasing order from when it was appended.
        a.insert(tree_locations[0], -1)
        tree_locations.pop(0)

    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sort_by_height(a))
