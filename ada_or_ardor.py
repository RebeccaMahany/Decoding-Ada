# Rebecca Mahany
# Decoding Van and Ada's coded messages

# Imports
import string, sys, re

# Consts
VERSION_ALPHABETIC = 0
VERSION_POEM = 1
POEM_GARDEN = 'garden'
POEM_MEMOIRE = 'memoire'


# Read in and clean poem.
# Poem must be a list of lines, each line with no spaces or punctuation in it.
def get_poem(poem):
    with open(poem + '.txt', 'r') as poem_file:
        poem_lines = poem_file.readlines()
        poem_lines_clean = [re.sub(r'\W+', '', line.lower()) for line in poem_lines]
        # TODO deal with French accents?
        return poem_lines_clean


# Determine which of the codes is in use: the first alphabetic version, or the
# later poem-based version.
def determine_version(word):
    poem_match = re.match(r'(L|l)\d+\.(\d+\.)*(\d+)*', word)
    if poem_match == None:
        return VERSION_ALPHABETIC
    return VERSION_POEM


# Determine which of the codes are in use. Lowercase first letter denotes
# Garden; uppercase first letter denotes Mémoire.
def determine_poem(word):
    if word[0].islower():
        return POEM_GARDEN
    return POEM_MEMOIRE


# Decoding version one of Van and Ada's code--an alphabetic code
def alphabetic_decode(word_list):
    decoding_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    word_list_out = []
    for encoded_word in word_list:
        word_len = len(encoded_word)
        if word_len == 1:
            # One-letter words are not encoded
            word_list_out.append(encoded_word)
            continue

        decoded_word = ''
        for char in encoded_word:
            if char.islower():
                char_index = string.ascii_lowercase.index(char)
            else:
                char_index = string.ascii_lowercase.index(char.lower()) + 26

            decoded_word += decoding_alphabet[char_index - word_len]

        word_list_out.append(decoded_word)

    return(word_list_out)


# Decoding version two of Van and Ada's code--a code based on one of two poems
def poem_decode(word_list):
    # Determine which poem we need to use to decode
    decoding_poem = determine_poem(word_list[0])
    decoding_poem_lines = get_poem(decoding_poem)

    word_list_out = []
    for encoded_letter in word_list:
        cleaned_encoded_letter = encoded_letter.lstrip('Ll')
        cleaned_encoded_letter = cleaned_encoded_letter.rstrip('.') # We don't need the final period
        pieces = cleaned_encoded_letter.split('.')
        if len(pieces) < 2:
            sys.exit('input contains an encoded letter that does not include a character identifier: ' + encoded_letter)

        # The first number is always the line number
        line_num = int(pieces.pop(0))

        if len(decoding_poem_lines) - 1 < line_num:
            sys.exit('input contains an encoded letter that calls for a line number out of bounds for this poem: ' + encoded_letter)

        # The remaining 1 (or more) numbers indicates the character on that line
        for char_num in pieces:
            char_num = int(char_num)
            word_list_out.append(decoding_poem_lines[line_num - 1][char_num - 1])

    return(word_list_out)


# Main method: opens file, decodes text
def main():
    # Check correctness of command line args
    if len(sys.argv) != 2:
        print('Usage: python ada_or_ardor.py text_file')
        return

    # Read in encoded text
    with open(sys.argv[1], 'r') as encoded_file:
        encoded = encoded_file.read()
        encoded.rstrip()
        encoded_words = encoded.split()

    # Decode words properly, according to their type of code
    version = determine_version(encoded_words[0])
    if version == VERSION_ALPHABETIC:
        decoded_words = alphabetic_decode(encoded_words)
    elif version == VERSION_POEM:
        decoded_words = poem_decode(encoded_words)

    # Reassemble decoded words into string to print
    decoded = ' '.join(decoded_words)
    print(decoded)


if __name__ == '__main__':
    main()

