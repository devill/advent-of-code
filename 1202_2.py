import collections

with open('1202.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

for i in range(len(content[0])):
    c = [x[:i] + '*' + x[i+1:] for x in content]
    count = collections.Counter(c)
    if 2 in count.values():
       print count 



