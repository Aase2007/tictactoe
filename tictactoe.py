import pygame
import time
global turn
#initialising pygame
pygame.init()

#defining size of game window
windowsSize = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Hello World Printer")

#Bakgrunnsfargen i RGB
color = (100, 0, 200)
color_dark = (100,100,100)
windowsSize.fill(color)
#definerer font og størrelse
myFont = pygame.font.SysFont("Segoe UI", 100)
header = myFont.render("TRE PÅ RAD", 1, (255, 255, 255))

#deifinerer globale variabler
winner = None
draw = False
turn = "x"
grid = []

#definerer bilder:
x_image = pygame.image.load("ximage.png")
o_image = pygame.image.load("oimage.png")
#scaler bildene:
x_image = pygame.transform.scale(x_image, (100, 100))
o_image = pygame.transform.scale(o_image, (100, 100))

#definerer knapp variabler:

margin = 130
firstButtonx = 190
firstButtony = 150

mainrec = pygame.draw.rect(windowsSize, color_dark, [firstButtonx, firstButtony, 120+margin*2, 120+margin*2])
for i in range(3):
    lineList = []
    for n in range(3):
        pygame.draw.rect(windowsSize, color, [firstButtonx+margin*n, firstButtony+margin*i,120,120])
        lineList.append(True)
    grid.append(lineList)
print(grid)

def check_win():
    global winner
    diagonal1 = []
    diagonal2 = []
    for i in range(len(grid)):
        diagonal1.append(grid[i][i])
        diagonal2.append(grid[i][-(i+1)])
        vertical = [grid[0][i],grid[1][i],grid[2][i]]
        if grid[i] == ["x","x","x"] or vertical == ["x","x","x"]:
            winner = "x"
        elif grid[i] == ["o","o","o"] or vertical == ["o","o","o"]:
            winner = "o"
    if diagonal1 == ["x","x","x"] or diagonal2 == ["x","x","x"]:
        winner = "x"
    elif diagonal1 == ["o","o","o"] or diagonal2 == ["o","o","o"]:
        winner = "o"

    if winner != None:
        print(winner, "vant!")
        windowsSize.fill(color)
        winnertxt = myFont.render(f'{winner} vant!', 1, (255, 255, 255))
        windowsSize.blit(winnertxt, (firstButtonx,firstButtony))


def mouse_clicked(pos):
    global turn
    if mainrec.collidepoint(pos[0],pos[1]):
        for i in range(3):
            for n in range(3):
                rect = pygame.Rect(firstButtonx+margin*n, firstButtony+margin*i, 120, 120)
                if rect.collidepoint(pos[0],pos[1]):
                    if grid[i][n]:
                        grid[i][n] = turn
                        if turn == "x":
                            windowsSize.blit(x_image, (firstButtonx+margin*n+10, firstButtony+margin*i+10))
                            turn = "o"
                        else:
                            windowsSize.blit(o_image, (firstButtonx+margin*n+10, firstButtony+margin*i+10))
                            turn = "x"
                    print(grid)
                    check_win()




while 1:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked(pygame.mouse.get_pos())
        elif event.type==pygame.QUIT: sys.exit() #lukker programmet
        else: pass
    windowsSize.blit(header, (10, 10))
    pygame.display.update()