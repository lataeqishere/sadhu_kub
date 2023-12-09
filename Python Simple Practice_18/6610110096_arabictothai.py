arabic_num = input("Enter only 5 Arabic number: ").strip()
thai_num = " ๐๑๒๓๔๕๖๗๘๙ "
arab_num = " 0123456789 "
thai_numm = ""
for x in arabic_num :
    index = arab_num.find(x)
    if (index != -1) :
        thai_numm = thai_numm + thai_num[index]
print(f"Thai number is {thai_numm}")