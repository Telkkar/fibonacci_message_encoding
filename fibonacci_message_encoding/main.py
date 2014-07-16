import string

# Pseudocode

## Encode
def encode(secret_string, wordlist=[]):
    # TODO: wordlist is not intended for production
    message = []

    # Generate fibo values V_m_n using m_0
    # TODO: add possibility of calculating closed-form fibo numbers using starting position
    fibonacci_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    for i, char in enumerate(secret_string):
        suitable_words = filter(lambda word: word[(fibonacci_values[i] - 1) % len(word)] is char,
                                wordlist)

        # TODO: Catch StopIteration (meaning that there are no suitable words)
        message.append(next(suitable_words))

    return message


## Decode
def decode(message_list):
    secret = []

    # Generate fibo values V_m_n using m_0
    # TODO: add possibility of calculating closed-form fibo numbers using starting position
    fibonacci_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    for i, word in enumerate(message_list):
        # Find char s_n at position p where
        # p = (V_m_n - 1) mod length(w_n)
        #position = divmod((fibonacci_values[i] - 1), len(word))
        position = (fibonacci_values[i] - 1) % len(word)
        secret_character = word[position]

        secret.append(secret_character)

    return secret


def main():
    print("Encoding \"william\"")
    print(encode("william", wordlist=["why", "ignites", "sleep", "bold", "heroic", "aura", "mail"]))

    print("Decoding the encode: ", end='')
    decoded = decode(["why", "ignites", "sleep", "bold", "heroic", "aura", "mail"])
    print("".join(decoded))

if __name__ == "__main__":
    main()