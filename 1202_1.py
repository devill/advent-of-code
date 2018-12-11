import collections

with open('1202.txt') as f:
    content = f.readlines()

content = [collections.Counter(list(x.strip())) for x in content]

twos = [1 if 2 in x.values() else 0 for x in content]
threes = [1 if 3 in x.values() else 0 for x in content]

print sum(twos)* sum(threes)


