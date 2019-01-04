import re


def reduced(string):
    rs = ""
    i = 0
    while i < len(string) - 1:
        if string[i] != string[i + 1].swapcase():
            rs += string[i]
            i+=1
        else:
            i+=2 

    if i < len(string):
        rs += string[i]

    return rs

with open("1205.txt") as f:
    content = f.readlines()[0].strip()

min_len = len(content)
for c in 'abcdefghijklmnopqrstuvwxyz':
    regex = re.compile(c, re.IGNORECASE)
    m = regex.sub('', content)

    n = reduced(m)

    while len(n) != len(m):
        m = n
        n = reduced(m)

    min_len = min(len(n), min_len)

    print c, min_len, len(n)
