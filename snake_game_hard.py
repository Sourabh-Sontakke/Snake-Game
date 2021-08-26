import pygame
from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RETURN, K_RIGHT, K_UP, K_a, K_d, K_s, K_w, QUIT
import random

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0 ,0)

pygame.init()

screen_width = 800
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")



clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 40)



def display_score(text, colour, x, y):
    score_text = font.render(text, True, colour)
    gameWindow.blit(score_text, [x,y])

def plot_snake(gameWindow, colour, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 150
    snake_y = 200
    velocity_x = 0
    velocity_y = 0
    init_velocity = 10

    snake_list = []
    snake_length = 1

    with open("hiscore_hard.txt", "r") as f:
        h = int(f.read()) 

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    snake_size = 25
    fps = 30
    score = 0
    while not exit_game:
        if game_over:
            gameWindow.fill(white)

            with open("hiscore_hard.txt", "w") as f:
                f.write(str(h))

            
            
            
                
                    
            

            
            
            display_score(f"The total score you made is {score}", red, 70, 100)
            display_score("Game Over! Press Enter to continue", red, 70, 250)
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game = True

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        gameloop()
        else:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit_game = True
                
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT or event.key == K_d:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == K_LEFT or event.key == K_a:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == K_DOWN or event.key == K_s:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == K_UP or event.key == K_w:
                        velocity_y = -init_velocity
                        velocity_x = 0
            

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 1
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snake_length += 5
                if score > h:
                    h = score

            
            

            gameWindow.fill(white)
            display_score(f"Score: {score}", red, 5,5)
            display_score(f"Hiscore: {h}", red, 200,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()

        clock.tick(fps)
        

    pygame.quit()
    quit()

gameloop()