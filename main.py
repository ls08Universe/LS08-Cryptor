def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha(): 
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        elif char.isdigit(): 
            shifted = ord(char) + shift
            if shifted > ord('9'):
                shifted -= 10 
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha(): 
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_message += chr(shifted)
        elif char.isdigit():  
            shifted = ord(char) - shift
            if shifted < ord('0'):
                shifted += 10 
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

def get_input():
    choice = input("Do you want to encode or decode? (Enter 'encode' or 'decode'): ").lower()
    if choice == 'encode':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        return caesar_cipher_encrypt(message, shift)
    elif choice == 'decode':
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        return caesar_cipher_decrypt(encrypted_message, shift)
    else:
        print("Invalid choice! Please enter 'encode' or 'decode'.")
        return get_input()

ascii_art = """

┓ ┏┓┏┓┏┓  ┏┓           
┃ ┗┓┃┫┣┫  ┃ ┏┓┓┏┏┓╋┏┓┏┓
┗┛┗┛┗┛┗┛  ┗┛┛ ┗┫┣┛┗┗┛┛ 
               ┛┛      
 
"""
if __name__ == "__main__":
    print(ascii_art)
    while True:
        result = get_input()
        print("Result:", result)
        another = input("Do you want to create another encryption or decryption? (Enter 'yes' or 'no'): ").lower()
        if another != 'yes':
            break
