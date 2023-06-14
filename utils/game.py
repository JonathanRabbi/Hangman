class Hangman:
    def__init__(self):
        self.word_to_find = ["becode"]
        self.lives = 5
        self.correctly_guessed_letters = ["_" for letter in self.word_to_find] #list the letters that the player had correctly guessed
        self.wrongly_guessed_letters = [] # this will list the letters that the player had wrong
        self.guesses=[] # this will list the letters that the player has attempted
        self.turn_count = 0 # this will add the amount of turns the player took
        self.error_count = 0 # this will add the amount of times the player was wrong
    
    def play(self):
        while True:
            letter = input("Guess a letter:")
            if not letter.isalpha() or len(letter)!=1:
                print("Please enter 1 letter.")
                continue #the player must insert a letter not a number
            self.guesses.append(letter) #after picking a random letter, the letter will be stored in the list of guessed attribute
            
            if letter in self.word_to_find:
                for i in range(len(self_word_to_find)):
                    if self.word_to_find==letter:
                        self.correctly_guessed_letters= letter
                








