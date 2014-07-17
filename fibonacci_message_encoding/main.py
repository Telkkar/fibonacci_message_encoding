from fibonacci_message_encoding import algorithms, errors


def main():
    print("Choices:")
    print("\t 1: Encode custom secret")
    print("\t 2: Encode \"william\"")

    choice = eval(input("Choice: "))

    if choice == 1:
        custom_encode()
    elif choice == 2:
        print("Encoding \"william\" as a list of words")
        print(algorithms.encode("william"))

        print("Decoding the encode of william: ")
        decoded = algorithms.decode(["why", "ignites", "sleep", "bold", "heroic", "aura", "mail"])
        print("\t" + "".join(decoded))


def custom_encode():
    print()
    secret = input("Enter secret to encode: ")
    initial = int(input("Enter initial spot in fibonacci sequence: "))

    print("Encoded secret:")
    encoded = algorithms.encode(secret, initial)
    print("\t" + str(encoded))

    print("Decoded message without initial spot:")
    decoded_without_initial = algorithms.decode(encoded)
    print("\t" + "".join(decoded_without_initial))

    print("Decoded message with initial spot:")
    decoded = algorithms.decode(encoded, initial)
    print("\t" + "".join(decoded))



if __name__ == "__main__":
    main()