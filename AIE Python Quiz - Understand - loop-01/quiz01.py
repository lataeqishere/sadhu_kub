input_num = [int(x) for x in input("Enter numbers: ").split()]
even_number = [i for i in input_num if i%2==0]
print("Total:",sum(even_number))