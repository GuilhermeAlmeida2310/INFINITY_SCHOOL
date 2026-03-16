word = input('Insert a word to see if it is a palindrome: ')

start = 0
end = len(word) - 1
is_palindrome = True

while start < end:
    if word[start] != word[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print('The word is a palindrome!')
else:
    print('The word is not a palindrome!')