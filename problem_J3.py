distances = '13 2 56 90'
dist = distances.split(' ')
distint = [int(r) for r in dist]

d1 = distint[0]
d2 = distint[1]
d3 = distint[2]
d4 = distint[3]


city1 = 0
city2 = d1
city3 = d2
city4 = d3
city5 = d4


print(city1 + city1, city1 + city2, city1 + city2 + city3, city1 + city2 + city3 + city4, city1 + city2 + city3 + city4 + city5)

city1 = d1
city2 = 0
print(city2 + city1, city2 + city2, city2 + city3, city2 + city3 + city4, city2 + city3 + city4 + city5)

city2 = d2
city3 = 0
print(city3 + city2 + city1, city3 + city2, city3 + city3, city3 + city4, city3 + city4 + city5)

city3 = d3
city4 = 0
print(city4 + city3 + city2 + city1, city4 + city3 + city2, city4 + city3, city4 + city4, city4 + city5)

city4 = d4
city5 = 0
print(city5 + city4 + city3 + city2 + city1, city5 + city4 + city3 + city2, city5 + city4 + city3, city5 + city4, city5 + city5)

