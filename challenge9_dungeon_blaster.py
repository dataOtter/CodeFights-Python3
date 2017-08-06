"""Dungeon Blaster is an exciting new computer game in which you must guide your character through
a perilous labyrinth. The game is still in its alpha stage, so you've been hired to test some level designs.
You're given a map of the labyrinth, in the form of an array of equal-length strings.

LEGEND
Here's what each type of tile represents:
    "*" : This is your character's starting position;
    "^" : This is the exit (the goal is to get your character to this spot);
    " " : Spaces represent open space that your character can move through freely;
    "#" : Hashtags represent walls, which your character can't move through;
    "A" : Uppercase letters represent doors, which are all initially locked, meaning your character
            can't go through a door unless you have collected the corresponding key;
    "a" : Lowercase letters represent keys, which unlock the door of the same letter. Your character
            can move through these tiles.

HOW TO PLAY
Your character can move in four directions: up, down, left, and right - but no diagonals.
The goal is to direct your character from her starting position ("*") to the exit ("^").
You may need to pick up some keys in order to get there!
One more important detail: This labyrinth is located on the surface of a torus,
so it is possible for your character to wrap around the map vertically or horizontally,
unless they're blocked by a wall or door.
As an alpha tester, your responsibility is to determine whether or not
it's possible to reach the exit on the given map."""


def dungeonBlaster(map):
    """Input: array.string m. This is the map of the level. Check the legend above to see what
    each type of character represents. Guaranteed constraints: 1 ≤ m.length ≤ 40, 2 ≤ m[i].length ≤ 40.
    Output: Returns boolean True if the level can be completed, and False if the level is impossible."""
    num_c = len(map[0])
    num_r = len(map)

    m = []

    for r in map:
        lst = []
        for c in r:
            lst.append(c)
        m.append(lst)

    visited = []
    removed = 999

    door_pos = {}
    key_pos = {}

    for i in range(num_r):
        for j in range(num_c):
            x = get_pos_value(m, [i, j])
            if x == "*":
                s_pos = [i, j]
                m[i][j] = ' '
            elif x == "^":
                e_pos = [i, j]
            elif x.isupper():
                door_pos[x] = [i, j]
            elif x.islower():
                key_pos[x] = [i, j]

    print(key_pos)
    '''to_remove = []
    for d in door_pos:
        if d.lower() not in key_pos:
            to_remove += d

    for d in to_remove:
        del door_pos[d]'''

    while removed > 0:
        removed = try_remove_keys_and_doors(m, s_pos, key_pos, num_r, num_c, visited, door_pos)
        #print(removed)

    visited = []

    return depth_first_path_search(m, s_pos, e_pos, num_r, num_c, visited)


def try_remove_keys_and_doors(m, s_pos, key_pos, num_r, num_c, visited, door_pos):
    removed = 0
    to_remove = []

    for k in key_pos:
        kk = key_pos[k]
        kr = kk[0]
        kc = kk[1]
        visited = []

        if depth_first_path_search(m, s_pos, kk, num_r, num_c, visited):
            dd = door_pos[k.upper()]
            dr = dd[0]
            dc = dd[1]
            m[kr][kc] = ' '
            m[dr][dc] = ' '
            removed += 1
            to_remove += k
            #print(k)

    for k in to_remove:
        del key_pos[k]

    return removed


def depth_first_path_search(m, cur_pos, e_pos, num_r, num_c, visited):
    n_pos = get_open_neighbors(m, num_r, num_c, cur_pos, visited)
    if not n_pos:
        return False

    e_n_pos = get_open_neighbors(m, num_r, num_c, e_pos, visited)

    for p in n_pos:
        if p in e_n_pos:
            return True

        v = visited
        v.append(p)

        attempt = depth_first_path_search(m, p, e_pos, num_r, num_c, v)
        if attempt == True:
            return True

    return False


def get_pos_value(m, pos):
    return m[pos[0]][pos[1]]


def get_open_neighbors(m, num_r, num_c, pos, visited):
    """Input: Map array.string m. Number of rows num_r. Number of columns num_c.
    Current position array.int pos, len 2.
    Output: Returns array.array.int n of neighbor coordinates that are open,
    wrapping around the map when necessary."""
    n = []
    r, c = pos[0], pos[1]

    pos_below = [(r + 1) % num_r, c]
    if pos_below not in visited and (get_pos_value(m, pos_below) == ' ' or get_pos_value(m, pos_below).islower()):
        n.append(pos_below)

    pos_above = [(r - 1) % num_r, c]
    if pos_above not in visited and (get_pos_value(m, pos_above) == ' ' or get_pos_value(m, pos_above).islower()):
        n.append(pos_above)

    pos_left = [r, (c - 1) % num_c]
    if pos_left not in visited and (get_pos_value(m, pos_left) == ' ' or get_pos_value(m, pos_left).islower()):
        n.append(pos_left)

    pos_right = [r, (c + 1) % num_c]
    if pos_right not in visited and (get_pos_value(m, pos_right) == ' ' or get_pos_value(m, pos_right).islower()):
        n.append(pos_right)

    return n

m= ["########",
 "#^CeFgj#",
 "#AcEhiI#",
 "#aDbHKk#",
 "#BdGfJ*#",
 "########"]

print(dungeonBlaster(m))
