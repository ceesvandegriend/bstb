worth = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}


def word_value(word: str) -> int:
    """Calculate the word value of the string."""
    # filter word
    w = [c for c in word.lower() if c in worth]
    # letter to number
    scores = [worth[c] for c in w]
    # add numbers
    scores = [int(d) for d in str(sum(scores))]

    while len(scores) > 1:
        scores = [int(d) for d in str(sum(scores))]

    return scores[0]
