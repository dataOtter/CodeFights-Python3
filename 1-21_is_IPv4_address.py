"""IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers,
each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1.
Given a string, find out if it satisfies the IPv4 address naming rules."""


def is_ipv4_address(string_in: str):
    """Input: string inputString, consisting of digits, full stops and lowercase Latin letters.
    Guaranteed constraints: 5 ≤ inputString.length ≤ 15.
    Output: Returns boolean true if inputString satisfies the IPv4 address naming rules, false otherwise."""
    ipv4 = True
    s = string_in.split(".")

    if len(s) != 4:
        ipv4 = False

    else:
        for x in s:
            # isdigit() only works on positive integers, so making sure 0 <= int(x) is redundant
            if not x.isdigit() or int(x) > 255:
                ipv4 = False
                break

    return ipv4

inputString = "172.-16.254.0"
print(is_ipv4_address(inputString))
