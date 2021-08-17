import random

a = random.sample(range(1, 100), random.randint(0, 10))
b = random.sample(range(1, 100), random.randint(0, 10))

c = list(set([x for x in a if x in b]))

print(a)
print(b)
print(c)