d = ''
for i in range(1, 10):
    d += str(i)
    print(f"{d} * 8 + {i} = {int(d) * 8 + i}")
d = ''
for i in range(1, 10):
    d += str(i)
    print(f"{d} * 9 + {i+1} = {int(d) * 9 + (i+1)}")
for i in range(1, 10):
    d = '1' * i
    print(f"{d} * {d} = {int(d) * int(d)}")