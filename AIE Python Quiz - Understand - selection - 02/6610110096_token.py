input_token = input("Enter Token number: ")
count_token = len(input_token)
token_0 = input_token.count("0")
token_1 = input_token.count("1")
if count_token - (token_0 + token_1) == 0 :
    if count_token%token_1 == token_0 :
        print("You get jackpot!!")
    else :
        print("See you next time, have a nice day.")
else :
    print("Your token is invalid")