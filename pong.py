from pygame import *
from random import randint

init()

SCREEN_WIDTH, SCREEN_HEIGHT= 800, 600
SPRITE_WIDTH, SPRITE_HEIGHT = 65, 65
background = (0, 0, 255)
pelota_img = 'ball.png'
FPS = 60

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



class Wall1(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 635:
           self.rect.y += self.speed

pelota = Pelota(pelota_img, 400, 300, 50, 50, 5, 5)
wall = Wall1(pelota_img, 780, 175, 10, 300, 0)

clock = time.Clock()
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(background)
        pelota.reset()
        pelota.update()
        wall.reset()
        wall.move()
        

    display.update()
    clock.tick(FPS)

quit()
