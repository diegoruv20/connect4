from board import Connect4Board, MAX_COL_COUNT
from random import randint

class Connect4():
    def __init__(self):
        self._currPlayerId = 1
        self._board = Connect4Board()
    
    def __str__(self):
        return str(self._board)

    def getBoard(self):
        return self._board

    def currPlayerId(self):
        return self._currPlayerId

    def placeToken(self, col):
        self._board.placeToken(col, self.currPlayerId())
        self._currPlayerId += 1
        if self._currPlayerId == 3:
            self._currPlayerId = 1
    
    def isValidMove(self, col):
        return self._board.isValidMove(col)

    def playNRandomActions(self, n=10):
        board = self.getBoard()
        for i in range(n):
            col = self.getRandomAction()
            if not  board.isValidMove(col):
                print(f'Invalid Move col {col}')
                break

            playerId = self.currPlayerId()
            board.placeToken(col)
            print(f'Player {playerId} went on column {col}')
            print(board)
    
    def isGameOver(self):
        return self.getBoard().hasConnectFour()

    def getRandomAction(self):
        return randint(0, MAX_COL_COUNT - 1)

def main():
    game = Connect4()
    while True:
        col = -1
        try:
            col = int(input(f"Enter col of move(1-{MAX_COL_COUNT}): "))
            col -= 1
        except ValueError:
            print("Not a valid number...Try Again...")
            continue

        if not game.getBoard().isValidMove(col):
            print("Invalid Move...")
            continue

        currPlayer = game.currPlayerId()
        # print(f'Player {board.getCurrPlayerId()} played on column {col}')
        game.placeToken(col)
        print(game, end="\n\n")

        if game.isGameOver():
            print(f"GAME OVER! Player {currPlayer} Wins!")
            break

        print('hello')

if __name__ == "__main__" : main()
