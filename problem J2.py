totalspaces = int(input())
day1 = input()
day2 = input()
sameocc = 0

for i in range(totalspaces):
    if day1[i] == 'C' and day2[i] == 'C':
        sameocc = sameocc + 1

print(sameocc)