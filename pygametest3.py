import pygame
import sys
from math import *
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
x,y=width/2,height/2
# top_left=(223, 127)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("R-C - 副本.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)
        # self.rect.topleft=(100,100)
        # self.rect.bottomleft=(100,200)
        # self.rect.topright =(200,100)
        # self.rect.bottomright =(200,200)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("R-C.png")
        self.rect = self.image.get_rect()
        self.rect.center = (223, 127)
# 设置帧数
FPS = 60
clock = pygame.time.Clock()
background = pygame.image.load("park.jpg")

enemy1=Enemy()
enemy1.rect.center=(223, 127)
enemy2=Enemy()
enemy2.rect.center=(59, 130)
enemy3=Enemy()
enemy3.rect.center=(468, 125)
# enemy_rect=enemy.get_rect()
car = Player()
print(car.image)
print(car.rect)
enemires=pygame.sprite.Group()
enemires.add(enemy1)
enemires.add(enemy2)
enemires.add(enemy3)
cars=pygame.sprite.Group()
cars.add(car)
print(cars.sprites())
degree=0
Vdegree=0
newcar=Player()
newcar.image = pygame.transform.rotate(car.image, angle=0)
#车辆参数
speed=1
#C车辆之心
Lr=138*0.3 #后悬长度
#beta滑移角
#seta_r=后轮偏角
#o 转向圆心
Lf=138*0.3#前悬长度
#R 转向半径
# fai 偏航角
# seta_f前轮偏角
Lb=138*0.7
Ltw=70*0.9
yaw=0
while True:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    # screen.blit(car.image, car.rect)
    for enemy in enemires:
        screen.blit(enemy.image,enemy.rect)
    # car.rect.center = (x , y )

    # degree=0
    # car.rect()
    # newacr_rect = car.image.get_rect(center=car.image.get_rect(topleft=top_left).center)
    newcar.rect.center= (x,y)
    screen.blit(newcar.image, newcar.rect)
    # car.enemy
    # screen.blit(player1.image, player1.rect)
    # screen.blit(player.image, player.rect)
    # y-=1
    # x,y=pygame.mouse.get_pos()
    # print(x,y)
    print('degree=',degree)
    print('yaw=',yaw/pi*180)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pressed_key=pygame.key.get_pressed()
    if pressed_key[pygame.K_SPACE]:
        degree=0
    if pressed_key[pygame.K_DOWN]:
        seta_f = degree / 180 * pi
        beta = atan(Lr / (Lr + Lf) * tan(seta_f))
        dx = -speed * cos(yaw + beta)
        dy = -speed * sin(yaw + beta)
        dyaw = -speed * sin(beta) / Lr

        y = y - dy
        x = x + dx
        yaw = yaw + dyaw
        # a = 2 * speed * tan(-degree / 180 * pi) / (2 * Lb + Ltw * tan(abs(degree / 180 * pi)))
        # yaw = yaw + a
        # dx = -speed * cos(a) -Lb*sin(a)
        # dy = -speed * sin(a) -Lb*(1-cos(a))
        # rx = dx * cos(-yaw / 180 * pi) + dy * sin(-yaw / 180 * pi)
        # ry = dy * cos(-yaw / 180 * pi) - dx * sin(-yaw / 180 * pi)
        # y = y - ry
        # x = x + rx
        newcar.image = pygame.transform.rotate(car.image, angle=yaw * 180 / pi)
    if pressed_key[pygame.K_UP]:
        # R=Lb/tan(degree/180*pi)
        #两轮模型
        seta_f=degree/180*pi
        beta=atan(Lr/(Lr+Lf)*tan(seta_f))
        dx=speed*cos(yaw+beta)
        dy=speed*sin(yaw+beta)
        dyaw=speed*sin(beta)/Lr

        y=y-dy
        x=x+dx
        yaw=yaw+dyaw

        # a = 2 * speed * tan(degree / 180 * pi) / (2 * Lb + Ltw * tan(abs(degree / 180 * pi)))
        # yaw = yaw + a
        # dx = speed * cos(yaw)
        # dy = speed * sin(yaw)
        # rx = dx * cos(-yaw / 180 * pi) + dy * sin(-yaw / 180 * pi)
        # ry = dy * cos(-yaw / 180 * pi) - dx * sin(-yaw / 180 * pi)
        # y = y - ry
        # x = x + rx
        # Vdegree=Vdegree+degree/180
        newcar.image = pygame.transform.rotate(car.image, angle=yaw * 180 / pi)
        # newcar.rect = newcar.image.get_rect().center
    if pressed_key[pygame.K_LEFT]:
        degree += 1
        if degree>45:
            degree=45
    if pressed_key[pygame.K_RIGHT]:
        degree -= 1
        if degree<-45:
            degree=-45
        # if event.type ==pygame.
    blocks_hit_list =pygame.sprite.spritecollide(newcar, enemires, False)
    for hit in blocks_hit_list:
        print(blocks_hit_list )
        x,y=width/2,height/2
        yaw=0
        degree=0
    # enemies = pygame.sprite.spritecollide(player, enemy, False)
    # if pygame.sprite.spritecollideany(player,enemy,False):
    #     print("碰撞了")

    # print(car)
    pygame.display.update()

