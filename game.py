
import pygame
pygame.init()

# importing necessary frameworks
import pygame
import time
import random
from pygame.locals import *
from pygame import mixer

pygame.init()


# specifying color rgbs
black = (0, 0, 0)
red = (220,20,60)
green = (34,139,34)


# generating random color for the snake and food
r = random.randint(0,255)
g = random.randint(0,250)
b = random.randint(0,255)
rgb = [r,g,b]
rgb1 = [g,r,b]

# setting display sizes
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()


snake_block = 20
snake_speed = 10 

font_style = pygame.font.SysFont("", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# adding background music
mixer.init()
mixer.music.load('backgroundmusic.mp3')
mixer.music.play(loops=-1)

# showing the score on the display
def Your_score(score):
    value = score_font.render(" Score: " + str(score), True, green)
    dis.blit(value, [0, 0])

# adding random colors to the snake blocks
def our_snake(snake_block, snake_list):
    for x in snake_list:
        r = random.randint(0,255)
        g = random.randint(0,250)
        b = random.randint(0,255)
        pygame.draw.rect(dis, [r,g,b], [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# game syntax
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0


# when game over
    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    
                

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, rgb1, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()








