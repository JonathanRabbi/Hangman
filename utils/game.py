class Hangman:
    def __init__(self):
        #the searched word
        self.word_to_find = ["becode"]
        
        #the amount of lives the player has
        self.lives = 5

        #list the letters that the player had correctly guessed
        self.correctly_guessed_letters = ["_" for letter in self.word_to_find]
        
        # this will list the letters that the player had wrong
        self.wrongly_guessed_letters = [] 

        # this will list the letters that the player has attempted
        self.guesses=[] 

        # this will add the amount of turns the player took
        self.turn_count = 0 

        # this will add the amount of times the player was wrong
        self.error_count = 0 
    
    def play(self):
        """
        This method requests the player to enter a letter. 
        The game does not allow the player to type anything other that a letter nor are they allowed
        to type in more than 1 letter.
        If the player had guessed the letter well, then the letter will be added to the correctly_guessed_letters list
        If they player gets the letetr wrong, the letter will be added to the wrongly_guessed_letters list.
        The wrong letter will also be added to the error_count

        """

        while True:
            letter = input("Guess a letter:")
            if not letter.isalpha() or len(letter)!=1:
                print("Please enter 1 letter.")
                continue 
            self.guesses.append(letter)
            self.turn_count+=1 

            if letter in self.word_to_find:
                for i in range(len(self.word_to_find)):
                    if self.word_to_find ==letter:
                        self.correctly_guessed_letters = letter

            else:
                print("nope, guess again")
                self.wrongly_guessed_letters.append(letter) #adds the wrongly guessed letter to the list
                self.error_count+=1 # starts counting how many errors you got
                self.lives -=1

            #not done yet with the play method
        
    def start_game(self):
        """
        The start game method will call the play method until the game has finished.
        This will end by either the player guessing all the correct letters or running out of lives.
        If the letters are correctly guessed within the 5 attempts/lives, the method will call the well_played-method.
        Moreover, if all the lives have been used, this method will call the game_over-metod

        """
        while True:
            # this calls the play-method and its code, allowing the player to enter and validate the input and furtehr perform necessary actions from th start_game-method
            self.play() 

            # if the player no longer has lives, then game_over-method is called
            if self.lives ==0:
                self.game_over()
                break 

            # if the player guessed all the letters correctly then well_played method is called
            if self.word_to_find== self.correctly_guessed_letters:
                self.well_played()
                break 

    def game_over(self):
        print("game over")
    
    def well_played(self):
        print(f"you found the word: {self.word_to_find} in {self.turn_count} and {self.error_count} errors!")







