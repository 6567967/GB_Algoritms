from collections import Counter

a = Counter()
b = Counter('abrakadabra')
c = Counter({'cat': 15, 'dog': 5})
d = Counter(cats=2, dogs=4)
print(a, b, c, d, sep='\n')

print(b['z'])
b['z'] = 3
print(b)

print(b.most_common(3))

print(list(b.elements()))

e = Counter(a=1, b=-2, c=3)
print(list(e.elements()))
f = Counter(a=3, b=-1, c=-4)
print(e, f, sep='\n')
print(e + f)
print(e - f)
print(e & f)
print(e | f)
