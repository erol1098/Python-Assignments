	
from numpy import ERR_LOG


password = {"Erol": ("SP00&+c(Q", ), "Zehra": ("SP00&+c(Q", ), "Enes": ("q9N##t4$4", ) }
query_name = input("Enter a name to query:  ").capitalize()
is_found = False
for key in password:
    if query_name == key:
        print(f"Hello, {query_name}! The password is : {password[key]}")
        is_found = True
if is_found == False:
    print(f"Hello, {query_name}! See you later.")