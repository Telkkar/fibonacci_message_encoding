from fibonacci_message_encoding import errors

def encode(secret_string, wordlist=[]):
    # TODO: wordlist is not intended for production
    message = []

    # Generate fibo values V_m_n using m_0
    # TODO: add possibility of calculating closed-form fibo numbers using starting position
    fibonacci_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    for i, char in enumerate(secret_string):
        suitable_words = filter(lambda word: word[(fibonacci_values[i] - 1) % len(word)] is char,
                                wordlist)

        try:
            message.append(next(suitable_words))
        except StopIteration:
            raise errors.NoSuitableWord(char)

    return message


def decode(message_list):
    secret = []

    # Generate fibo values V_m_n using m_0
    # TODO: add possibility of calculating closed-form fibo numbers using starting position
    fibonacci_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    for i, word in enumerate(message_list):
        position = (fibonacci_values[i] - 1) % len(word)
        secret_character = word[position]

        secret.append(secret_character)

    return secret
