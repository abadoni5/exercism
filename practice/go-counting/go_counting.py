"""
This class, `Board`, is designed to analyze territories in a Go game. It defines methods to determine the owner and territories given a coordinate on the board, as well as to find the owners and territories of the entire board.

Constants:
- `WHITE`: Represents the white player on the Go board.
- `BLACK`: Represents the black player on the Go board.
- `NONE`: Represents an empty intersection on the Go board.
- `UNKNOWN`: Represents an unassigned owner for a territory.

Class `Board`:
Attributes:
- `board`: A two-dimensional Go board.
- `rows`: The number of rows in the board.
- `cols`: The number of columns in the board.

Methods:
- `__init__(self, board)`: Initializes the Board instance with the given board configuration.
- `onboard(self, x, y)`: Checks if a given coordinate is within the boundaries of the board.
- `neighbors(self, x, y)`: Finds the neighboring coordinates of a given coordinate.
- `territory(self, x, y)`: Finds the owner and territories given a coordinate on the board.
- `territories(self)`: Finds the owners and territories of the entire board.

Approach:
- The `territory` method uses a flood fill algorithm to identify enclosed territories and determine their owner.
- The `territories` method iterates over empty intersections on the board, identifies their territories, and assigns them to the respective owners.
"""

WHITE = "W"
BLACK = "B"
NONE = " "
UNKNOWN = "?"

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = 0 if self.rows == 0 else len(board[0])

    def onboard(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def neighbors(self, x, y):
        nbr = []
        for dx in (-1, 1):
            if self.onboard(x + dx, y):
                nbr.append((x + dx, y))
        for dy in (-1, 1):
            if self.onboard(x, y + dy):
                nbr.append((x, y + dy))
        return nbr
        
    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self.onboard(x, y):
            raise ValueError("Invalid coordinate")
        if self.board[y][x] != NONE:
            return NONE, set()
        owner = UNKNOWN
        visited = set()
        enclosed = set()
        stack = [(x, y)]
        while len(stack) != 0:
            c, r = stack.pop()
            visited.add((c, r))
            stone = self.board[r][c]
            if stone == NONE:
                enclosed.add((c, r))
                for n in self.neighbors(c, r):
                    if n not in visited:
                        stack.append(n)
            elif stone != owner:
                owner = stone if owner == UNKNOWN else NONE
        if owner == UNKNOWN:
            owner = NONE
        return owner, enclosed
            
    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        t = {WHITE: set(), BLACK: set(), NONE: set()}
        vacant = set((c, r) for c in range(self.cols) for r in range(self.rows) if self.board[r][c] == NONE)
        while len(vacant) != 0:
            v = vacant.pop()
            who, where = self.territory(v[0], v[1])
            vacant -= where
            t[who] |= where
        return t
