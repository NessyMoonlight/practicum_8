def perfect_number(number):
    div_sum = sum([i for i in range(1, number) if number % i == 0])
    return div_sum == number

def count_perf_num(n):
    perfect_count = 0
    for i in range(2, n+1):
        if perfect_number(i):
            perfect_count += 1
    return perfect_count

number = int(input())
perf_c = count_perf_num(number)
print(perf_c)
