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


# list of tweets scores, replies and retweets by count
#! My preferred way of doing it using next(), but their interpreter would allow it. 👇🏼
results = []
# with open("project_twitter_data.csv") as tweet_f:
#     next(tweet_f)
#     for line in tweet_f:
#         retweet_count = line.split(",")[1]
#         reply_count = line.split(",")[2].replace("\n", "")
#         poss_count = get_pos(line)
#         neg_count = get_neg(line)
#         net_score = poss_count - neg_count
#         temp_tupl = (retweet_count, reply_count,
#                      poss_count, neg_count, net_score)
#         results.append(temp_tupl)
#         print("Retweet Count: {}, Reply Count: {}, Positive:{}, Negative:{}, Net Score:{}".format(
#             retweet_count, reply_count, poss_count, neg_count, net_score))

tweet_f = open("project_twitter_data.csv", "r")
lines = tweet_f.readlines()
for line in lines[1:]:
    retweet_count = line.split(",")[1]
    reply_count = line.split(",")[2].replace("\n", "")
    poss_count = get_pos(line)
    neg_count = get_neg(line)
    net_score = poss_count - neg_count
    temp_tupl = (retweet_count, reply_count,
                 poss_count, neg_count, net_score)
    results.append(temp_tupl)
    print("Retweet Count: {}, Reply Count: {}, Positive:{}, Negative:{}, Net Score:{}".format(
        retweet_count, reply_count, poss_count, neg_count, net_score))

print(results)

# Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score

with open("resulting_data.csv", "w") as result_f:
    # Header row
    result_f.write(
        "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    result_f.write("\n")
    # Each of the rows
    for result in results:
        row_string = "{},{},{},{},{}".format(
            result[0], result[1], result[2], result[3], result[4])
        result_f.write(row_string)
        result_f.write("\n")
