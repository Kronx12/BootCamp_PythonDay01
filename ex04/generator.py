import numpy as np


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        print("ERROR")
    elif (option is not None and option != "shuffle"
          and option != "orderer" and option != "unique"):
        print("ERROR")
    else:
        words = text.split(sep)
        if option == "shuffle":
            np.random.shuffle(words)
            for i in words:
                yield i
        elif option == "orderer":
            words.sort()
            for i in words:
                yield i
        elif option == "unique":
            for i in list(set(words)):
                yield i
        else:
            for i in words:
                yield i
