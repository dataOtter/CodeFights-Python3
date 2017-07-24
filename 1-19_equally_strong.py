"""Call two arms equally strong if the heaviest weights they each are able to lift are equal.
Call two people equally strong if their strongest arms are equally strong
(the strongest arm can be both the right and the left), and so are their weakest arms.
Given your and your friend's arms' lifting capabilities find out if you two are equally strong."""


def are_equally_strong(yourLeft, yourRight, friendsLeft, friendsRight):
    """Input: 4 non-negative integers representing the heaviest weight you and your friend can lift with each arm.
    Guaranteed constraints: 0 ≤ arm ≤ 20.
    Output: Returns true if you and your friend are equally strong, false otherwise."""
    '''you = sorted([yourLeft, yourRight])
    friend = sorted([friendsLeft, friendsRight])
    equal = False
    if you == friend:
        equal = True
    return equal'''
    return sorted([yourLeft, yourRight]) == sorted([friendsLeft, friendsRight])

print(are_equally_strong(10, 15, 15, 10))
