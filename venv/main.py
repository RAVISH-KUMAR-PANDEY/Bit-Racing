import pygame
import time
import random


pygame.init()

crash_sound = pygame.mixer.Sound('Crash.wav')
pygame.mixer.music.load('Leveled_Up.wav')

display_width = 800
display_height = 600
car_width = 60
car_height = 88
black = (0,0,0)
green = (0,255,0)
bright_green = (32,182,42)
green_b = (63,128,66)
white = (255,255,255)
red = (200, 0, 0)
blue = (132,129,208)
bright_red = (255,0,0)
bright_blue = (189,188,237)
obs_color = (53,155,255)
pause = False


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bit Racing')
carImg = pygame.image.load('Car.png')
clock = pygame.time.Clock()
bck_img = pygame.image.load('URy5F.png')
obcar_img = pygame.image.load('racecar.png')
coll_img = pygame.image.load('collision.png')
rd_img = pygame.image.load('road3.png')
p_background = pygame.image.load('th.png')
GameIcon = pygame.image.load('CarIcon1.png')
pygame.display.set_icon(GameIcon)

def obs_dodged(count):
    font = pygame.font.Font(None,25)
    text = font.render('Dodged: '+str(count),True,black)
    gameDisplay.blit(text,(0,0))


def obstacles(obx, oby):
    gameDisplay.blit(obcar_img,(obx,oby))


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    text_Surface = font.render(text, True, black)
    return text_Surface,text_Surface.get_rect()

def msg1_Display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf , TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2-100))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def msg_Display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf , TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def crash(x,y,flag,d_count):
    if flag == 1:
        gameDisplay.blit(coll_img,(x+10,y+20))
    elif flag ==2:
        gameDisplay.blit(coll_img,(x+10,y-10))

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    msg1_Display('Score : '+str(d_count))
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurface, TextRect = text_objects("You Crashed",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurface,TextRect)
    #msg_Display('You Crashed!!!')
    while True:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button('Play Again', 150, 450, 120, 50, green_b, bright_green, game_loop)
        button('QUIT!!', 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(p_background,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurface, TectRect = text_objects('Paused', largeText)
        TectRect.center = ((display_width) / 2, (display_height) / 2)
        gameDisplay.blit(TextSurface, TectRect)

        button('Continue', 150, 450, 100, 50, blue, bright_blue, unpause)
        button('QUIT!!', 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,i_color,a_color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x < mouse[0] < x+w and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, a_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, i_color, (x, y, w, h))
    sml_txt = pygame.font.Font('freesansbold.ttf', 20)
    txt_srf, txt_rct = text_objects(msg, sml_txt)
    txt_rct.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(txt_srf, txt_rct)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bck_img,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurface, TectRect = text_objects('Bit Racing',largeText)
        TectRect.center = ((display_width)/2,(display_height)/2)
        gameDisplay.blit(TextSurface,TectRect)
        button('GO!!',150,450,100,50,blue,bright_blue,game_loop)
        button('QUIT!!', 550, 450, 100, 50, red, bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    obs_startx = random.randrange(200,570)
    obs_starty = -600
    obs_speed = 5
    obs_width = 73
    obs_height = 80
    dodge_count = 0
    game_Exit = False
    rd_y =-300
    global pause
    pygame.mixer.music.play(-1)

    while not game_Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    #print("Left")
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    #print("Right")
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            #print(event)

        x += x_change
        gameDisplay.fill(green)
        gameDisplay.blit(rd_img,(180,rd_y))
        #obstacles(obx, oby, obw, obh, color):

        obstacles(obs_startx,obs_starty)

        if rd_y == 0:
            rd_y = -325
        else:
            rd_y += 5

        #gameDisplay.blit(obcar_img,(obs_startx1,obs_starty-300))


        obs_starty += obs_speed
        car(x,y)
        obs_dodged(dodge_count)

        if x > 630 - car_width or x < 180:
            flag = 1
            crash(x,y,flag,dodge_count)
        if y < obs_starty+obs_height:
            if (x+5) > obs_startx and (x + 5) < obs_startx+obs_width or (x + car_width - 5) > obs_startx and (x+car_width-5) < obs_startx+obs_width:
                flag = 2
                crash(x,y,flag,dodge_count)

        if obs_starty > display_height:
            obs_starty = 0 - car_height
            obs_startx = random.randrange(200,570)
            dodge_count += 1
            if obs_speed >= 15:
                obs_speed = 15
            else:
                obs_speed += 1
        pygame.display.update()
        clock.tick(45)
game_intro()
#game_loop()
