n = int(input())
for i in range(2, n+1):
    k_div = 0
    for k in range(2, int(i**0.5)+1):
        if i % k == 0:
            k_div += 1
    if k_div == 0:
        print(i)