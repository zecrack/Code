s = '*'
#(a)
for i in range(1,6):
    print(s*i)
print()
#(b)
for i in range(1, 10, 2):
    print((s*i).center(9))
print()
#(c)
for i in range(1, 6, 2):
    print((s*i).center(5))
for i in reversed(range(1, 4, 2)):
    print((s*i).center(5))