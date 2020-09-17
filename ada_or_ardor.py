# Rebecca Mahany
# Decoding Van and Ada's coded messages

# Imports
import sys


# TODO description
# TODO deal w French accents
# Parse poems by line
def get_poems():
    poems = {}
    for poem in ["garden", "memoire"]:
        with open(poem + ".txt", 'r') as poem_file:
            poem_lines = poem_file.readlines()
            poem_lines_clean = [line.rstrip() for line in poem_lines]
            poems[poem] = poem_lines_clean
    return poems


# Determine which of the two codes are in use
def determine_version(word):
    return(1)


# Decoding version one of Van and Ada's code--an alphabetic code
def v1_decode(word_list):
    return(word_list)


# Version two of Van and Ada's code--a code based on one of two poems
def v2_decode(word_list):
    return(word_list)


# Main method: opens file, decodes text
def main():

    # For now--read in poems each time and format them.
    # TODO possibly replace with hardcoded arrays in this file to avoid doing this multiple times
    poems = get_poems()

    # Check correctness of command line args
    if len(sys.argv) != 2:
        print("Usage: python ada_or_ardor.py text_file")
        return

    # Read in encoded text
    with open(sys.argv[1], 'r') as encoded_file:
        encoded = encoded_file.read()
        encoded.rstrip()
        encoded_words = encoded.split()

    # Decode words properly, according to their type of code
    version = determine_version(encoded_words[0])
    if version == 1:
        decoded_words = v1_decode(encoded_words)
    elif version == 2:
        decoded_words = v2_decode(encoded_words)

    # Reassemble decoded words into string to print
    decoded = " ".join(decoded_words)
    print(decoded)


if __name__ == '__main__':
    main()
