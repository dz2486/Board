class Board:
    def __init__(self):
        # Define a 3x3 empty grid
        self.squares = [
            [None for _ in range(3)],
            [None for _ in range(3)],
            [None for _ in range(3)],
        ]
        # Whose turn is it? O will begin the game
        self._turn = "O"
        
    def __repr__(self):
        return "\n" + "\n".join(
            "".join("_" if piece is None else piece for piece in row)
            for row in self.squares
        ) + "\n"
    
    def mark_square(self, coordinates):
        """
        Mark the square at the given coordinates with the current player's character.
        
        Then move to the other player's turn.
        """
        x, y = coordinates
        self.squares[x][y] = self._turn
        if self._turn == "O":
            self._turn = "X"
        else:
            self._turn = "O"