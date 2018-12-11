
with open('1201.txt') as f:
    content = f.readlines()

content = [int(x.strip()) for x in content] 

i = 0
f = 0

frequencies = {}

while not f in frequencies:
    frequencies[f] = True
    f += content[i%len(content)]
    i += 1
    print f

print i, f
