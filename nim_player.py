# Author: Ben Berton
# Desc: This file contains the NimPlayer class which is used to play the game of nim.
# Date: 10/8/2023
class NimPlayer:
    def __init__(self) -> None:
        pass

    # takes in a board state and returns a move
    def play(self, board):
        if (self.isEndgameState(board)):
            for i in range(len(board)):
                if board[i] > 1:
                    potentialState = self.deepCopy(board)
                    potentialState[i] = 0
                    if (self.oddNumOfStacks(potentialState)):
                        return potentialState
                    potentialState[i] = 1
                    return potentialState
        else:
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
        return board
    
    def isEndgameState(self, board):
        largeColCount = 0
        for stack in board:
            if stack > 1:
                largeColCount += 1
                if (largeColCount > 1):
                    return False
        if (largeColCount == 0):
            return False
        return True
            
    def oddNumOfStacks(self, board):
        number_of_ones = 0
        for stack in board:
            if stack == 1:
                number_of_ones += 1

        return number_of_ones % 2 == 1
    

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