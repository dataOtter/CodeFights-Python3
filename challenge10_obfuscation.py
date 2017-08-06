def codeObfuscation(data, program):
    """Input: array.integer data. A data list that stores the type of each data cell,
    represented as integer. For the exact type, see the chart in the description above.
    Guaranteed constraints: 0 ≤ data.length ≤ 255.
    [input] string program. A string that represents the program that you're validating.
    Guaranteed constraints: 0 ≤ program.length ≤ 100.
    Output: Returns boolean true if the given program is valid or false if it is invalid,
    based on the data set and the data types and instructions that were given in the description above."""
    if program == '':
        return True

    for c in program:
        if not c.isdigit() and not c.isupper():
            return False

    if '0R' in program and program.index('0R') % 2 == 0:
        p = [program[:program.index('0R')]]

        while p != ['']:
            x = p[0][:2]

            if not check_instruction_and_data(x, p, data):
                return False

        return True

    return False


def get_data_definition(hx, data):
    index = int(hx, 16)
    if index < len(data):
        x = data[index]
    else:
        return '.'

    v = '.'
    if x == 1 or x == 3 or x == 4:
        v = 'n'
    elif x == 2:
        v = 'i'
    elif x == 5 or x == 6:
        v = 't'

    return v


def check_instruction_and_data(x, program, data):
    p = program[0]

    if len(p) > 5 and (x == '01' or x == '4A' or x == '13' or x == 'S2'):
        d1 = get_data_definition(p[2]+p[3], data)
        d2 = get_data_definition(p[4]+p[5], data)
        if (d1 == 'n' or d1 == 'i') and (d2 == 'n' or d2 == 'i'):
            program[0] = program[0][6:]
            return True

    elif len(p) > 3 and (x == '11' or x == '3F'):
        d1 = get_data_definition(p[2] + p[3], data)
        if d1 == 'i':
            program[0] = program[0][4:]
            return True

    elif len(p) > 5 and x == '99':
        d1 = get_data_definition(p[2] + p[3], data)
        d2 = get_data_definition(p[4] + p[5], data)
        if d1 == 't' and d2 == 't':
            program[0] = program[0][6:]
            return True

    elif len(p) > 5 and x == 'G0':
        d1 = get_data_definition(p[2] + p[3], data)
        d2 = get_data_definition(p[4] + p[5], data)
        if d1 == 't' and (d2 == 'n' or d2 == 'i'):
            program[0] = program[0][6:]
            return True

    return False


data = [1, 2, 3, 4, 5, 6]
program = "0100004A0000130101S2030311013F01990405G005010R"
p = "01 00 00 4A 00 00 13 01 01 S2 03 03 11 01 3F 01 99 04 05 G0 05 01 0R"
print(codeObfuscation(data, program))
