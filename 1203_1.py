import re
import numpy as np

with open('1203.txt') as f:
    content = f.readlines()

r = re.compile("\#(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)")

content = [r.search(s).groupdict() for s in content]

m = np.zeros((1200,1200))

for c in content:
    m[int(c['left']):int(c['left'])+int(c['width']),int(c['top']):int(c['top'])+int(c['height'])] += 1 


print "Square inch of overlap:"
print np.count_nonzero(m > 1)

print "Claims with no overlap:"

for c in content:
    claim = m[int(c['left']):int(c['left'])+int(c['width']),int(c['top']):int(c['top'])+int(c['height'])]
    
    if np.count_nonzero(claim > 1) == 0:
        print c['id']
