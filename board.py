import numpy as np

MAX_COL_COUNT = 7
MAX_ROW_COUNT = 6

class Connect4Board:
    def __init__(self):
        self._board = np.zeros((MAX_ROW_COUNT, MAX_COL_COUNT))
        # Keeps track of open row index
        self._validRows = [MAX_ROW_COUNT - 1 for i in range(MAX_COL_COUNT)]

    def __repr__(self):
        return 'Board()'

    def __str__(self):
        return str(self._board)

    def isValidMove(self, col):
        return col >= 0 and col < MAX_COL_COUNT - 1 and self._validRows[col] > - 1

    def placeToken(self, col, playerId):
        # Place in column
        row = self._validRows[col]
        self._board[row, col] = playerId

        # Update valid rows and currPlayerId
        self._validRows[col] -= 1

    def _inBounds(self, row, col):
        return row < MAX_ROW_COUNT and row > self._validRows[col] and col < MAX_COL_COUNT and col >= 0

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
            if row == MAX_ROW_COUNT-1:
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
