import pygame
from pygame.constants import K_ESCAPE
from pygame.sprite import Sprite
from connect4 import Connect4

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN
)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

class Connect4Game:
    BUFFER = 30
    PlayerIdToColor = [BLACK, YELLOW, RED]

    def __init__(self, args):
        self._game = Connect4(args)
        self._gameOver = False
        self.tokenSize = 75
        self._screenWidth = self._game.getBoard().numCols() * self.tokenSize + Connect4Game.BUFFER
        self._screenHeight = (self._game.getBoard().numRows() + 1) * self.tokenSize + Connect4Game.BUFFER
        self.screen = self.initializeGraphics()

    def playConnect4(self):
        self._game.resetGame()
        
        while not self.isGameOver():
            mouseClick = self.eventListener()
            
            if mouseClick:
                self.drawBoard()

            pygame.display.flip()

    def initializeGraphics(self):
        pygame.init()
        screen = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        background = (0, 0, 0)
        screen.fill(background)
        return screen

    def eventListener(self):
        mouseClick = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.gameOver()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
        return mouseClick

    def getBoard(self):
        return self._game.getBoard()

    def drawBoard(self):
        tokenRadius = self.tokenSize//2 - 5
        p = (0, self._screenWidth - self.tokenSize)
        pygame.draw.rect(self.screen, BLUE, ((0, self.tokenSize), (self._screenWidth, self._screenHeight - self.tokenSize)))
        board = self.getBoard()
        for row in range(board.numRows()):
            for col in range(board.numCols()):
                pos = (col * self.tokenSize + tokenRadius +10, row * self.tokenSize + self.tokenSize + tokenRadius+10)
                playerId = board.getToken(row, col)
                color = Connect4Game.PlayerIdToColor[playerId]
                pygame.draw.circle(self.screen, color, pos, tokenRadius)

    def isGameOver(self):
        return self._gameOver

    def gameOver(self):
        self._gameOver = True

