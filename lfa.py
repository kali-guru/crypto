alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
atbash = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

text = input("Enter ciphertext: ").upper()

frequency = {}

for c in alphabet:
    frequency[c] = text.count(c)

letters = list(alphabet)

for i in range(26):
    for j in range(i + 1, 26):
        if frequency[letters[j]] > frequency[letters[i]]:
            letters[i], letters[j] = letters[j], letters[i]

print("\nLetter Frequency:")
for c in letters:
    if frequency[c] > 0:
        print(c, "=", frequency[c])

result = ""

for c in text:
    if c in alphabet:
        result += atbash[alphabet.index(c)]
    else:
        result += c

print("\nDecrypted Text:")
print(result)