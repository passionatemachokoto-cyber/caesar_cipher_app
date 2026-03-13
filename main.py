def caesar_cipher(message, shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    result=""
    for char in message:
        if char.lower() in alphabet:    #check if the character is a letter
            index= alphabet.find(char.lower())
            new_index=(index+shift)%26
            new_char=alphabet[new_index]

            # keep the same letter case
            if char.isupper():
                result+=new_char.upper()
            else:
                result+=new_char
        else:
            result+=char  #preserve spaces, numbers, punctuation

    return result

def caesar_decrypt(message,shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    result=""

    for char in message:
        if char.lower() in alphabet:
            index=alphabet.find(char.lower())
            new_index=(index - shift)%26 # Subtract shift for decryption 
            new_char=alphabet[new_index]

            # Preserve original case
            if char.isupper():
                result+= new_char.upper()
            else:
                result+=new_char
        else:
            result+=char
    return result


message='Hello World!'
shift=3
encrypted=caesar_cipher(message,shift)
print(f"Encrypted text: {encrypted}")


decrypted=caesar_decrypt(encrypted,shift)
print('Decrypted:', decrypted)
