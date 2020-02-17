#Convert bin, hex

print("This is a convert App")

length = int(input("\nHow many values whould yoy like to convert:"))



list_numbers = list(range(1, length+1))
print(list_numbers)

bin_values = []
hex_values = []

for bin_value in list_numbers:
    bin_values.append(bin(bin_value))

for hex_value in list_numbers:
    hex_values.append(hex(hex_value))

print("\nThe lists completed...")

#Get user range
print("\nUsing skices, we will now show a portion of each list.")
start_poz = int(input("What number would you like to start at:"))
finish_poz = int(input("What number would you like to finish at:"))

#Show values
print("\nDecimal values from " + str(start_poz) + " to " + str(finish_poz))
for i in list_numbers[start_poz-1:finish_poz]:
    print(i)
print("\nBinary values from " + str(start_poz) + " to " + str(finish_poz))
for i in bin_values[start_poz-1:finish_poz]:
    print(i)
print("\nHexadecimal values from " + str(start_poz) + " to " + str(finish_poz))
for i in hex_values[start_poz-1:finish_poz]:
    print(i)

#All values
input("\nPress Enter to see all values from " + str(list_numbers[0]) + " to " + str(length))
print("Decimal---Binary---Hexadecimal\n--------------------")
for list_number, bin_value, hex_value in zip(list_numbers, bin_values, hex_values):
    print(str(list_number) + "\t\t" + str(bin_value) + "\t\t" + str(hex_value))






    
