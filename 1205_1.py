
def reduced(string):
    rs = ""
    highlights = ""
    i = 0
    while i < len(string) - 1:
        if string[i] != string[i + 1].swapcase():
            highlights += string[i]
            rs += string[i]
            i+=1
        else:
            highlights += '\033[1m' + string[i] + string[i+1] + '\033[0m'
            i+=2 

    if i < len(string):
        highlights += string[i]
        rs += string[i]

    if rs == string:
        return rs
    else:
        print highlights
        print rs
        return reduced(rs)


with open("1205.txt") as f:
    content = f.readlines()[0].strip()

print len(reduced(content))
