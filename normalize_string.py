import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_strings(strings):
        results = []
        for string in strings:
            string = string.strip()
            string = re.sub('[!#?]', '', string)
            string = string.title()
            results.append(string)

        return results


result = clean_strings(states)
print(result)


def remove_specialchar(string):
    string = re.sub('[!#?]', '', string)

    return string


def clean_strings2(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)

        results.append(string)

    return results


results = clean_strings2(states, str.strip, str.title, remove_specialchar)
print(results)
