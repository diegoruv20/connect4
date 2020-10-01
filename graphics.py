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
    PlayerIdToColor = [BLACK, YELLOW, RED]

    def __init__(self, args):
        self._game = Connect4(args)
        self._gameOver = False
        self.tokenSize = 75
        self._screenWidth = self._game.getBoard().numCols() * self.tokenSize
        self._screenHeight = (self._game.getBoard().numRows() + 1) * self.tokenSize
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
        background = (255, 255, 255)
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
        board = self.getBoard()
        for col in range(board.numCols()):
            for row in range(board.numRows()):
                coordinates = (row * self.tokenSize + self.tokenSize - 20, col * self.tokenSize + self.tokenSize)
                tokenSize = (self.tokenSize, self.tokenSize)
                pygame.draw.rect(self.screen, BLUE, (coordinates, tokenSize))
                playerId = board.getToken(row, col)
                color = Connect4Game.PlayerIdToColor[playerId]
                pygame.draw.circle(self.screen, color, coordinates, tokenRadius)

    def isGameOver(self):
        return self._gameOver

    def gameOver(self):
        self._gameOver = True

