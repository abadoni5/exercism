"""
Hangman game implementation using a class.

The Hangman class encapsulates the logic for playing the Hangman game. It allows initializing the game with a word, guessing letters, and checking the game's status.

Approach:
- The class initializes with a word chosen for the game, setting attributes like remaining_guesses, status, and creating a masked version of the word.
- During the game, players can guess letters. If the guessed letter is correct, it updates the masked word; otherwise, it decreases the remaining guesses.
- The game ends either when the word is completely guessed (STATUS_WIN) or when the remaining guesses run out (STATUS_LOSE).

"""
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
    """
    Class for the Hangman game.
    """
    def __init__(self, word: str):
        self.word = word
        self._set_word = set(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self._masked_word = [0] * len(self.word)
        self._guessed: set[str] = set()
 
    def guess(self, char: str) -> None:
        """
        Try to guess a letter.
        """
        if self.status == STATUS_ONGOING:
            if char not in self._set_word or char in self._guessed:
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
            else:
                self._guessed.add(char)
                self._masked_word = [
                    value if self.word[i] != char else 1
                    for i, value in enumerate(self._masked_word)
                ]
                if sum(self._masked_word) == len(self.word):
                    self.status = STATUS_WIN
        else:
            raise ValueError("The game has already ended.")
 
    def get_masked_word(self) -> str:
        """
        Return the masked word.
        """
        return "".join(
            letter if self._masked_word[i] else "_"
            for i, letter in enumerate(self.word)
        )
 
    def get_status(self) -> str:
        """
        Get the status of the game.
        """
        return self.status