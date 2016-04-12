from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    og_text = open(file_path).read()

    # your code goes here

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

    # end = len(words)
    for word in text_string.split():
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
    
   
    key = choice(chains.keys())
    while key in chains:
        if text == "":
            # unpacking the key 
            word1, word2 = key
            word3 = choice(chains[key])
            # adds words to text 
            text = word1 + " " + word2 + " " + word3
            

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
           
    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
