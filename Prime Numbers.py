prime_list = []	
prime = None
n = 100
for n in range(2, 101):
  for i in range(2, n):
      if n % i == 0:
          prime = False
  if prime == False:
      pass
  else:
      prime_list.append(n)
  prime = True      
print(prime_list)