import pygame
import math
from pygame.constants import K_ESCAPE
from pygame.sprite import Sprite
from connect4 import Connect4

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    VIDEORESIZE
)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

class Connect4Game:
    BUFFER = 5
    PlayerIdToColor = [BLACK, YELLOW, RED]
    PlayerIdToName = ["Yellow", "Red"]

    def __init__(self, args):
        self._game = Connect4(args)
        self.tokenSize = 100
        self._running = True
        self._screenWidth = self._game.getBoard().numCols() * self.tokenSize + self.BUFFER
        self._screenHeight = (self._game.getBoard().numRows() + 1) * self.tokenSize + self.BUFFER
        self.screen = self.initializeGraphics()

    def playConnect4(self):
        self._game.resetGame()
        
        while self._running:
            currPlayerId = self._game.currPlayerId()
            self.eventListener()

            self.drawBoard()
            pygame.display.flip()

            if self._game.isGameOver():
                font = pygame.font.SysFont("monospace", self.tokenSize-20)
                playerName = self.PlayerIdToName[currPlayerId - 1]
                label = font.render(f"{playerName} wins!", 1, self.PlayerIdToColor[currPlayerId])
                textHorizontalBuffer = [self._screenWidth//2 - 290, self._screenWidth//2 - 210][currPlayerId-1]
                self.screen.blit(label, (textHorizontalBuffer, 10))
                self._running = False
                pygame.display.flip()
                pygame.time.wait(3000)

            self._clock.tick(30)
        

    def initializeGraphics(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        pygame.display.set_caption('Connect 4')
        screen = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        background = (0, 0, 0)
        screen.fill(background)
        return screen

    def eventListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self._running = False
            if event.type == MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                col = int(math.floor(mouseX/self.tokenSize))
                self.playMove(col)
            # if event.type == VIDEORESIZE:
            #     self.resizeWindow(event.size, event.w, event.h)

    def resizeWindow(self, size, width, height):
        pass

    def playMove(self, col):
        self._game.placeToken(col)

    def getBoard(self):
        return self._game.getBoard()

    def drawBoard(self):
        tokenRadius = int(self.tokenSize * 0.43)
        pygame.draw.rect(self.screen, BLUE, ((0, self.tokenSize-self.BUFFER), (self._screenWidth, self._screenHeight - self.tokenSize + self.BUFFER)))
        board = self.getBoard()
        for row in range(board.numRows()):
            y = row * self.tokenSize + int(self.tokenSize * 3/2)
            for col in range(board.numCols()):
                x = col * self.tokenSize + self.tokenSize//2
                pos = (x + self.BUFFER//2, y)
                playerId = board.getToken(row, col)
                color = Connect4Game.PlayerIdToColor[playerId]
                pygame.draw.circle(self.screen, color, pos, tokenRadius)
