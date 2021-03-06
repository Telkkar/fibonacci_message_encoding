import random
import mpmath

from fibonacci_message_encoding import errors


def encode(secret_string, initial_n=1, wordlist=None):
    # Set decimal precision for fibonacci calculation
    mpmath.mp.dps = 5000

    if wordlist is None:
        f = open("words", "r")
        temp_wordlist = f.readlines()

        # Strip newline
        for i, word in enumerate(temp_wordlist):
            temp_wordlist[i] = word[:-1]

        wordlist = list(filter(lambda word: len(word) >= 2,
                               temp_wordlist))

    message = []
    fibonacci_values = []

    for i in range(len(secret_string)):
        fibonacci_values.append(int(mpmath.fibonacci(initial_n + i)))

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


def decode(message_list, initial_n=1):
    mpmath.mp.dps = 5000

    secret = []
    fibonacci_values = []

    for i in range(len(message_list)):
        fibonacci_values.append(int(mpmath.fibonacci(initial_n + i)))

    for i, word in enumerate(message_list):
        position = (fibonacci_values[i] - 1) % len(word)
        secret_character = word[position]

        secret.append(secret_character)

    return secret
