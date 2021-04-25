from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class PLayer (GameSprite):
    def update_r (self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y< win_height - 80 :
            self.rect.y += self.speed
    def update_l (self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y< win_height - 80 :
            self.rect.y += self.speed


win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("Background.jpg"), (win_width, win_height))



racket1 = PLayer('rock.jpg', 30,200,4,50,15)
racket2 = PLayer('rock.jpg',520,200,4,50,15)
ball =GameSprite("ball.png",200,200,4,50,50)

font.init()
font1 =font.Font(None,70)
lose1 =font1.render('YOU LOOSE PLAYER 1',True,(246,129,30))
lose2 = font1.render('YOU LOOSE PLAYER 2',True,(246,129,30))

speed_x=3
speed_y=3

game = True
finish =False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish !=True:
        window.blit(background,(0, 0))
        racket1.update_l()
        racket2.update_r()  
        ball.rect.x +=speed_x 
        ball.rect.y +=speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        

        if ball.rect.y > win_height - 50 or ball.rect.y <0:
            speed_y *= -1
        

        if ball.rect.x < 0 :
            finish =True
            window.blit(lose1 , (200,200))
            game_over = True


        if ball.rect.x > win_width :
            finish =True
            window.blit(lose2 , (200,200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
