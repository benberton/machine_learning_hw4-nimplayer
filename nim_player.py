# Author: Ben Berton
# Desc: This file contains the NimPlayer class which is used to play the game of nim.
# Date: 10/1/2023
class NimPlayer:
    def __init__(self) -> None:
        pass

    # takes in a board state and returns a move
    def play(self, board):
        if (self.getNimSum(board) == 0):
            for i in range(len(board)):
                if board[i] > 0:
                    board[i] -= 1
                    return board
        else:
            for i in range(len(board)):
                boardSize = board[i]
                for j in range(boardSize):
                    board[i] = j
                    if (self.getNimSum(board) == 0):
                        return board
                board[i] = boardSize
        return board
        
    def getNimSum(self, board):
        nimSum = 0
        for i in range(len(board)):
            nimSum ^= board[i]
        return nimSum
    
    def deepCopy(self, board):
        newBoard = []
        for i in range(len(board)):
            newBoard.append(board[i])
        return newBoard