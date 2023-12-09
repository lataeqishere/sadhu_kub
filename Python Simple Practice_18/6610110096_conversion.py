input_value = input("Enter value in mm, cm, and m: ")
x = -2
if len(input_value) == 2 :
    x = x+1
input_unit = input_value[-2:]
conv_unit = input("Enter unit to convert in mm, cm, m: ")
value = float(input_value[:x])
if input_unit == "cm" :
    value = value*0.01
elif input_unit == "mm" :
    value = value*0.001
if conv_unit == "cm" :
    value = value*100
elif conv_unit == "mm" :
    value = value*1000

print(f"Value after unit conversion is {value}{conv_unit}")