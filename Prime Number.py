	
prime = None
is_positive = True
is_end = False
n = int(input("Check this number: "))
while is_positive and not is_end:
    if n == 0 or n== 1:
        print(f"{n} cannot be prime number")
        is_positive = False
    elif n <= 1:
        print("Negative numbers cannot be prime number")
        is_positive = False        
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
        if prime == False:
            print(f"{n} is not a prime number.")
        else:
            print(f"{n} is a prime number.")
    is_end = True