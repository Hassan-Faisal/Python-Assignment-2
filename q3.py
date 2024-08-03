temp_in_fahrenheit : str = input("Enter Temperature in Fahrenheit : ")
convert : float = float(temp_in_fahrenheit)

temp_in_celsius : float = (convert - 32) * 5.0/9.0

print(f"Temperature : {convert} ^ Fahrenheit = {temp_in_celsius} ^ Celsius")

