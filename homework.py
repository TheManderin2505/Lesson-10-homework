import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 400
TITLE = 'Fighter Jet Game'

player = Actor('fighter')
computer = Actor('alien')
playergun = Actor('button')
computergun = Actor('red lock')
score = 0

computer.pos = (450,200)
player.pos = (50,200)

animations = []

def update():
    global score
    if keyboard.w:
        player.y = player.y + 2
    if keyboard.s:
        player.y = player.y - 2
    if keyboard.space:
        playergun.pos = player.pos 
        playergun.draw
        while True:
            playergun.x = playergun.x + 5
            if playergun.colliderect(computer):
                score = score + 10
                
            






def draw():
    screen.blit("desert",(-100,0))
    player.draw()
    computer.draw()







pgzrun.go()