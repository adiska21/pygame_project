import pygame
import random
import sys


def bot(mas):
    for row in range(3):
        if mas[row].count("o") == 2:
            print(row)
            for i in range(3):
                if mas[row][i] == 0:
                    mas[row][i] = "o"
                return mas
        elif mas[row].count("x") == 2:
            print(row)
            for i in range(3):
                if mas[row][i] == 0:
                    mas[row][i] = "o"
                    return mas
    for col in range(3):
        oes = [mas[0][col], mas[1][col], mas[2][col]]
        if oes.count("o") == 2:
            for i in range(3):
                if oes[i] == 0:
                    mas[i][col] = "o"
                    return mas
        elif oes.count("x") == 2:
            for i in range(3):
                if oes[i] == 0:
                    mas[i][col] = "o"
                    return mas

    diagonal = [mas[0][0], mas[1][1], mas[2][2]]
    diagonal2 = [mas[0][2], mas[1][1], mas[2][0]]

    if diagonal.count("o") == 2 or diagonal.count("x") == 2:
        if mas[0][0] == 0:
            mas[0][0] = "o"
        elif mas[1][1] == 0:
            mas[1][1] = "o"
        elif mas[2][2] == 0:
            mas[2][2] = "o"
        return mas
    elif diagonal2.count("o") == 2 or diagonal2.count("x") == 2:
        if mas[2][0] == 0:
            mas[2][0] = "o"
        elif mas[1][1] == 0:
            mas[1][1] = "o"
        if mas[0][2] == 0:
            mas[0][2] = "o"
        return mas

    while True:
        x = random.randrange(0, 3)
        y = random.randrange(0, 3)
        if mas[x][y] == 0:
            mas[x][y] = "o"
            return mas


def check_win(mas, sign):
    for row in mas:
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    elif mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
    if zeroes == 0:
        return "Piece"


pygame.init()

size_block = 200
margin = 5
width = height = (size_block * 3) + (margin * 4)

size_window = width, height

screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("TicTakToe")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

massive = [[0] * 3 for i in range(3)]
query = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if massive[row][col] == 0:
                if query % 2 == 0:
                    massive[row][col] = "x"
                    query = (query + 1) % 2
                else:
                    query = (query + 1) % 2
                    massive = bot(mas=massive)

    for row in range(3):
        for col in range(3):
            if massive[row][col] == "x":
                color = red
            elif massive[row][col] == "o":
                color = green
            else:
                color = white
            y = row * size_block + (row + 1) * margin
            x = col * size_block + (col + 1) * margin

            pygame.draw.rect(screen, color, (x, y, size_block, size_block))

            if color == red:
                pygame.draw.line(screen, white, (x + 3 + 3, y + 3), (x + size_block - 5 - 3, y + size_block - 2 - 3), 7)
                pygame.draw.line(screen, white, (x + 4 + 3, y + size_block - 2 - 3), (x + size_block - 5 - 3, y + 3), 7)
            elif color == green:
                pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 7)

    win = False
    if (query - 1) % 2 == 0:  # x
        win = check_win(massive, "x")
    elif (query - 1) % 2 != 0:  # o
        win = check_win(massive, "o")

    if win:
        screen.fill(black)
        font = pygame.font.SysFont("Arial", 80)
        text = font.render(win, True, (green if win == "o" else red if win == "x" else white))
        text_rect = text.get_rect()
        text_x = screen.get_width() // 2 - text_rect.width // 2
        text_y = screen.get_height() // 2 - text_rect.height // 2
        screen.blit(text, [text_x, text_y])

    clock.tick(10)

    pygame.display.flip()