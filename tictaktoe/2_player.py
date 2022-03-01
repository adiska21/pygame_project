import pygame
import sys


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
    return False


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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if massive[row][col] == 0:
                if query % 2 == 0:
                    massive[row][col] = "x"
                    query = (query + 1) % 2
                else:
                    massive[row][col] = "o"
                    query = (query + 1) % 2

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

    pygame.display.flip()