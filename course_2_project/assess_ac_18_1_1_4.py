# Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake
# generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from
# the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called
# resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy
# words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score
# (how positive or negative the text is overall) for each tweet. The file should have those headers in that order.
# Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and
# produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re
# accessing this textbook from Coursera.
import csv


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
            positive_count += 1
    return(positive_count)


def get_neg(sentence):
    negative_count = 0
    sentence = strip_punctuation(sentence)
    sentence_lst = sentence.lower().split()
    for word in sentence_lst:
        if word in negative_words:
            negative_count += 1
    return(negative_count)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# dictionary of tweets
with open("project_twitter_data.csv") as tweet_f:
    next(tweet_f)
    for line in tweet_f:
        poss_lines = get_pos(line)
        neg_lines = get_neg(line)
        print("Positive:{}, Negative:{}".format(poss_lines, neg_lines))

results = {}
with open("project_twitter_data.csv") as tweet_f:
    next(tweet_f)
    for line in tweet_f:
        retweet_count = line[-4].replace(",", "")
        reply_count = line[-2].replace(",", "")
        poss_lines = get_pos(line)
        neg_lines = get_neg(line)
        print("Retweet Count: {}, Reply Count: {}, Positive:{}, Negative:{}".format(
            retweet_count, reply_count, poss_lines, neg_lines))
