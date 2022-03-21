	
fib_list = [1, 1]
for index in range(2, 56):
    if fib_list[-1] + fib_list[-2] == index:
        fib_list.append(index)
print(fib_list)