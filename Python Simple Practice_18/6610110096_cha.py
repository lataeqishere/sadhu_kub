alpha_count = {}
while True:
    input_str = input("Enter string: ")
    if input_str == 'end' :
            break
    else :
        for i in input_str :
            if i.isalpha() :
                lower = i.lower()
                if lower in alpha_count :
                    alpha_count[lower] += 1
                else :
                    alpha_count[lower] = 1

print("******************************")
print("*     Alphabet Counting      *")
print("******************************")

for i in sorted(alpha_count.keys()) :
    print(i, alpha_count[i])

print("******************************")