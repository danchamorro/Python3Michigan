# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a
# string which represents one or more sentences, and calculates how many words in the string are considered negative words.
# Use the list, negative_words to determine what words will count as negative. The function should return a positive
# integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are
# lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return(word)


def get_pos(sentence):
    positive_count = 0
    sentence = strip_punctuation(sentence)
    sentence_lst = sentence.lower().split()
    for word in sentence_lst:
        if word in positive_words:
            print(word)
            positive_count += 1
    return(positive_count)


def get_neg(sentence):
    negative_count = 0
    sentence = strip_punctuation(sentence)
    sentence_lst = sentence.lower().split()
    for word in sentence_lst:
        if word in negative_words:
            print(word)
            negative_count += 1
    return(negative_count)
