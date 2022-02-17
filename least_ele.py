s = [10,4,2,9,6,39]
least = s[0]
for i in range(1, len(s)):
    if s[i] < least:
        least = s[i]


print(least)
res = []
res.append(least)
print(res)