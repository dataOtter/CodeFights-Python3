"""Given an IP address in CIDR notation. Calculate it's network address.
Example:
For cidr = "128.42.5.4/21", the output should be calculateNetworkAddress(cidr) = "128.42.0.0".
The network address is the logical AND of the respective bits in the binary representation
of the IP address and network mask.
Finally convert these four blocks to decimal to get the network address.
Thus the network address is calculated as "128.42.0.0" for the CIDR "128.42.5.4/21"."""


def calculate_network_address(cidr):
    """Input: string cidr in the format "n1.n2.n3.n4/m", where all n-s are 0 ≤ n ≤ 255 and 0 ≤ m ≤ 32.
    Guaranteed constraints: 9 ≤ cidr.length < 20.
    Output: Returns the network address of the given CIDR notation as a string."""
    ip = cidr.split('/')
    m = int(ip[1])
    ip = ip[0]

    # get one binary string, length 32, representing the ip address
    cc = ['{0:08b}'.format(int(x)) for x in ip.split('.')]
    cbin = ''.join(cc)

    # get network mask as a length 32 binary string
    mask = '1' * m + '0' * (32-m)
    net_addr = ''
    # get logical AND of binary ip address and network mask
    for i in range(32):
        net_addr += str(int(cbin[i]) and int(mask[i]))

    # convert the result from binary to integers, add them to a list
    network_address = []
    for i in range(0, 32, 8):
        n = int(net_addr[i:i+8], 2)
        network_address.append(str(n))

    # return that list in a valid network address string format
    return '.'.join(network_address)

cidr = "128.42.5.4/21"
print(calculate_network_address(cidr))
