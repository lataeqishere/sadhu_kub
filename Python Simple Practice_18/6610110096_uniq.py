numbers = []
even_num = []

for i in range(1,21):
    num = int(input(f"Enter number #{i}: "))
    numbers.append(num)

sort = sorted(set(numbers))

for x in range(len(sort)) :
    if x % 2 == 0 :
        even_num.append(sort[x])
        
avg_even = sum(even_num) / len(even_num)
uniq_num = " ".join(map(str, sort))

print("Unique numbers is",uniq_num)
print(f"Average number of even position in list is {avg_even:.2f}")