import re

exclusion_list = [("é|è|ê", 'e'), ("-|.|,|!|:|'| ", ""), ("ç", "c"), ("À|à|â", "a")]


def clean_string(value, exclusion_list_p):
    transform = []
    for letter in value:
        for rule in exclusion_list_p:
            if letter in rule[0]:
                new_value = re.sub(rule[0], rule[1], letter)
                break
            else:
                new_value = letter
        transform.append(new_value.lower())
        if "" in transform:
            transform.remove("")
    return transform


def is_palindrome(thestring):
    string_to_evaluate = clean_string(thestring, exclusion_list)
    if string_to_evaluate == string_to_evaluate[::-1] and len(thestring) != 0:
        print("{0} is a palindrome".format(thestring))
    else:
        print("{0} is not a palindrome".format(thestring))


def main():
    names_list = ['anna', 'çyril', 'Boob!', 'sébastien', '', '11', '112', '121', '@!@!@',
                  'Dans la Prairie verte, il y a une bête !', 'À Cuba, Anna a bu ça.', "À l'étape, épate-la ! "]

    for name in names_list:
        is_palindrome(name)


main()
