up_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_char = "abcdefghijklmnopqrstuvwxyz"
en_meth = str.maketrans(up_char + low_char, up_char[::-1]+ low_char[::-1])
input_char = input("Enter 5 characters: ")
encrypted = input_char.translate(en_meth)
print("Encryption is",encrypted.lower())