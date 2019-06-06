#! /usr/bin/env python
# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.
#
# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.
#
# ###Arguments
#
#     First argument (required): the original string to be converted.
#     Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string.


def convert_to_title_case(s: str, exceptions="") -> str:
    """convert s to title case with exceptions"""
    converted_s = []
    for index, word in enumerate(s.split()):
        if word.lower() not in exceptions.lower().split() or index == 0:
            converted_s.append(word.title())
        else:
            converted_s.append(word.lower())
    return ' '.join(converted_s)


def test_convert_to_title_case():
    assert convert_to_title_case("this is a sentence with exceptions", "is a") == "This is a Sentence With Exceptions"
    assert convert_to_title_case("in a hole in the ground there lived a hobbit", "in a the") == "In a Hole in the Ground There Lived a Hobbit"
