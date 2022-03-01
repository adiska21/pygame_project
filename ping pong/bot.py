import pygame
import random
import sys


def ball_restart():
    global ball_speed_x, ball_speed_y

    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))
    ball.center = (windows_width // 2, windows_height // 2)


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= windows_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= windows_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(bot):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= windows_height:
        player.bottom = windows_height


def bot_animation():
    bot.y += bot_speed

    if bot.top <= 0:
        bot.top = 0
    if bot.bottom >= windows_height:
        bot.bottom = windows_height


def drawing():
    screen.fill(background_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, bot)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (windows_width / 2, 0), (windows_width / 2, windows_height))


def bot_ai():
    global bot_speed

    if bot.y < ball.y:
        bot.top += bot_speed
    if bot.y > ball.y:
        bot.top -= bot_speed * 2


def for_():
    global player_speed, bot_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


pygame.init()

windows_width = 1000
windows_height = 700
size_window = (windows_width, windows_height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Pong")

background_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball = pygame.Rect(windows_width // 2 - 15, windows_height // 2 - 15, 30, 30)
player = pygame.Rect(windows_width - 20, windows_height / 2 - 70, 10, 140)
bot = pygame.Rect(10, windows_height / 2 - 70, 10, 140)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
bot_speed = 6.99999

clock = pygame.time.Clock()

while True:
    for_()

    bot_ai()

    ball_animation()
    player_animation()
    bot_animation()

    drawing()

    clock.tick(60)
    pygame.display.flip()