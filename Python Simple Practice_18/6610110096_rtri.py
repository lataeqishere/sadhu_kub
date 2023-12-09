num_row = int(input("Enter the number of rows: "))
for x in range(1,num_row+1):
    for i in range(1,(num_row - x)+1) :
        print(" ",end = "")
    for z in range(1,x+1) :
        print("*",end= "")
    print()