"""1-12 sorting constraints:
Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

1-13 string operations - reverse sections:
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets.
It is guaranteed that the parentheses in s form a regular bracket sequence.
Your task is to reverse the strings contained in each pair of matching parentheses,
starting from the innermost pair. The results string should not contain any parentheses.

1-14 alternating sums:
Several people are standing in a row and need to be divided into two teams.
The first person goes into team 1, the second goes into team 2,
the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people.
Return an array of two integers, where the first element is the total weight of team 1,
and the second element is the total weight of team 2 after the division is complete."""


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


def reverse_parentheses(s):
    """Input: A string s consisting of English letters, punctuation marks, whitespace characters and brackets.
    It is guaranteed that parentheses form a regular bracket sequence. Constraints: 5 ≤ s.length ≤ 55
    Output: Returns the reversed string as per the above specified parentheses rules."""
    open_pos = []
    close_pos = []

    # get the positions in s of all open and close parenthesis
    for i in range(len(s)):
        if s[i] == "(":
            open_pos.append(i)
        if s[i] == ")":
            close_pos.append(i)
    #open_pos.reverse()
    #pairs = zip(open_pos, close_pos)
    # this does not work for cases where the parentheses are not all nested (if more than one pair)
    pairs = []

    # while there is at least one open parenthesis position left
    while len(open_pos) > 0:
        o = open_pos[0]
        c = close_pos[0]
        # append the last remaining open and close parentheses positions
        if len(open_pos) == 1:
            pairs.append([o, c])
        # if the second open parenthesis comes after the first close parenthesis, i.e. there is no nesting
        elif open_pos[1] > c:
            pairs.append([o, c])
            close_pos.remove(c)
        else:   # if there is nesting, pair the first open parenthesis with the last close parenthesis
            lc = len(close_pos)-1
            pairs.append([o, close_pos[lc]])
            close_pos.remove(close_pos[lc])
        open_pos.remove(o)

    pairs.reverse()    # to move the innermost parentheses pair to the front - irrelevant if there is no nesting

    for o, c in pairs:
        s_prev = s
        s2rev = ''.join(reversed(s[o+1:c]))    # get the content of the innermost parentheses and reverse it
        s = s_prev[:o+1] + s2rev + s_prev[c:]    # insert this into the "original" string (overwriting it)

    # get rid of all the parentheses for the final string
    s1 = s.replace("(", "")
    s_final = s1.replace(")", "")

    return s_final

s = "Where are the parentheses?"
s2 = "a(bcdefghijkl(mno)p)q"
s3 = "abc(cba)ab(bac)c"
print(reverse_parentheses(s))


def alternating_sums(a):
    """Input: array.integer a. Guaranteed constraints: 1 ≤ a.length ≤ 10, 45 ≤ a[i] ≤ 100.
    Output: Returns array.integer containing the total weight of each team."""
    team1 = []
    team2 = []

    for i in range(len(a)):
        if i % 2 == 0:
            team1.append(a[i])
        else:
            team2.append(a[i])

    result = [sum(team1), sum(team2)]

    return result


def alternating_sums2(a):
    team1 = sum(a[::2])
    team2 = sum(a[1::2])
    return [team1, team2]

a = [50, 60, 60, 45, 70]
print(alternating_sums2(a))
