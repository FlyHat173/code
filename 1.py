import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ game
width, height = 720, 520
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước rắn và tốc độ
snake_block = 10
snake_speed = 10

# Font chữ
font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    x, y = width // 2, height // 2
    dx, dy = 0, 0

    snake_list = []
    length_of_snake = 1

    food_x = random.randrange(0, width - snake_block, 10)
    food_y = random.randrange(0, height - snake_block, 10)

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            window.fill(black)
            message = font.render("Ngu chết thì chịu!Press C-Continue or Q-Quit", True, red)
            window.blit(message, [width / 6, height / 3])
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    dx, dy = -snake_block, 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    dx, dy = snake_block, 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    dx, dy = 0, -snake_block
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    dx, dy = 0, snake_block
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += dx
        y += dy
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(snake_block, snake_list)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - snake_block, 10)
            food_y = random.randrange(0, height - snake_block, 10)
            length_of_snake += 2
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()