VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Part A: WOFPlayer

# We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. Every instance of WOFPlayer has three instance variables:

# .name: The name of the player (should be passed into the constructor)

# .prizeMoney: The amount of prize money for this player (an integer, initialized to 0)

# .prizes: The prizes this player has won so far (a list, initialized to [])

# Of these instance variables, only name should be passed into the constructor.

# It should also have the following methods (note: we will exclude self in our descriptions):

# .addMoney(amt): Add amt to self.prizeMoney

# .goBankrupt(): Set self.prizeMoney to 0

# .addPrize(prize): Append prize to self.prizes

# .__str__(): Returns the player’s name and prize money in the following format:
# Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)

# Write the WOFPlayer class definition (part A) here


class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print("{} has ${}".format(self.name, self.prizeMoney))
        print("Category: {}".format(category))
        print("Phrase: {}".format(obscuredPhrase))
        print("Guessed: {}".format(guessed))
        move = input(
            "Guess a letter, phrase, or type 'exit' or 'pass': ").upper()
        return move


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        letters = []
        for l in LETTERS:
            if l not in guessed:
                letters.append(l)
        if self.prizeMoney < VOWEL_COST:
            for l in VOWELS:
                letters.remove(l)
        return letters

    def getMove(self, category, obscuredPhrase, guessed):
        letters = self.getPossibleLetters(guessed)
        if self.smartCoinFlip():
            for l in letters:
                if l in self.SORTED_FREQUENCIES:
                    return l
        else:
            return random.choice(letters)
