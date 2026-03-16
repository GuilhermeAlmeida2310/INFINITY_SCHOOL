word = input('Insert a word: ')
amount_vowels = 0

for letter in word:
    if letter in 'AEIOUaeiou':
        amount_vowels += 1

print(amount_vowels)