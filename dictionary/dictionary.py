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


def values():
    values = []
    for i in range(len(dictionary)):
        values.append(dictionary[i][keys()[i]])
    return values


def translate_to_hun(eng_word):
    return keys()[values().index(eng_word)]


def translate_to_eng(hun_word):
    return dictionary[keys().index(hun_word)][hun_word]

add_word("citrom", "lemon")
print(dictionary)

print(translate_to_hun("lemon"))