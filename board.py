import numpy as np

class Connect4Board:
    def __init__(self, numRows, numCols):
        self._dimensions = numRows, numCols
        self._board = np.zeros((numRows, numCols))
        # Keeps track of open row index
        self._validRows = [numRows - 1 for i in range(numCols)]

    def __repr__(self):
        return 'Board()'

    def __str__(self):
        return str(self._board)

    def getToken(self, row, col):
        return int(self._board[row, col])

    def numCols(self):
        return self._dimensions[1]
    
    def numRows(self):
        return self._dimensions[0]

    def isValidMove(self, col):
        return col >= 0 and col < self.numCols() and self._validRows[col] > - 1

    def placeToken(self, col, playerId):
        # Place in column
        row = self._validRows[col]
        self._board[row, col] = playerId

        # Update valid rows and currPlayerId
        self._validRows[col] -= 1

    def _inBounds(self, row, col):
        return col < self.numCols() and col >= 0 and row < self.numRows() and row > self._validRows[col]

    def _countConsecutivePieces(self, rowStart, colStart, rowDelta=0, colDelta=0):
        playerId = self._board[rowStart, colStart]

        row = rowStart + rowDelta
        col = colStart + colDelta
        count = 0
        while self._inBounds(row, col) and self._board[row, col] == playerId:
            count += 1
            row += rowDelta
            col += colDelta
        return count

    def hasConnectFour(self):
        # iterate through last played piece in every col
        for col, row in enumerate(self._validRows):
            if row == self.numRows()-1:
                continue

            row = row + 1
            def checkHorizontalWin():
                count = self._countConsecutivePieces(
                    row, col, colDelta=-1) + self._countConsecutivePieces(row, col, colDelta=1)
                return count >= 3

            def checkVerticalWin():
                count = self._countConsecutivePieces(row, col, rowDelta=1)
                return count >= 3

            def checkDiagonalWinPosSlope():
                count = self._countConsecutivePieces(
                    row, col, rowDelta=1, colDelta=-1) + self._countConsecutivePieces(row, col, rowDelta=-1, colDelta=1)
                return count >= 3

            def checkDiagonalWinNegSlope():
                count = self._countConsecutivePieces(
                    row, col, rowDelta=-1, colDelta=-1) + self._countConsecutivePieces(row, col, rowDelta=1, colDelta=1)
                return count >= 3

            if checkVerticalWin() or checkHorizontalWin() or checkDiagonalWinPosSlope() or checkDiagonalWinNegSlope():
                return True
        return False
