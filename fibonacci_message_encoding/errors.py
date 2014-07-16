
class NoSuitableWord(Exception):
    def __init__(self, char):
        self.unsuitable_character = char
        self.msg = "No suitable word for '" + self.unsuitable_character + "' character"

    def __str__(self):
        return repr(self.unsuitable_character)

    def message(self):
        return self.msg