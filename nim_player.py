class NimPlayer:
    def __init__(self) -> None:
        pass

    # takes in a board state and returns a move
    def play(self, board):
        for i in range(len(board)):
            if board[i] > 0:
                board[i] -= 1
                return board
        return board