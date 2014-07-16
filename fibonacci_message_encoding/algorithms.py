import random

from fibonacci_message_encoding import errors

def encode(secret_string, wordlist=None):
    if wordlist is None:
        f = open("words", "r")
        temp_wordlist = f.readlines()

        # Strip newline
        for i, word in enumerate(temp_wordlist):
            temp_wordlist[i] = word[:-1]

        wordlist = list(filter(lambda word: len(word) >= 2,
                               temp_wordlist))

    message = []

    # Generate fibo values V_m_n using m_0
    # TODO: add possibility of calculating closed-form fibo numbers using starting position
    fibonacci_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]

    for i, char in enumerate(secret_string):
        suitable_words = list(filter(lambda word: word[(fibonacci_values[i] - 1) % len(word)] is char,
                                     wordlist))
        
        if len(suitable_words) == 0:
            raise errors.NoSuitableWord(char)

        # Select random suitable word
        #random.seed(1)
        word = suitable_words[random.randrange(0, len(suitable_words))]

        message.append(word)

    return message


def decode(message_list):
    secret = []

    # Generate fibo values V_m_n using m_0
    # TODO: add possibility of calculating closed-form fibo numbers using starting position
    fibonacci_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]

    for i, word in enumerate(message_list):
        position = (fibonacci_values[i] - 1) % len(word)
        secret_character = word[position]

        secret.append(secret_character)

    return secret
