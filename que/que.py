from random import sample
import pygame


def chose():
    indexes = sample(range(0, 97), 97)
    import sqlite3

    con = sqlite3.connect(r"que\Question.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT ques FROM qu""").fetchall()
    questions1 = []
    questions_with = []
    for j in indexes:
        questions1.append(result[j])
    for n in range(10):
        b = questions1[n]
        result = cur.execute(f"""SELECT * FROM qu
                        WHERE ques = '{''.join(b)}'""").fetchall()
        questions_with.append(result)
    return questions_with


if __name__ == "__main__":
    pygame.init()
    size_window = width, height = 600, 600
    screen = pygame.display.set_mode(size_window)
    screen.fill("black")
    questions = chose()
    coords = [((300, 150), (300, 175), (300, 200), (300, 225), (300, 250)),
              (165, 372), (440, 373), (165, 525), (440, 522)]
    num = [None, 'a)', 'b)', 'c)', 'd)']
    coords_of_rects = [None, (29, 345, 250, 60), (310, 344, 250, 60), (29, 491, 250, 60), (310, 488, 250, 60)]
    running = True
    col_of_true_ans = 0
    clock = pygame.time.Clock()
    ansflag = False
    for i in range(23):
        if running:
            if i == 21:
                screen.fill('black')
                fontObj = pygame.font.Font('freesansbold.ttf', 20)
                textSurfaceObj = fontObj.render(f'Верных ответов {col_of_true_ans}', True, pygame.Color('green'))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (300, 300)
                pygame.draw.rect(screen, pygame.Color('green'), (150, 150, 300, 300), 1)
                screen.blit(textSurfaceObj, textRectObj)
                clock.tick(1)
                pygame.display.update()
            elif i % 2 == 1:
                f = True
                flag_fail = False
                screen.fill('black')
                m_position = None
                if i == 19:
                    form = 9
                else:
                    form = (i + 1) // 2
                true_ans = questions[form][0][-1]
                for j in range(5):
                    elem = questions[form][0][j]
                    elem = elem.split()
                    flag = False
                    abc = []
                    l = len(elem)
                    if l > 7:
                        if 15 > l > 7:
                            for h in range(1, 3):
                                abc.append(' '.join(elem[0:7]))
                                abc.append(' '.join(elem[7:]))
                                fontObj = pygame.font.Font('freesansbold.ttf', 17)
                                textSurfaceObj = fontObj.render(abc[h - 1], True, pygame.Color('red'))
                                textRectObj = textSurfaceObj.get_rect()
                                textRectObj.center = coords[j][h]
                                screen.blit(textSurfaceObj, textRectObj)
                                coord = coords[j][h]
                                f = False
                        elif 23 > l > 15:
                            for h in range(1, 4):
                                abc.append(' '.join(elem[0:7]))
                                abc.append(' '.join(elem[9:15]))
                                abc.append(' '.join(elem[15:]))
                                fontObj = pygame.font.Font('freesansbold.ttf', 17)
                                textSurfaceObj = fontObj.render(abc[h - 1], True, pygame.Color('red'))
                                textRectObj = textSurfaceObj.get_rect()
                                textRectObj.center = coords[j][h]
                                screen.blit(textSurfaceObj, textRectObj)
                                f = False
                        elif 35 > l > 23:
                            for h in range(1, 5):
                                abc.append(' '.join(elem[0:7]))
                                abc.append(' '.join(elem[7:15]))
                                abc.append(' '.join(elem[15:23]))
                                abc.append(' '.join(elem[23:]))
                                fontObj = pygame.font.Font('freesansbold.ttf', 17)
                                textSurfaceObj = fontObj.render(abc[h - 1], True, pygame.Color('red'))
                                textRectObj = textSurfaceObj.get_rect()
                                textRectObj.center = coords[j]
                                screen.blit(textSurfaceObj, textRectObj)
                                f = False
                    elif f:
                        abc = ' '.join(elem)
                        fontObj = pygame.font.Font('freesansbold.ttf', 17)
                        textSurfaceObj = fontObj.render(abc, True, pygame.Color('red'))
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = coords[0][0]
                        screen.blit(textSurfaceObj, textRectObj)
                        f = False
                    else:
                        abc = num[j] + ' ' + ' '.join(elem)
                        fontObj = pygame.font.Font('freesansbold.ttf', 17)
                        textSurfaceObj = fontObj.render(abc, True, pygame.Color('red'))
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = coords[j]
                        pygame.draw.rect(screen, pygame.Color('red'), coords_of_rects[j], 1)
                        screen.blit(textSurfaceObj, textRectObj)
                    pygame.display.flip()

                    while True and j == 4:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    running = False
                                    exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                m_position = event.pos
                                flag_abc = True
                                x, y = m_position
                                for w in coords_of_rects:
                                    if w is None:
                                        continue
                                    x1, y1, we, hi = w
                                    if x1 <= x <= x1 + we and y1 <= y <= y1 + hi:
                                        answer = coords_of_rects.index(w)
                                        if answer == true_ans:
                                            ansflag = True
                                            print('True')
                                            col_of_true_ans += 1
                                        else:
                                            ansflag = False
                                        flag = True

                        if flag:
                            break
            else:
                if ansflag:
                    screen.fill("black")
                    pygame.display.update()
                    for _ in range(10):
                        pygame.display.update()
                        fontObj = pygame.font.Font('freesansbold.ttf', 20)
                        textSurfaceObj = fontObj.render('Ответ Верный', True, pygame.Color('green'))
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = (300, 300)
                        pygame.draw.rect(screen, pygame.Color('green'), (150, 150, 300, 300), 1)
                        screen.blit(textSurfaceObj, textRectObj)
                        clock.tick(10)
                        pygame.display.update()

                else:
                    if i != 0:
                        screen.fill("black")
                        pygame.display.update()
                        for _ in range(10):
                            fontObj = pygame.font.Font('freesansbold.ttf', 20)
                            textSurfaceObj = fontObj.render('Ответ Не Верный', True, pygame.Color('red'))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (300, 300)
                            pygame.draw.rect(screen, pygame.Color('red'), (150, 150, 300, 300), 1)
                            screen.blit(textSurfaceObj, textRectObj)
                            clock.tick(10)
                            pygame.display.update()
