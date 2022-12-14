a = [1, 2, 3, 4, 5]

a1 = [(x, x ** 2) for x in a]
print (a1)

a2 = list(map(lambda x: (x, x ** 2), a))
print (a2)

a3 = list(zip(a,[x**2 for x in a]))
print (a3)

a4 = list(zip([x for x in a], [x ** 2 for x in a]))
print (a4)