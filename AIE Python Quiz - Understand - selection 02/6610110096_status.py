comp_status = int(input("Enter computer status code: "))
formula = (comp_status//10)%3
if formula == 0 :
    print("Complete")
elif formula == 1 :
    print("Waiting")
elif formula == 2 :
    print("Error")