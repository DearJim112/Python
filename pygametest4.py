import pygame
import sys
from math import *
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
x,y=width/2,height/2+40
# top_left=(223, 127)
#设置字体和文字


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
font_big = pygame.font.SysFont("微软雅黑",45)
font_small = pygame.font.SysFont("微软雅黑",25)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
game_over = font_big.render("Game Over",True,BLACK)
speed1 = font_small.render("speed=1km/h",True,RED)
speed2 = font_small.render("speed=2km/h",True,BLACK)
EPS_speed1 = font_small.render("EPS_speed=1",True,RED)
EPS_speed2 = font_small.render("EPS_speed=10",True,BLACK)
wheel_deg = font_big.render("wheel_deg",True,BLUE)
steering_deg = font_big.render("steering_deg",True,BLUE)

pygame.display.set_caption("遥控泊车")



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
# cars=pygame.sprite.Group()
# cars.add(car)
# print(cars.sprites())
degree=0
Vdegree=0
newcar=Player()
newcar.image = pygame.transform.rotate(car.image, angle=0)
#车辆参数
speed=0.5
ddegree=0.1
#C车辆之心
Lr=138*0.5 #后悬长度
#beta滑移角
#seta_r=后轮偏角
#o 转向圆心
Lf=138*0.5#前悬长度
#R 转向半径
# fai 偏航角
# seta_f前轮偏角
Lb=138
Ltw=70*0.9
yaw=0
eps_speed1=40/540/60*10
x0=0
y0=0
R=0
degree=0
seta_f=0
while True:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    print([x0, y0, 2 * R, 2 * R])
    # pygame.draw.arc(screen, RED, [x0, y0,  2*R, 2*R], 180 - degree - yaw * 180 / pi, 180, 3)

    # print(R)
    screen.blit(speed1, (0, 0))
    screen.blit(speed2, (200, 0))
    screen.blit(EPS_speed1, (0, 40))
    screen.blit(EPS_speed2, (200, 40))
    screen.blit(wheel_deg, (0, 400))
    screen.blit(steering_deg, (0, 430))
    # print(x,y)
    seta_f = degree / 180 * pi
    R = Lb / (abs(tan(seta_f)) + 1e-15)
    if (yaw + seta_f)<0:
        alaf = (yaw + seta_f) % (-2 * pi)
        x0 = x - R * sin(alaf)
        y0 = y + R * cos(alaf)
    else:
        alaf = (yaw + seta_f) % (2 * pi)
        x0 = x - R * sin(alaf)
        y0 = y - R * cos(alaf)
    pygame.draw.arc(screen, RED, [x0-R, y0-R, 2 * R, 2 * R],0, 2*pi, 3)
    # pygame.draw.arc(screen, RED, [x, y, 150, 150], 0, 2 * pi, 3)
    # pygame.draw.arc(screen, RED, [x, y,  R,  R], 0, pi, 3)
    wheel_deg = font_big.render(str(degree), True, BLUE)
    steering_deg = font_big.render(str(degree*540/40), True, BLUE)
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
    # print('degree=',degree)
    # print('yaw=',yaw/pi*180)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.MOUSEBUTTONUP:
            # print('up')
            mousex,mousey=pygame.mouse.get_pos()
            # print(mousex, mousey)
            if ((200>mousex>0) & (30>mousey>0)):
                # print(mousex,mousey)
                speed1 = font_small.render("speed=2km/h", True, RED)
                speed2 = font_small.render("speed=4km/h", True, BLACK)
                speed=0.5
            if ((400 > mousex > 200) & (30 > mousey > 0)):
                speed1 = font_small.render("speed=2km/h", True, BLACK)
                speed2 = font_small.render("speed=4km/h", True, RED)
                speed=1
            if ((200 > mousex > 0) & (60 > mousey > 40)):
                eps_speed1= 40/540/60*10
                EPS_speed1 = font_small.render("EPS_speed=10°/s",True,RED)
                EPS_speed2 = font_small.render("EPS_speed=100°/s", True, BLACK)
            if ((400 > mousex > 200) & (60 > mousey > 40)):
                eps_speed1 = 40/54/60*10
                EPS_speed1 = font_small.render("EPS_speed=10°/s",True,BLACK)
                EPS_speed2 = font_small.render("EPS_speed=100°/s", True, RED)
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
        # print(seta_f)


        # a = 2 * speed * tan(-degree / 180 * pi) / (2 * Lb + Ltw * tan(abs(degree / 180 * pi)))
        # yaw = yaw + a
        # dx = -speed * cos(a) -Lb*sin(a)
        # dy = -speed * sin(a) -Lb*(1-cos(a))
        # rx = dx * cos(-yaw / 180 * pi) + dy * sin(-yaw / 180 * pi)
        # ry = dy * cos(-yaw / 180 * pi) - dx * sin(-yaw / 180 * pi)
        # y = y - ry
        # x = x + rx
        newcar.image = pygame.transform.rotate(car.image, angle=yaw * 180 / pi)
        # r = image.get_rect()
        # newcar.rect.center = (x,y)
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

        # if 0<alaf<pi/2:
        #     print('第一象限')
        #     x0=x-R*sin(alaf)
        #     y0=y-R*cos(alaf)
        # elif pi/2<alaf<pi:
        #     print('第2象限')
        #     x0=x+R*cos(alaf)
        #     y0=y-R*sin(alaf)
        # elif pi<alaf<3*pi/2:
        #     print('第3象限')
        #     print(alaf/pi*180)
        #     x0=x+R*cos(alaf)
        #     y0=y+R*sin(alaf)
        # elif 3*pi/2<alaf<2*pi:
        #     x0=x+R*cos(alaf)
        #     y0=y-R*sin(alaf)
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
        degree += eps_speed1
        if degree>40:
            degree=40
    if pressed_key[pygame.K_RIGHT]:
        degree -= eps_speed1
        if degree<-40:
            degree=-40
        # if event.type ==pygame.
    # blocks_hit_list =pygame.sprite.spritecollide(newcar, enemires, False)
    blocks_hit_list =pygame.sprite.spritecollideany(newcar,enemires)
    if blocks_hit_list!=None:
        screen.blit(game_over,(200,200))

    if pressed_key[pygame.K_s]:
        x,y=width/2,height/2+40
        yaw=0
        degree=0
    # enemies = pygame.sprite.spritecollide(player, enemy, False)
    # if pygame.sprite.spritecollideany(player,enemy,False):
    #     print("碰撞了")

    # print(car)
    pygame.display.update()

