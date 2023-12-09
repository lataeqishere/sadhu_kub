input_text = input("Enter text: ")
input_filter = input("Enter filter word: ")
len_filter = len(input_filter)
star = "*"*len_filter
after_filter = input_text.replace(input_filter,star)
if input_filter in input_text :
    print(f'Text after filter is "{after_filter}"')
else :
    print(f'Text after filter is "{input_text}"')

