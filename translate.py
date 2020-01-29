import json
from difflib import get_close_matches


dicts = json.load(open('JSON.dictionary', 'r'))


def translator(entry):
    entry = entry.lower()
    if entry in dicts:
        return dicts[entry]

    elif entry.title() in dicts:
        return dicts[entry.title()]

    elif entry.upper() in dicts:
        return dicts[entry.upper()]

    elif len(get_close_matches(entry, dicts.keys())) > 0:
        yes_no = input(f'Did you mean {get_close_matches(entry, dicts.keys())[0]}?  Enter Y if yes or N if no.')
        if yes_no == 'Y':
            return dicts[get_close_matches(entry, dicts.keys())[0]]
        else:
            return f'{entry} is either not in our dictionary or simply not a real word.'

    else:
        return f'{entry} is not in our dictionary.  Please check your spelling.'


word = input('Please enter a word ')
output = translator(word)

if type(output) == list:
    for word in output:
        print(word)
else:
    print(output)