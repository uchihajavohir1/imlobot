from uzwords import words
from difflib import get_close_matches
from translate import to_cyrillic, to_latin
def chekword(word: str , data: list = words)-> dict:
    result = {
        'ok': True,
        'matches': []
    }
    words = word.lower()
    if words.isascii():
        words = to_cyrillic(words)
    matches = get_close_matches(words, data, 5)
    if words not in matches:
        result['ok'] = False
        if word.isascii():
            matches = [to_latin(match) for match in matches]
        result['matches'] = matches



    return result
if name == 'main':
    print(chekword("xarakat"))