def encryption(text, s):
    s = int(s)
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char == ' ':
            result += ' '
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decryption(text, s):
    s = int(s)
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char == ' ':
            result += ' '
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

def main():
    print('Select the task number:')
    print('1. Encryption')
    print('2. Decryption')
    x = input('Enter the task number: ')
    if x == '1':
        text = input('Enter the text: ')
        s = input('Enter the key: ')
        print('Encrypted text:', encryption(text, s))
        y = input('Do you want to start the decryption process? (Yes/No): ').strip().lower()
        if y == 'yes':
            print('Decrypted text:', decryption(encryption(text, s), s))
        else:
            print('Exiting the platform. Thank you.')
    else:
        text = input('Enter the encrypted text: ')
        s = input('Enter the key: ')
        print('Decrypted text:', decryption(text, s))

main()
