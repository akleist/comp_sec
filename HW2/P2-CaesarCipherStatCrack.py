import sys
from collections import defaultdict

englishFreq = {
    "A": 0.080, "B": 0.015, "C": 0.030, "D": 0.040, "E": 0.130, "F": 0.020, "G": 0.015,
    "H": 0.060, "I": 0.065, "J": 0.005, "K": 0.005, "L": 0.035, "M": 0.030, "N": 0.070,
    "O": 0.080, "P": 0.020, "Q": 0.002, "R": 0.065, "S": 0.060, "T": 0.090, "U": 0.030,
    "V": 0.010, "W": 0.015, "X": 0.005, "Y": 0.020, "Z": 0.002
}

def getFrequency(ciphertext):
    freq = defaultdict(int)
    for letter in ciphertext:
        freq[letter] += 1

    return freq

def calculateCorrelation(key, cipherFreq):
    correlationSum = 0
    for letter in cipherFreq:
        letterIndex = (ord(letter) - key - 65 + 26) % 26 + 65
        letterCorrelation = cipherFreq[letter]*englishFreq[chr(letterIndex)]
        correlationSum += letterCorrelation

    return correlationSum

def findKey(cipherFreq):

    keyCorrelation = {}
    for i in range(26):
        keyCorrelation[i] = calculateCorrelation(i, cipherFreq)
        print(f'phi({i}): {keyCorrelation[i]:.3}')

    print()

    keys = []
    for _ in range(4):
        maximum = max(keyCorrelation, key=keyCorrelation.get)
        keys.append(maximum)
        del keyCorrelation[maximum]

    return keys

def decrypt(key, ciphertext):
    plaintext = ""
    for i, letter in enumerate(ciphertext):
        newLetter = (ord(letter) - key - 65 + 26) % 26 + 65
        plaintext += chr(newLetter)

    return(plaintext)

def main():

    if len(sys.argv) != 2:
        print("Usage: CaesarCipherStatCrack.py <cyphertext>")

    ciphertext = sys.argv[1].strip().upper()

    cipherFreq = getFrequency(ciphertext)

    total = len(ciphertext)
    for f in cipherFreq:
        cipherFreq[f] /= total

    keys = findKey(cipherFreq)

    plaintext = decrypt(keys[0], ciphertext)
    print(f'Most likely key: {keys[0]}')
    print(f'Decrypted message: {plaintext}') 

    print()
    print("Next most likely keys:")
    for key in keys[1:]:
        plaintext = decrypt(key, ciphertext)
        print(f'Key {key} results in plaintext: {plaintext}') 

if __name__ == '__main__':
    main()
