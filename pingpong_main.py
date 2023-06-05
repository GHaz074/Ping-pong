from pygame import *

win_witdh = 600
win_height = 500
window = display.set_mode((win_witdh,win_height))
#window.set_captons('Ping-pong')
font.init()
back = (200,255,255)

class GameSprite(sprite.Sprite):
    def __init__(self,filename,x,y,size_x,size_y,speed):
      super().__init__()
      self.image = transform.scale(image.load(filename),(size_x,size_y))
      self.speed = speed
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
        self.reset()
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
        self.reset()

run = True
finish = False
clock = time.Clock()
fps = 60
racket1 = Player('racket.png',50,200,50,150,4)
racket2 = Player('racket.png',500,200,50,150,4)
ball = GameSprite('ball.png',200,200,50,50,4)
font_t = font.SysFont('Arial',35)
lose1 = font_t.render('Player 1 lose',True,(180,0,0))
lose2 = font_t.render('Player 2 lose',True,(180,0,0))
restart = font_t.render("Press 'R' for restart",True,(180,0,0))
speed_x = 3
speed_y = 3
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_r and finish == True:
                finish = False
                racket1.rect.x = 50
                racket1.rect.y = 200
                racket2.rect.x = 500
                racket2.rect.y = 200
                ball.rect.x = 200
                ball.rect.y = 200
                speed_x = 3
                speed_y = 3
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.y > win_height - 50:
            speed_y *= -1
        if sprite.collide_rect(ball,racket1) == True or sprite.collide_rect(ball,racket2) == True:
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(lose1,(200,200))
            window.blit(restart,(200,250))
            finish = True
        if ball.rect.x > win_witdh - 50:
            window.blit(lose2,(200,200))
            window.blit(restart,(200,250))
            finish = True
        ball.reset()
    display.update()
    clock.tick(fps)
