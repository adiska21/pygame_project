import pygame
from random import randrange
from sprite import Apple

RES = 600
SIZE = 30

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {"W": True,
        "A": True,
        "S": True,
        "D": True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 10
score = 0

yellow = (244, 164, 96)
black = (20, 15, 11)
green = (127, 255, 0)
pygame.init()

screen = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 25, bold=True)
font_game_over = pygame.font.SysFont("Arial", 25, bold=True)

while True:
    screen.fill(yellow)

    for i, j in snake:
        pygame.draw.rect(screen, black, (i + 5, j + 5, 5, 5))
        snake_sprite = Apple(i + SIZE // 2 - 2, j + SIZE // 2, "snake/snake.png")
        screen.blit(snake_sprite.image, snake_sprite.rect)

    pygame.draw.rect(screen, yellow, (*apple, SIZE, SIZE))
    apple_sprite = Apple(apple[0] + SIZE // 2, apple[1] + SIZE // 2, "snake/mini_apple.png")
    screen.blit(apple_sprite.image, apple_sprite.rect)

    render_score = font_score.render(f"SCORE: {score}", 1, "red")
    screen.blit(render_score, (5, 5))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        length += 1
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        score += 1

    if x < 0 or x >= RES or y < 0 or y >= RES or len(snake) != len(set(snake)):
        while True:
            render_gama_over = font_game_over.render("GAME OVER", 1, "red")
            screen.blit(render_gama_over, (RES // 2 - 80, RES // 2))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_w] and dirs["W"]:
        dx, dy = 0, -1
        dirs = {"W": True, "S": False, "A": True, "D": True}
    if key[pygame.K_a] and dirs["A"]:
        dx, dy = -1, 0
        dirs = {"W": True, "S": True, "A": True, "D": False}
    if key[pygame.K_s] and dirs["S"]:
        dx, dy = 0, 1
        dirs = {"W": False, "S": True, "A": True, "D": True}
    if key[pygame.K_d] and dirs["D"]:
        dx, dy = 1, 0
        dirs = {"W": True, "S": True, "A": False, "D": True}
