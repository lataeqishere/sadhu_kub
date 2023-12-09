print("Select 2 options")
print(" - 1 encrypt with ROT 13")
print(" - 2 decrypt with ROT 13")
print()
option = input("Choose option: ")
if option == "1" :
    input_decrypt = input("Enter text: ")
    rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz','NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    print(f'Ciphertext is "{input_decrypt.translate(rot13)}"')
elif option == "2" :
    input_encrypt = input("Enter text: ")
    rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz','NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    print(f'Plaintext is "{input_encrypt.translate(rot13)}"')
