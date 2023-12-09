size = int(input("Enter the number of rows: "))
symbol = input("Enter print symbol: ")
for blank in range(size) :
    for star in range(blank) :
        print(" ",end="")
    for star in range(2*(size-blank)-1) :
        print(symbol,end="")
    print()