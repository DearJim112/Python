import pygame
import sys

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
# 设置帧数
FPS = 30
clock = pygame.time.Clock()

# 颜色定义
WHITE = pygame.color.Color(255, 255, 255)
BLACK = pygame.color.Color(0, 0, 0, a=255)
RED = "#FF000000"
GREEN = "#00FF0000"
BLUE = (0, 0, 255)
#
screen.fill(WHITE)
pygame.draw.circle(screen, (RED), (83, 30), 8)  # E
pygame.draw.circle(screen, (RED), (150, 180), 30)  # E
pygame.draw.line(screen, BLUE, (0, 0), (140, 13))
X = 250
Y = 250
pi = 3.141526
angd = 0

pygame.draw.arc(screen, RED, [X - 100, Y - 100, 200, 200], angd - pi / 2, angd + pi, 3)
pygame.draw.arc(screen, GREEN, [X, Y, 100, 100], angd, angd + pi / 2, 3)

# 图相的绘制
player=pygame.image.load("R-C.png")
play_rect=player.get_rect()
x, y = 250, 250


class PLAYER:

    def __int__(self):
        x,y=(width/2,height/2)
        self.image = pygame.image.load("R-C.png")
        self.rect = self.image.get_rect(center=(x,y))


player1 = PLAYER()
print(player1)
print(player1.rect)
background = pygame.image.load("park.jpg")

enemy=pygame.image.load("R-C.png")
enemy_rect=enemy.get_rect()
# enemy=PLAYER()
# enemires=pygame.sprite.Group()
# enemires.add(enemy)
while True:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    screen.blit(player, (x,y))
    screen.blit(enemy,(1,1))
    # screen.blit(player1.image, player1.rect)
    # screen.blit(player.image, player.rect)
    # y-=1
    # x,y=pygame.mouse.get_pos()
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pressed_key=pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN]:
        y+=1
    if pressed_key[pygame.K_UP]:
        y -= 1
    if pressed_key[pygame.K_LEFT]:
        x -= 1
    if pressed_key[pygame.K_RIGHT]:
        x += 1
        # if event.type ==pygame.
    # pygame.sprite.spritecollide(play_rect, enemy_rect, True,False)
    # enemies = pygame.sprite.spritecollide(player, enemy, False)
    # if pygame.sprite.spritecollideany(player,enemy,False):
    #     print("碰撞了")
    pygame.display.update()
