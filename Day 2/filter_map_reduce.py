from functools import reduce

data = [5, 12, 7, 18, 3, 10]
print("Original data:", data)

doubled = list(map(lambda x: x * 2, data))
print("Doubled values using map():", doubled)

greater_than_10 = list(filter(lambda x: x > 10, data))
print("Filtered values using filter() (greater than 10):", greater_than_10)

total_sum = reduce(lambda x, y: x + y, data)
print("Sum of all values using reduce():", total_sum)