
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

n = reduced(content)

while len(n) != len(content):
    content = n
    n = reduced(content)


print len(n)
