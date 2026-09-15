import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

############################################################
# Custom Types
# NOTE: You do not need to modify these.

"""
You can think of the keys of the defaultdict as representing the positions in
the sparse vector, while the values represent the elements at those positions.
Any key which is absent from the dict means that that element in the sparse
vector is absent (is zero).
Note that the type of the key used should not affect the algorithm. You can
imagine the keys to be integer indices (e.g., 0, 1, 2) in the sparse vectors,
but it should work the same way with arbitrary keys (e.g., "red", "blue", 
"green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problem 5a

def find_longest_lexicographically_first_word(text: str) -> str:
    """
    Given a string |text|, return the longest word in |text|.
    If multiple words have the same maximum length, return the one
    that comes first lexicographically.

    A word is defined by a maximal sequence of characters without whitespaces.

    If |text| is empty, you may return an empty string.
    """
    # BEGIN_YOUR_CODE
    text += " "

    maxLength = 0
    curLength = 0
    maxText = ""
    curText = ""

    for i in range(len(text)):        
        if(text[i] == " "):
            if(curLength > maxLength):
                maxLength = curLength
                maxText = curText
            
            elif(curLength == maxLength):
                if(maxLength > curLength):
                    maxText = curText  
            curLength = 0
            curText = ""

        else:
            curLength += 1
            curText += text[i]

    return maxText
    # END_YOUR_CODE

############################################################
# Problem 5b

def manhattan_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Manhattan distance (L1 distance) between two locations,
    where the locations are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    # END_YOUR_CODE


############################################################
# Problem 5c

def mutate_sentences(sentence: str) -> List[str]:
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence),
      - the first word is the same as the first word of the original sentence,
      - the last word is the same as the last word of the original sentence.
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
    Example:
      - Input: 'the red the blue the end'
      - Output: ['the red the blue the end', 'the blue the red the end',
                 'the red the red the end', 'the blue the blue the end']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    # END_YOUR_CODE


############################################################
# Problem 5d

def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Given two sparse vectors (vectors where most of the elements are zeros)
    |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.

    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    result = 0;
    for key, value in v2.items():
        result += v1[key]*value
    return result
    # END_YOUR_CODE


############################################################
# Problem 5e

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector,
) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scale is zero, you are allowed to modify v1 to include any
    additional keys in v2, or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for key, value in v2.items():
        v1[key] += value*scale
    # END_YOUR_CODE


############################################################
# Problem 5f

def find_most_frequent_words(text: str) -> Set[str]:
    """
    Split the string |text| by whitespace and return the set of word(s)
    that achieve the maximum frequency in the text.

    If |text| is an empty string, return the empty set.

    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 7 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE
