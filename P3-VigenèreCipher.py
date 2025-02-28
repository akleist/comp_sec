import sys
from collections import defaultdict

def main():
    
    if len(sys.argv) != 3:
        print("Usage: vigenèreCipherCrack.py <key> <'plaintext'>")
        exit(1)

    key = sys.argv[1]
    plaintext = sys.argv[2].upper()
    print(plaintext)

    index = 0
    keyLength = len(key)
    ciphertext = ""
    for letter in plaintext:
        if letter != " ":
            cipherLetter = (ord(letter) + ord(key[index]) - 2*65) % 26 + 65
            ciphertext += chr(cipherLetter)
        
            index += 1
            index %= keyLength
        else: ciphertext += " "

    print(ciphertext)

if __name__ == '__main__':
    main()
