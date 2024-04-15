"""
Approach:
For scoring a bowling game, the general approach is to implement two main classes: Frame and BowlingGame.

1. Frame Class:
   - The Frame class manages the state of each frame in the bowling game.
   - It includes methods to check if the frame is full and if it's invalid based on the number of pins knocked down.
   - The roll method is responsible for adding pins to the frame while ensuring the frame remains valid and full.
   - The score method calculates the score for the frame considering the pins knocked down and the next throws.

2. BowlingGame Class:
   - The BowlingGame class handles the overall game state.
   - It includes methods for rolling the ball and calculating the final score of the game.
   - Error handling is implemented to ensure adherence to game rules and scoring protocols.
   - The is_full method checks if the game is complete by verifying if all frames are full.
   - The roll method rolls the ball and advances to the next frame if the current frame is full.
   - The score method calculates the final score of the game by iterating through frames and calculating each frame's score.

By implementing these classes and methods, we can effectively manage the state of the bowling game, handle player rolls, and accurately calculate the final score while adhering to game rules and scoring protocols.
"""

class Frame(object):
    def __init__(self, tenth=False):
        self.tenth = tenth
        self.pins = []

    def is_full(self):
        if self.tenth:
            return len(self.pins) == 2 and sum(self.pins) < 10 or \
                   len(self.pins) == 3 and (sum(self.pins[:2]) == 10 or self.pins[0] == 10)
        else:
            return len(self.pins) == 2 or len(self.pins) == 1 and self.pins[0] == 10

    def is_invalid(self):
        if self.tenth:
            return len(self.pins) == 2 and self.pins[0] < 10 and sum(self.pins) > 10 or \
                   len(self.pins) == 3 and self.pins[0] == 10 and self.pins[1] != 10 and sum(self.pins[1:]) > 10
        else:
            return sum(self.pins) > 10

    def roll(self, pins):
        if self.is_full():
            raise RuntimeError("Adding to full frame")
        else:
            self.pins.append(pins)
            if self.is_full() and self.is_invalid():
                raise ValueError ("This frame is not valid: {}".format(self.pins))
            return self.is_full()

    def score(self, next_throws):
        if next_throws:
            if self.pins[0] == 10:
                return sum(self.pins) + sum(next_throws[:2])
            elif sum(self.pins) == 10:
                return sum(self.pins) + next_throws[0]
            else:
                return sum(self.pins)
        else:
            return sum(self.pins)

    def __repr__(self):
        return "pins={}, full={}, is_invalid={}".format(self.pins, self.is_full(), self.is_invalid())

class BowlingGame(object):
    def __init__(self):
        self.frames = [Frame() for _ in range(9)] + [Frame(tenth=True)]
        self.current = 0

    def is_full(self):
        return all([frame.is_full() for frame in self.frames])

    def roll(self, pins):
        if not 0 <= pins <= 10:
            raise ValueError("Invalid pins value")
        elif self.is_full():
            raise IndexError("Trying to roll for full game")
        else:
            if self.frames[self.current].roll(pins):
                self.current += 1

    def score(self):
        if not self.is_full():
            raise IndexError("An incomplete game cannot be scored")

        score = 0
        for (i, frame) in enumerate(self.frames):
            next_throws = [throw for next_frame in self.frames[i+1:] for throw in next_frame.pins]
            score += frame.score(next_throws)

        return score