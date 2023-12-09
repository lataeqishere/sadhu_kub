int_num = [int (x) for x in input("Enter 10 numbers: ").split()]
even_num = {num for num in int_num if num%2==0}
print("Result is",even_num)