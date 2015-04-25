'''
Created on Apr 19, 2015

@author: Jay
'''
import pygame
import os
import random

pygame.init()

#initialize variables
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,155,0)

menuSelect = pygame.mixer.Sound("FF7ok.wav")
menuCancel = pygame.mixer.Sound("FF7cancel.wav")
menuWrong = pygame.mixer.Sound("FF7no.wav")
menuMove = pygame.mixer.Sound("FF7move.wav")


displayWidth = 800
displayHeight = 600
font = pygame.font.SysFont(None, 25)
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
images = ["VII-1.jpg","VII-2.jpg","IX-1.jpg","IX-2.jpg","IX-3.jpg","IX-4.jpg"]



class controlDisplay(object):
    def __init__(self,):
        pass

    def gameDisplay(self,displayWidth,displayHeight):
        pygame.display.set_mode((displayWidth,displayHeight))
        pygame.display.set_caption("Welcome!")

    def displayText(self,msg,XPos,YPos,color):
        on_screen = font.render(msg, True, color)
        gameDisplay.blit(on_screen, [XPos,YPos])

    def resetDisplay(self,color):
        gameDisplay.fill(color)
        pygame.display.update()
        
    def loadImage(self,images,imagesIndex):
        imagesIndex = 0
        imageToLoad = images[imagesIndex]
        displayImage = pygame.image.load(os.path.join("C:/Users/Jay/Documents/LiClipse Workspace/LD32-Take-2/beginning", imageToLoad))
        gameDisplay.blit(displayImage,(0,0))
        pygame.display.update()
        
class Game(object):
    def __init__(self):
        self.cd = controlDisplay()
        pass

    def gameLoop(self):
        gameRunning = True
        mainMenu = True
        gameOver = False
        quitting = False
        inGame = False
        inViewer = False
        imagesIndex = 0

        while gameRunning:
            while mainMenu:
                gameDisplay.fill(white)
                self.cd.displayText("Please select an option",50,50,black)
                self.cd.displayText("\"ENTER\": Play",75,75,black)
                self.cd.displayText("\"S\" Key: Viewer",75,100,black)
                self.cd.displayText("\"ESCAPE\": Quit",75,125,black)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        mainMenu = False
                        quitting = True
                        menuCancel.play()
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_ESCAPE]:
                            mainMenu = False
                            quitting = True
                            menuCancel.play()
                        elif key[pygame.K_RETURN]:
                            mainMenu = False
                            inGame = True
                            menuSelect.play()
                            self.cd.resetDisplay(white)
                        elif key[pygame.K_s]:
                            mainMenu = False
                            inViewer = True
                            menuSelect.play()
                        else:
                            menuWrong.play()

            while gameOver:
                gameDisplay.fill(black)
                self.cd.displayText("Game Over, press \"ENTER\" to return to the main menu or \"ESCAPE\" to quit",50,50,red)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        quitting = True
                        menuCancel.play()
                    elif event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_RETURN]:
                            gameOver = False
                            menuSelect.play()
                            mainMenu = True
                        elif key[pygame.K_ESCAPE]:
                            gameOver = False
                            quitting = True
                        else:
                            menuWrong.play()

            while quitting:
                gameDisplay.fill(black)
                self.cd.displayText("Are you sure you want to quit?",50,50,red)
                self.cd.displayText( "Press \"ENTER\" to quit or \"ESCAPE\" to go back to menu",50,75,red)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quitting = False
                        gameRunning = False
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_RETURN]:
                            quitting = False
                            gameRunning = False
                            menuSelect.play()
                        elif key[pygame.K_ESCAPE]:
                            mainMenu = True
                            quitting = False
                            menuCancel.play()
                        else:
                            menuWrong.play()

            while inGame:
                randColor = (0,0,0)
                self.cd.displayText("Press \"ESCAPE\" to return to menu",50,50,black)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        inGame = False
                        quitting = True
                        menuCancel.play()
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_ESCAPE]:
                            inGame = False
                            mainMenu = True
                            menuCancel.play()
                        elif key[pygame.K_RETURN]:
                            menuSelect.play()
                            randX = randY = random.randrange(0,500)
                            randColor = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
                            gameDisplay.fill(randColor)
                            self.cd.displayText("You played the game!",randX,randY,black)
                        else:
                            menuWrong.play()
                pygame.display.update()


            while inViewer:
                self.cd.displayText("Press \"ESCAPE\" to return to menu",50,50,black)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        inViewer = False
                        quitting = True
                        menuCancel.play()
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_ESCAPE]:
                            inViewer = False
                            mainMenu = True
                            menuCancel.play()
                        elif key[pygame.K_LEFT]:
                            menuMove.play()
                            if imagesIndex == 0:
                                imagesIndex = len(images) - 1
                            else:
                                imagesIndex -= 1
                        elif key[pygame.K_RIGHT]:
                            menuMove.play()
                            if imagesIndex == len(images) - 1:
                                imagesIndex = 0
                            else:
                                imagesIndex += 1
                    
                self.cd.loadImage(images,imagesIndex)

                pygame.display.update()

        pygame.quit()
        quit()

gamething = Game()
gamething.gameLoop()
