def perfect_number(number):
    div_sum = sum([i for i in range(1, number) if number % i == 0])
    return div_sum == number

n = int(input())
for i in range(2, n+1):
    if perfect_number(i):
        print(i)
