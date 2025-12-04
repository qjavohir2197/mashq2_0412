#1-misol
roy = [12, 45, 76, 86, 93]
result = list(map(lambda x: abs(x), roy))
print(result)

#2-misol
roy = ['Jack', 'Bob', 'Sam', 'Robert']
result = list(map(lambda soz: soz[::-1], roy))
print(result)

#3-misol
roy = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**3, roy))
print(result)

#4-misol
roy = ['Jack', 'Sam', 'Nicolas', 'Bob']
result = list(map(lambda soz: soz[0], roy))
print(result)

#5-misol
roy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: 'Juft' if  x % 2 == 0 else 'Toq', roy))
print(result)
