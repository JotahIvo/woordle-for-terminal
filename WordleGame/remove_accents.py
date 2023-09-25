from unicodedata import normalize

def RemoveAccent(word):
    target = normalize('NFKD', word).encode('ASCII','ignore').decode('ASCII')
    return target
