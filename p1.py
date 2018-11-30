def solve_p1(seq):
    res = 0
    arr = []
    if seq[0] == seq[-1]:
        print("part1: 1st and last are equal")
        res += int(seq[0])
        arr.append(int(seq[0]))

    for i in range(0,len(seq)-1):
        if seq[i] == seq[i+1]:
            res += int(seq[i])
            arr.append(int(seq[i]))

    print("part1: res:{}".format(res))
    print("part1: arr:{}".format(arr))
    s = sum(arr)
    assert(s == res)
    return res

def halfway_around_match(seq):
    seq_len = len(seq)
    print("sequence length:{}".format(seq_len))
    separate = int(seq_len/2)
    print("separate:{}".format(separate))
    res = 0

    for i in range(0,seq_len):
        print("i:{}, (i+separate) % seq_len:{}".format(i,(i+separate) % seq_len))
        if seq[i] == seq[(i+separate) % seq_len]:
            res += int(seq[i])

    return res

