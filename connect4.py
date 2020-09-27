from board import Connect4Board
from random import randint
import argparse

DEFAULT_NUM_COL = 7
DEFAULT_NUM_ROW = 6

class Connect4():
    def __init__(self, args):
        self._currPlayerId = 1
        self._board = Connect4Board(args.numRows, args.numCols)
    
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
        return randint(0, self.getBoard().numCols() - 1)

def playGame(args):
    game = Connect4(args)
    while True:
        col = input(f"Enter col of move(1-{args.numCols}): ")
        if not isInt(col):
            print("Not a valid int... Try Again...")
            continue
        col = int(col) - 1

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

def isInt(string):
    try:
        int(string)
        return True
    except:
        return False
    
def main():
    parser = argparse.ArgumentParser(description='Play a game of Connect 4')

    parser.add_argument('--numRows', '-r',
                        default=DEFAULT_NUM_ROW, type=int, help='Number of rows on the board')
    parser.add_argument('--numCols', '-c',
                        default=DEFAULT_NUM_COL, type=int, help='Number of columns on the board')

    args = parser.parse_args()
    playGame(args)
    

if __name__ == "__main__" : main()
