size = int(input("Enter the number of rows: "))
for blank in range(size) :
    for star in range(blank+1) :
        print("",end="")
    for star in range(blank,size) :
        print("*",end="")
    print()