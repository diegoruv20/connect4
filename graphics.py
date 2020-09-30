import pygame
from pygame.constants import K_ESCAPE
from pygame.sprite import Sprite
from connect4 import Connect4

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN
)


class Connect4Game:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    PlayerIdToColor = [(255, 255, 255), (255, 0, 0), (255, 255, 0)]

    def __init__(self, args):
        self._game = Connect4(args)
        self._gameOver = False
        self.screen = self.initializeGraphics()
        self.board = self._game.getBoard()

    def playConnect4(self):
        self._game.resetGame()
        
        while not self.isGameOver():
            self.eventListener()
            
            self.drawBoard()

            pygame.display.flip()

    def initializeGraphics(self):
        pygame.init()
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        background = (255, 255, 255)
        screen.fill(background)
        return screen

    def eventListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.gameOver()

    def drawBoard(self):

    def isGameOver(self):
        return self._gameOver

    def gameOver(self):
        self._gameOver = True

