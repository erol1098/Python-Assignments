user_entry = input("Enter a number:  ")
if user_entry.isdigit():
    number_length = len(user_entry)
    number = int(user_entry)
    sum = 0
    for num in user_entry:
        num = int(num)
        digit = 1
        for _ in range(number_length):
            digit *= num
        sum += digit

    if sum == int(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")