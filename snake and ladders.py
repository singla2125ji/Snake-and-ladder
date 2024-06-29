import pygame
from pygame.locals import *
import random as rd

pygame.init()

color = (255, 255, 255)
pos = (75, 0)

screen = pygame.display.set_mode((825, 750))
pygame.display.set_caption("Snake and Ladders")
image = pygame.image.load("Board.jpg")
image1 = pygame.transform.scale(image, (750, 750))
dice_images = [
    pygame.transform.scale(pygame.image.load(f"dice_{i}.jpg"), (65, 65)) for i in range(1, 7)
]
smallfont = pygame.font.SysFont('Corbel', 25)
bigfont = pygame.font.SysFont('Corbel',150)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
text = smallfont.render('roll dice', True, color)
exit_game = False
roll = 1

snakes_ladders={99:[[125,175,-1],[95,175,-1],[125,200,-1],[95,200,-1]],95:[[620,400,1],[650,400,1],[620,425,1],[650,425,1]],
                84:[[200,325,-1],[170,325,-1],[200,350,-1],[170,350,-1]],90:[[800,325,-1],[770,325,-1],[800,350,-1],[770,350,-1]],
                75:[[425,325,-1],[395,325,-1],[425,350,-1],[395,350,-1]],55:[[575,475,-1],[545,475,-1],[575,500,-1],[545,500,-1]],
                43:[[545,700,1],[575,700,1],[545,725,1],[575,725,1]],32:[[800,625,-1],[770,625,-1],[800,650,-1],[770,650,-1]],
                23:[[170,700,1],[200,700,1],[170,725,1],[200,725,1]],4:[[275,625,-1],[245,625,-1],[275,650,-1],[245,650,-1]],
                9:[[620,550,1],[650,550,1],[620,575,1],[650,575,1]],25:[[545,400,1],[575,400,1],[545,425,1],[575,425,1]],
                30:[[770,400,1],[800,400,1],[770,425,1],[800,425,1]],39:[[95,400,1],[125,400,1],[95,425,1],[125,425,1]],
                45:[[350,325,-1],[320,325,-1],[350,350,-1],[320,350,-1]],52:[[620,250,1],[650,250,1],[620,275,1],[650,275,1]],
                65:[[395,100,1],[425,100,1],[395,125,1],[425,125,1]],79:[[275,25,-1],[245,25,-1],[275,50,-1],[245,50,-1]],
                89:[[800,25,-1],[770,25,-1],[800,50,-1],[770,50,-1]]
               }

head_base={99:[(150,226),(0,76)],95:[(450,526),(0,76)],90:[(750,826),(75,151)],84:[(300,376),(75,151)],75:[(450,526),(150,226)],
            55:[(450,525),(300,376)],43:[(225,301),(375,451)],32:[(675,751),(450,526)],23:[(225,301),(525,601)],
            4:[(300,376),(675,751)],9:[(675,751),(675,751)],25:[(375,451),(525,601)],30:[(750,826),(525,601)],
            39:[(150,226),(450,526)],45:[(375,451),(375,451)],52:[(675,751),(300,376)],65:[(375,451),(225,301)],
            79:[(150,226),(150,226)],89:[(675,751),(75,151)]
           }

red_x, red_y = 20, 700
yellow_x, yellow_y = 50, 700
green_x, green_y = 20, 725
blue_x, blue_y = 50, 725
current_player = 1

def move_player(x, y, roll, direction):
    new_x = x + roll * 75 * direction
    if new_x > 825:
        overflow = new_x - 825
        new_x = 825 - overflow
        y -= 75
        direction *= -1
    elif new_x < 75:
        overflow = 75 - new_x
        new_x = 75 + overflow
        y -= 75
        direction *= -1
    if new_x < 75 or y < 0:
        return None
    for k1,v1 in head_base.items():
        if new_x in range(v1[0][0],v1[0][1]) and y in range(v1[1][0],v1[1][1]):
            for k,v in snakes_ladders.items():
                if k==k1:
                    if current_player==1:
                        new_x,y,direction=v[0]
                        return new_x, y, direction
                    elif current_player==2:
                        new_x,y,direction=v[1]
                        return new_x, y, direction
                    elif current_player==3:
                        new_x,y,direction=v[2]
                        return new_x, y, direction
                    elif current_player==4:
                        new_x,y,direction=v[3]
                        return new_x, y, direction
            
    return new_x, y, direction

def is_winner(x, y):
    if x in range(75, 151) and y in range(0, 76):
        exit_game=True
        return True
    return False

red_direction= 1
yellow_direction = 1
green_direction = 1
blue_direction = 1

while not exit_game:
    screen.fill(color)
    screen.blit(image1, pos)
    screen.blit(dice_images[roll - 1], (5, 75))
    red = pygame.draw.circle(screen, (255, 0, 0), (red_x, red_y), 10, 0)
    yellow = pygame.draw.circle(screen, (255, 255, 0), (yellow_x, yellow_y), 10, 0)
    green = pygame.draw.circle(screen, (0, 128, 0), (green_x, green_y), 10, 0)
    blue = pygame.draw.circle(screen, (0, 0, 255), (blue_x, blue_y), 10, 0)
    if current_player==1:
        screen.blit(smallfont.render('Red',True,(255,0,0)),(10,150))
    elif current_player==2:
        screen.blit(smallfont.render('Yellow',True,(255,255,0)),(10,150))
    elif current_player==3:
        screen.blit(smallfont.render('Green',True,(0,128,0)),(10,150))
    elif current_player==4:
        screen.blit(smallfont.render('Blue',True,(0,0,255)),(10,150))
    mouse = pygame.mouse.get_pos()
    if 5 <= mouse[0] <= 70 and 30 <= mouse[1] <= 70:
        pygame.draw.rect(screen, color_light, [5, 30, 65, 40])
    else:
        pygame.draw.rect(screen, color_dark, [5, 30, 65, 40])
    
    screen.blit(text, (5, 40))
    pygame.display.update()
    
    if is_winner(red_x, red_y):
        screen.blit(bigfont.render('Red Wins',True,(255,0,0)),(300,300))
        pygame.display.update()
        exit_game = True
        
    elif is_winner(yellow_x, yellow_y):
        screen.blit(bigfont.render('Yellow Wins',True,(255,255,0)),(300,300))
        pygame.display.update()
        exit_game = True
    
    elif is_winner(green_x, green_y):
        screen.blit(bigfont.render('Green Wins',True,(0,128,0)),(300,300))
        pygame.display.update()
        exit_game = True
                    
    elif is_winner(blue_x, blue_y):
        screen.blit(bigfont.render('Blue Wins',True,(0,0,255)),(300,300))
        pygame.display.update()
        exit_game = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 5 <= mouse[0] <= 70 and 30 <= mouse[1] <= 70:
                roll = rd.randint(1, 6)
                screen.blit(dice_images[roll - 1], (5, 75))

                if current_player == 1:
                    result = move_player(red_x, red_y, roll, red_direction)
                    if result:
                        red_x, red_y, red_direction = result
                    current_player = 2
                elif current_player == 2:
                    result = move_player(yellow_x, yellow_y, roll, yellow_direction)
                    if result:
                        yellow_x, yellow_y, yellow_direction = result
                    current_player = 3
                    
                elif current_player == 3:
                    result = move_player(green_x, green_y, roll, green_direction)
                    if result:
                        green_x, green_y, green_direction = result
                    current_player = 4
                elif current_player == 4:
                    result = move_player(blue_x, blue_y, roll, blue_direction)
                    if result:
                        blue_x, blue_y, blue_direction = result
                    current_player = 1