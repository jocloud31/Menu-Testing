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

#create display
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Welcome!")

#initialize functions
def resetDisplay():
    gameDisplay.fill(white)
    pygame.display.update()

def displayText(msg,textX,textY,color):
    on_screen = font.render(msg, True, color)
    gameDisplay.blit(on_screen, [textX,textY])

def gameLoop():
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
            displayText("Please select an option",50,50,black)
            displayText("\"ENTER\": Play",75,75,black)
            displayText("\"S\" Key: Viewer",75,100,black)
            displayText("\"ESCAPE\": Quit",75,125,black)
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
                        gameDisplay.fill(white)
                        pygame.display.update()
                    elif key[pygame.K_s]:
                        mainMenu = False
                        inViewer = True
                        menuSelect.play()
                    else:
                        menuWrong.play()
        
        while gameOver:
            gameDisplay.fill(black)
            displayText("Game Over, press \"ENTER\" to return to the main menu or \"ESCAPE\" to quit",50,50,red)
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
            displayText("Are you sure you want to quit?",50,50,red)
            displayText( "Press \"ENTER\" to quit or \"ESCAPE\" to go back to menu",50,75,red)
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
            displayText("Press \"ESCAPE\" to return to menu",50,50,black)
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
                        randX = random.randrange(0,500)
                        randY = random.randrange(0,500)
                        randColor = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
                        gameDisplay.fill(randColor)
                        displayText("You played the game!",randX,randY,black)
                    else:
                        menuWrong.play()
            pygame.display.update()    
                    
                    
        while inViewer:
            displayText("Press \"ESCAPE\" to return to menu",50,50,black)
            images = ["VII-1.jpg","VII-2.jpg","IX-1.jpg","IX-2.jpg","IX-3.jpg","IX-4.jpg"]
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
            imageToLoad = images[imagesIndex]
            displayImage = pygame.image.load(os.path.join("C:/Users/Jay/Documents/LiClipse Workspace/LD32-Take-2/beginning", imageToLoad))
            gameDisplay.blit(displayImage,(0,0))
            pygame.display.update()
                        
        pygame.display.update()
        
    pygame.quit()
    quit()
    
gameLoop()
