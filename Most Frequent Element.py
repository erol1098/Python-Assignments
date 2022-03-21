	
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
number = max(numbers, key = numbers.count)
count = numbers.count(number)
print(f"The most frequent number is {number} and it was {count} times repeated")