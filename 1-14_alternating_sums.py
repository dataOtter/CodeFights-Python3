"""Several people are standing in a row and need to be divided into two teams.
The first person goes into team 1, the second goes into team 2,
the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people.
Return an array of two integers, where the first element is the total weight of team 1,
and the second element is the total weight of team 2 after the division is complete."""


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
