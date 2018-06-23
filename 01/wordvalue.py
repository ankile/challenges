from data import DICTIONARY, LETTER_SCORES
from collections import namedtuple
import json
from functools import reduce
import os

WordScore = namedtuple('WordScore', 'word score')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_words() -> object:
    """
    Load dictionary into a list and return list
    """
    with open(DICTIONARY, 'r') as f:
        return f.read().split('\n')


def calc_word_value(word):
    """
    Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES
    """
    return reduce(
        lambda accum, char: accum + LETTER_SCORES.get(char.upper(), 0),
        list(word), 0
    )


def calc_word_value2(word):
    """
    Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES
    """
    result: int = 0
    for letter in word.upper():
        result += LETTER_SCORES.get(letter, 0)
    return result


def max_word_and_value(words=load_words()):
    """
    Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    """
    current_max = 0
    current_word = ''
    for word in words:
        score = calc_word_value(word)
        if score > current_max:
            current_max = score
            current_word = word
    return WordScore(current_word, current_max)


def max_word_value(words=load_words()):
    """
    Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    """
    current_max = 0
    current_word = ''
    for word in words:
        score = calc_word_value(word)
        if score > current_max:
            current_max = score
            current_word = word
    return current_word


def calculate_all_scores(words=load_words()):
    return {word: calc_word_value(word) for word in words}


def dump_words_to_file_json(name, words=load_words()):
    word_count = len(words)
    print(f'Starting writing to file {name}')
    with open(name, 'w') as f:
        for i in range(0, len(words), 1000):
            f.writelines(json.dumps(calculate_all_scores(words[i:i + 1001]), indent=4))
            clear()
            print(f'{i + 1000}/{word_count} words written to file...')

    clear()
    print(f'Done writing {word_count} words to file {name}')


if __name__ == "__main__":
    print('book', calc_word_value('book'))
    load_words()
    word_score = max_word_and_value(['book', 'machine', 'computer'])
    return_string = (
        f'{word_score.word.capitalize()} was the best word with '
        f'{word_score.score} points'
    )
    print(return_string)
    word_scores = json.dumps(
        calculate_all_scores(['book', 'machine', 'computer', 'imperative']),
        indent=4,
    )
    print(word_scores)

    filename = 'dictionary_json.txt'
    dump_words_to_file_json(filename)
