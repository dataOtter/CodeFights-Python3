"""Lazy Beaver, Busy Beaver's less ambitious cousin, is extremely lazy.
He needs help finding the shortest of the available three tasks.
These tasks involve writing down values to a tape, and this tape is
infinite so if you pick poorly our Beaver friend may be occupied indefinitely.
Each task is presented as a a series of states. Each state is represented by
an array of six integers - [a0, a1, b0, b1, c0, c1], which determine the next
action depending on the value on the tape at the current position. Here is how it works:
    a0 and a1 - if the initial value (when we entered current state) is 0, then we change
        the current value to a0, if the initial value is 1 - to the value a1;
    b0 and b1 - if the initial value is 0, then move in the direction b0, otherwise -
        in the direction b1, where 1 stands for the right, -1 stands for the left.
    c0 and c1- if the initial value is 0, move to the next state c0, otherwise - to c1 (0-based).
        The state with value -1 is the halting.
The initial state of the tape is fully zeroed. 0 and 1 are the only valid values to write to tape.
Your goal is to find out how many 1-s will be written to the tape by the machine which halts first.
It is guaranteed that there is at least one halting task."""


def lazyBeaver(t1, t2, t3):
    """Input: array.array.integer t1, t2, t3. t[i][0] and t[i][1] can only be
    0 or 1 as a0 and a1, t[i][2] and t[i][3] can only be -1 or 1 as b0 and b1.
    -1 ≤ t[i][4] < t.length and -1 ≤ t[i][5] < t.length, as c0 and c1.
    Guaranteed constraints: 2 ≤ t.length ≤ 5, t[i].length = 6.
    Output: Returns number of 1s written to tape by the machine which halts first."""
    tur1 = get_tur(t1)
    tur2 = get_tur(t2)
    tur3 = get_tur(t3)

    while True:
        if tur1["state"] == -1:
            t = tur1
            break
        elif tur2["state"] == -1:
            t = tur2
            break
        elif tur3["state"] == -1:
            t = tur3
            break
        else:
            step(tur1)
            step(tur2)
            step(tur3)

    ones = 0
    for i in range(len(t["tape"])):
        if t["tape"][i] == 1:
            ones += 1

    return ones


def get_tur(t):
    return {"task": t,
            "tape": [0] * 999,
            "pos": 0,
            "state": 0, }


def step(tur):
    t, tp, p, s = tur["task"], tur["tape"], tur["pos"], tur["state"]
    b = tp[p]

    tp[p] = t[s][b]
    if t[s][b+2] == 1:
        p += 1
    else:
        p -= 1
    st = s
    s = t[st][b+4]

    tur["task"], tur["tape"], tur["pos"], tur["state"] = t, tp, p, s

    return tur


t1 = [[1,1,1,-1,1,1], [1,1,-1,1,0,-1]]
t2 = [[0,1,1,1,1,-1], [0,1,-1,1,2,0], [1,1,1,-1,1,2]]
t3 = [[1,1,1,1,1,-1], [1,0,-1,1,1,2], [1,1,-1,-1,2,0]]

tt1 = [[1,1,1,1,4,4],
 [1,1,-1,1,2,2],
 [0,1,-1,1,0,0],
 [1,0,-1,-1,-1,-1],
 [0,0,-1,-1,1,1]]
tt2 = [[1,1,1,-1,1,1],
 [1,0,-1,-1,0,2],
 [1,1,1,-1,-1,3],
 [1,0,1,1,3,0]]
tt3 = [[1,1,1,1,4,4],
 [1,1,-1,1,2,2],
 [0,1,-1,1,0,0],
 [1,0,-1,-1,-1,-1],
 [0,0,-1,-1,1,1]]

print(lazyBeaver(tt1, tt2, tt3))
