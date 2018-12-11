import re
import numpy as np

with open('1204s.txt') as f:
    content = f.readlines()

line_regex = re.compile("\[.*(?P<hour>\d\d):(?P<minute>\d\d)\] (?P<line>.*)")

content = [line_regex.search(s).groupdict() for s in content]

id_regex = re.compile(" \#(?P<id>\d+) ")

last_id = -1
sleep_minute = -1

guards = {}

for record in content:
    l = record['line']

    if l == "wakes up":
        wake_minute = int(record['minute'])

        guards[last_id][sleep_minute:wake_minute] += 1

    elif l == "falls asleep":
        sleep_minute = int(record['minute'])
    else:
        gid = id_regex.search(l).groupdict()['id']
        if gid not in guards:
            guards[gid] = np.zeros(60)

        last_id = gid


max_v = 0
max_k = -1
for g in guards:
    s = np.sum(guards[g])
    if s > max_v:
        max_k = g
        max_v = s

print max_k

t = guards[max_k]
print np.argmax(t)

print int(max_k) * np.argmax(t)
