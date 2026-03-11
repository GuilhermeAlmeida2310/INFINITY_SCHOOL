def text_processor(text, **kwargs):
    counting_words = lambda t: len(t.split())
    counting_letters = lambda t: len(t.replace(' ',''))
    invert_text = lambda t: t[::-1]
    replace_text = lambda t, old, new: t.replace(old, new)

    if kwargs.get('counting_words'):
        print(f'Amount Words: {counting_words(text)}')
    
    if kwargs.get('counting_letters'):
        print(f'Amount Letters: {counting_letters(text)}')

    if kwargs.get('invert_text'):
        print(f'Text Inverted: {invert_text(text)}')
    
    if kwargs.get('replace_text'):
        old = kwargs.get('old_word')
        new = kwargs.get('new_word')
        print(f'Word Replaced: {replace_text(text, old, new)}')
    
text_processor('Guilherme love Java',counting_words=True)