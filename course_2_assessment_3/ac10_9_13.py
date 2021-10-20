# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have
# seen that word.


sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

wrd_d = {}

sent_lst = sent.split()

for word in sent_lst:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] = wrd_d[word] + 1

print(wrd_d)
