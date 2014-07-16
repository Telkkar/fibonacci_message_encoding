from fibonacci_message_encoding import algorithms, errors

def main():
    print("Encoding \"william\" as a list of words")
    print("\t", end = "")
    print(algorithms.encode("william", wordlist=["why", "ignites", "sleep", "bold", "heroic",
                                                 "aura", "mail"]))
    print()

    print("Encoding \"william\" using an empty dictionary")
    try:
        print("\t" + algorithms.encode("william"))
    except errors.NoSuitableWord as nsw:
        print("\t" + nsw.message())
    print()

    print("Decoding the encode of william: ")
    decoded = algorithms.decode(["why", "ignites", "sleep", "bold", "heroic", "aura", "mail"])
    print("\t" + "".join(decoded))

if __name__ == "__main__":
    main()