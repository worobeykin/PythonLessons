#convert temperature

print("convert temperature App")

celsius = float(input("\nEnter celsius degree: "))

fahrenheit = celsius*9/5+32
kelvin = celsius+273.15

fahrenheit = round(fahrenheit, 4)
kelvin = round(kelvin, 4)
               

print("\nfahrenheit: \t" + str(fahrenheit))
print("keivin: \t" + str(kelvin))


