from random import choice
import sys


def open_and_read_file(file_path1, file_path2):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    og_1 = open(file_path1).read()
    og_2 = open(file_path2).read()
    # your code goes here
    og_text = (og_2, og_1)

    return og_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}


    words = []

    for string in text_string:

        for word in string.split():
            words.append(word)
        # your code goes here
        for index, word in enumerate(words[:-2]):
            key = (word, words[index+1])
            value = words[index+2]
            if key in chains:
                chains[key].append(value)
            else:
                chains[key] = [value]
            # print key, value

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    
    # makes sure the first key starts with an upper case. 
    key = ("place", "holder")
    while not key[0][0].isupper():
        key = choice(chains.keys())

    while key in chains:
        if text == "":
            # unpacking the key 
            word1, word2 = key
            word3 = choice(chains[key])
            if word1[0].isupper():
                # adds words to text 
                text = word1 + " " + word2 + " " + word3
            else:
                continue

        else:
            # rebbinding key to the second and third words
            key = (word2, word3)
            # verifying that the new key is in chains
            if key in chains:
                # re-binding the third word to the second
                word2 = word3
                # binds word three to a random value from the key
                word3 = choice(chains[key])
                # adds new word to end of text     
                text = text + " " + word3
            
            else:
                continue
    text = text[:140]

    # assigns a variable to the index of rightmost position of the punctuation
    exclamation = text.rfind("!")
    question = text.rfind("?")
    period = text.rfind(".")

    # find the senctence ending punctuation that is the farthest right and removes everything to the left of it.
    if exclamation > question and exclamation > period:
        text = text[:exclamation + 1]
    elif question > exclamation and question > period:
        text = text[:question + 1]
    elif period > question and period > exclamation:
        text = text[:period +1]
    else:
        make_text(chains)
    
    return text


input_path1 = sys.argv[1]
input_path2 = sys.argv[2]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path1, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
