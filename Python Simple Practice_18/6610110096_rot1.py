up_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_char = "abcdefghijklmnopqrstuvwxyz"
input_char = input("Enter 5 characters: ")
char_trans = str.maketrans(up_char + low_char,up_char[2:]+up_char[0] + low_char[2:]+low_char[0])
lower_char = input_char.lower()
print("Ciphertext is",lower_char.translate(char_trans))