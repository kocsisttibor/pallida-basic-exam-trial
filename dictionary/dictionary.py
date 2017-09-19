dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(hun_word, eng_word):
    new_dict = {}
    new_dict[hun_word] = eng_word
    dictionary.append(new_dict)


# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'

def keys():
    keys = []
    for i in range(len(dictionary)):
        keys.append(list(dictionary[i].keys())[0])
    return keys


def translate_to_hun(eng_word):
    pass


def translate_to_eng(hun_word):
    return dictionary[keys().index(hun_word)][hun_word]

