def knothash(line,  length = 256):
    lengths = [ord(char) for char in line] + [17, 31, 73, 47, 23]

    n = []
    for i in range(length):
        n.append(i)

    pos = 0
    skipSize = 0

    iterations = 64

    for _ in range(iterations):
        for k in lengths:
            for l in range(k // 2):
                p1 = (pos + l) % length
                p2 = (pos + k - 1 - l) % length
                t = n[p1]
                n[p1] = n[p2]
                n[p2] = t
            pos = (pos + k + skipSize) % length
            skipSize += 1

    out = ""
    for c in range(16):
        x = 0
        for i in range(16):
            x ^= n[c * 16 + i]
        out += "{:02x}".format(x)

    return out

