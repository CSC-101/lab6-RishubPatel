import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def book_index_smallest_from(values: list[data.Book], start: int) -> Optional[int]: #returns the index of the first alphabetical Book from a given list of Books
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title.lower() < values[mindex].title.lower():
            mindex = idx

    return mindex

def selection_sort_books(values: list[data.Book]) -> None: #alphabetically sorts a given list of Books by title
    for idx in range(len(values) - 1):
        mindex = book_index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 2

def swap_case(string: str) -> str: #Swaps case (upper/lower) for letters in a string
    return "".join([(character.upper() if character.islower() else character.lower()) if character.isalpha() else character for character in string])

# Part 3

def str_translate(string: str, old:str, new:str) -> str: #swaps all old characters with the new character from a given string
    return "".join([new if char == old else char for char in string])

# Part 4

def histogram(string: str) -> dict: #lists the number of times each word in a given string is in the string
    word_list = string.split()
    counts = {word : 0 for word in word_list}
    for word in word_list:
        counts[word] += 1
    return counts