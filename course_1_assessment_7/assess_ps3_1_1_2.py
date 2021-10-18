# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the
# same letter, including one-letter words. Store the result in the variable same_letter_count.

# Hard-coded answers will receive no credit.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count = 0

sentence_lst = sentence.split()

for word in sentence_lst:
    if word[-1] == word[0]:
        same_letter_count += 1
    elif len(word) == 1:
        same_letter_count += 1
