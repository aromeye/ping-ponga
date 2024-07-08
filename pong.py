from pygame import *
from random import randint

init()

SCREEN_WIDTH, SCREEN_HEIGHT= 800, 600
SPRITE_WIDTH, SPRITE_HEIGHT = 65, 65
background = transform.scale(image.load('CAT.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_solid = (0, 0, 255)
pelota_img = 'ball.png'
wall_L_img = 'wall_L.jpg'
wall_R_img = 'wall_R.jpg'
FPS = 60
score_L = 0
score_R = 0

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('pelota')

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, pos_image, pos_x, pos_y, size_x, size_y, speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)
        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(pos_image), (size_x, size_y))
        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.widht = size_x
        self.height = size_y
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Pelota(GameSprite):
    def __init__(self, pos_image, pos_x, pos_y, size_x, size_y, speed_y, speed_x, speed=0):
        # llamamos al constructor de la clase (Sprite):
        super().__init__(pos_image, pos_x, pos_y, size_x, size_y, speed)
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= SCREEN_HEIGHT -self.height or self.rect.y <= 0:
            self.speed_y *= -1 
        
        if self.rect.x >= SCREEN_WIDTH - self.widht:
            global score_R
            score_R += 1
            self.rect.x = 300
            self.rect.y = 400
            self.speed_x *= -1
            print(score_R)

        if self.rect.x <= 0:
            global score_L
            score_L += 1
            self.rect.x = 300
            self.rect.y = 400
            self.speed_x *= -1
            print(score_L)



class Wall1(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 305:
           self.rect.y += self.speed

class Wall2(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 305:
           self.rect.y += self.speed           

pelota = Pelota(pelota_img, 400, 300, 50, 50, 5, 5)
wall_R = Wall1(wall_R_img, 780, 175, 10, 300, 5)
wall_L = Wall2(wall_L_img, 20, 175, 10, 300, 5)

clock = time.Clock()
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0, 0))
        pelota.reset()
        pelota.update()
        wall_R.reset()
        wall_R.move()
        wall_L.reset()
        wall_L.move()
        
        if sprite.collide_rect(pelota, wall_R) or sprite.collide_rect(pelota, wall_L):
            pelota.speed_x *= -1

    display.update()
    clock.tick(FPS)

quit()
