n = int(input())

lst = list(map(int, input().split()))
count_even = 0
count_odd = 0
for i in lst:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(count_even, count_odd)