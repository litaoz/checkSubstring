listOfWords1 = [
    "nutarian"
    "convict",
    "glove",
    "grow",
    "crime"
]

listOfWords2 = [
    "nutarian"
    "convict",
    "glove",
    "grow",
    "crime",
    "crimefighter",
    "acrime"
]

listOfWords3 = [
    "nutarian"
    "convict",
    "glove",
    "grow",
    "lot",
    "allot"
]

listOfWords4 = [
    "nutarian"
    "convict",
    "glove",
    "grow",
    "no",
    "another"
]


def substringInList(wordList):
    seen = set()

    for word in wordList:
        if word in seen:
            return True
        for comparison in seen:
            if word in comparison or comparison in word:
                return True
        seen.add(word)

    return False


def main():
    '''
    This function will go through a list of words 
    and find if any of the words in the list is a subset of different word in the list
    '''
    a1 = substringInList(listOfWords1)
    a2 = substringInList(listOfWords2)
    a3 = substringInList(listOfWords3)
    a4 = substringInList(listOfWords4)

    print("1: ", a1)
    print("2: ", a2)
    print("3: ", a3)
    print("4: ", a4)


if __name__ == "__main__":
    main()
