number_i = int(input('Enter number i: '))
number_j = int(input('Enter number j: '))
magic_num = int(input('Enter magic number: '))

c = 0
for i in range(number_i+1) :
    for j in range(number_j+1) :
        magic = i*10+j

        if magic  % magic_num == 0 :
            c = c+1



print(f'Found {c} magic numbers ')