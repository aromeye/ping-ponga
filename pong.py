from pygame import *
from random import randint
from time import *

init()

SCREEN_WIDTH, SCREEN_HEIGHT= 800, 600
SPRITE_WIDTH, SPRITE_HEIGHT = 65, 65
background = (0, 0, 0)
pelota_img = 'ball.png'
FPS = 60

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('pelota')

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, pos_image, pos_x, pos_y, size_x, size_y):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)
        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(pos_image), (size_x, size_y))
        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

class Pelota(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = randint(0, SCREEN_WIDTH - 50)


pelota = Pelota(pelota_img, 400, 300, 50, 50)

#clock = time.Clock()
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(background)

    display.update()
    #clock.tick(FPS)

quit()
