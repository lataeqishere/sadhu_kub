list_num = []
while True :
    user_input = int(input("Enter number: "))
    if user_input > 0 :
        list_num.append(user_input)
    elif user_input < 0 :
        break
print("Minimum number is",min(list_num))
print("Maximum number is",max(list_num))
