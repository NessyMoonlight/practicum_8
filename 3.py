zp = []
while True:
    salary = float(input())
    if salary == 0:
        break
    else:
        zp.append(salary)
zp = sum(zp) / len(zp)
print(f"{zp:.1f}")