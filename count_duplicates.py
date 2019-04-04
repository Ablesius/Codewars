#! /usr/bin/env python
# Count the number of Duplicates
# 
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
#
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


def count_duplicate_characters(input_string):
    count = 0
    normalized_string = input_string.lower()
    for char in set(normalized_string):
        if normalized_string.count(char) > 1:
            count += 1
    return count


def count_duplicates(input_string):
    """More concise version"""
    return len([char for char in set(input_string.lower()) if input_string.lower().count(char) > 1])
