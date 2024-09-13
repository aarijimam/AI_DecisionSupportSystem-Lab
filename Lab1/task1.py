import numpy as np


def pig_latin(text):
    # check whitespace
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    word_array = text.split(" ")
    for i, word in enumerate(word_array):
        if word[0] in vowels:
            word_array[i] = word + 'hay'
        else:
            word_array[i] = word[1:] + word[0] + 'ay'

    return ' '.join(word_array)


if __name__ == '__main__':
    input_string = input("Enter a string: ")
    print(pig_latin(input_string))
