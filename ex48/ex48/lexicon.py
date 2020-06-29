lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
}

def num(word):
    try:
        return int(word)
    except ValueError:
        return None

def scan(sentence):
    result = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)

        if word_type == None:
            if num(word) != None:
                result.append(('number', num(word)))
            else:
                result.append(('error', word))
        else:
            result.append((word_type, word))

    return result
