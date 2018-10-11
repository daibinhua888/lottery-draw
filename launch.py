import pygame
import random
from pygame.locals import *

pygame.init()  # 2、初始化init() 及设置

screen_list=pygame.display.list_modes()

screen_size = screen_list[0]
RND_FROM=1
RND_END=430
background_image_filename = 'resources/back.jpg'
background_wav_file='resources/40.wav'
font_ZHCN=pygame.font.SysFont('SimHei', 100)
congratulationWord_color=255,255,255
congratulationWord_text_position=(700, 230)
text_position_y = 450
random_text_position1=(1000, text_position_y)
random_text_position2=(random_text_position1[0]+80, text_position_y)
random_text_position3=(random_text_position2[0]+80, text_position_y)


import RandomNumberSprite
screen = pygame.display.set_mode(screen_size, FULLSCREEN, 32)

background = pygame.image.load(background_image_filename).convert()
background = pygame.transform.scale(background, screen_size)



current_status = 'init'
random1_int = 0
random2_int = 0
random3_int = 0

background_music = pygame.mixer.Sound(background_wav_file)

clock=pygame.time.Clock()

number1 = RandomNumberSprite.RandomNumberSprite(screen,random_text_position1)
number2 = RandomNumberSprite.RandomNumberSprite(screen,random_text_position2)
number3 = RandomNumberSprite.RandomNumberSprite(screen,random_text_position3)
number1.number=random1_int
number2.number=random2_int
number3.number=random3_int

import utils

# 4、游戏循环，进入游戏循环就以为着游戏的开始
while True:
    # 5、获取事件并逐类响应
    for event in pygame.event.get():
        # print(event)
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
        if event.type == MOUSEBUTTONUP:
            if current_status == 'init' or current_status == 'stop':
                current_status = 'start'
                background_music.play()
                number1.begin()
                number2.begin()
                number3.begin()

            if number1.isInitialized() and not number1.isDone() and number1.isMousePositionHit(pygame.mouse.get_pos()):
                number1.stop()
            if number2.isInitialized() and not number2.isDone() and number2.isMousePositionHit(pygame.mouse.get_pos()):
                number2.stop()
            if number3.isInitialized() and not number3.isDone() and number3.isMousePositionHit(pygame.mouse.get_pos()):
                number3.stop()

            if number1.isInitialized() and number1.isDone() and number2.isInitialized() and number2.isDone() and number3.isInitialized() and number3.isDone():
                current_status = 'stop'
                background_music.stop()

    screen.blit(background, (0, 0))

    if number1.isInitialized() and not number1.isDone():
        while True:
            number1.switchTo(random.randint(0, 4))
            if utils.inRange(RND_FROM, RND_END, number1.number, number2.number, number3.number):
                break
    if number2.isInitialized() and not number2.isDone():
        while True:
            number2.switchTo(random.randint(0, 9))
            if utils.inRange(RND_FROM, RND_END, number1.number, number2.number, number3.number):
                break
    if number3.isInitialized() and not number3.isDone():
        while True:
            number3.switchTo(random.randint(0, 9))
            if utils.inRange(RND_FROM, RND_END, number1.number, number2.number, number3.number):
                break

    if current_status == 'stop':
        random_text = str(number1.number)+str(number2.number)+str(number3.number)
        congratulationWord = font_ZHCN.render('恭喜！'+random_text, True, congratulationWord_color)
        screen.blit(congratulationWord, congratulationWord_text_position)
    elif not current_status == 'init':
        number1.draw()
        number2.draw()
        number3.draw()

    pygame.display.update()  # 6、update 更新屏幕显示
    clock.tick(100)


