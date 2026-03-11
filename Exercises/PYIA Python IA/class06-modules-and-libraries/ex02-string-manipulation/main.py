def invert_text(text):
    return text[::-1]

def counting_words(text):
    return len(text.split())

def palindrome(text):
    reverse_text = invert_text(text)
    return text == reverse_text