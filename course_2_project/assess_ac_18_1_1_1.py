# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv
# which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet.
# We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and
# negative_words.txt.

# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score
# (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and
# the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the
# Net Score vs Number of Retweets.

# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word,
# and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return(word)


print(strip_punctuation("Apple!!#@;"))
