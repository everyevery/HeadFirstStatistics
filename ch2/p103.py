d1 = dict(((1,4),(2,6),(3,4),(4,4),(5,3),(6,2),(7,1),(8,1)))
d2 = dict(((1,1),(4,1),(6,2),(8,3),(9,4),(10,4),(11,5),(12,5)))

n = 0
s = 0

for k in sorted(d1.keys()):
    s +=  (k * d1[k])
    n += d1[k]

print(s/n)
median = n // 2

for k in sorted(d1.keys()):
    median -= d1[k]
    if median <= 0:
        print(k)
        break

n = 0
s = 0

for k in sorted(d2.keys()):
    s +=  (k * d2[k])
    n += d2[k]

print(s/n)
median = n // 2

for k in sorted(d2.keys()):
    median -= d2[k]
    if median <= 0:
        print(k)
        break
