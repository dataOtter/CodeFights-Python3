"""You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets.
It is guaranteed that the parentheses in s form a regular bracket sequence.
Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair.
The results string should not contain any parentheses."""


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
    #print(pairs)

    for o, c in pairs:
        s_prev = s
        s2rev = ''.join(reversed(s[o+1:c]))    # get the content of the innermost parentheses and reverse it
        #print(s2rev)
        s = s_prev[:o+1] + s2rev + s_prev[c:]    # insert this into the "original" string (overwriting it)
        #print(s)

    # get rid of all the parentheses for the final string
    s1 = s.replace("(", "")
    s_final = s1.replace(")", "")

    return s_final


s = "Where are the parentheses?"
s2 = "a(bcdefghijkl(mno)p)q"
s3 = "abc(cba)ab(bac)c"
print(reverse_parentheses(s))

