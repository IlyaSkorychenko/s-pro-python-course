import re
from typing import Sized


def remove_marks(sentence: str) -> str:
    return re.sub(r'(?![\w\s]).', '', sentence)


def get_words(sentence: str) -> [str]:
    formatted_sentence = remove_marks(sentence)

    return formatted_sentence.split(' ')


def get_the_longest_word(words: [str]) -> Sized:
    return max(words, key=len)
