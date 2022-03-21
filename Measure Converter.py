	
temp_c = input("Please enter the temperature in Celcius:  ")
temp_c = float(temp_c)
temp_f = round(temp_c * 1.8 + 32, 2)
print(f"Temperature is {temp_f} Fahrenheit")


dist_km = input("Please enter the distance in kilometers: ")
dist_km = float(dist_km)
dist_mile = round(0.621371192 * dist_km, 2)
print(f"Distance is {dist_mile} miles")