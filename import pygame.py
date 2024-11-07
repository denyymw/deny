import pygame
import random
import sys


# inicio de todo
pygame.init()


# colocar dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # verifica las medidas
pygame.display.set_caption("Galaga Fake") # nombre para la ventana


# colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# FPS
clock = pygame.time.Clock()
FPS = 60


# imagen de la nave jugador
player_image = pygame.image.load("nave.png") 
player_image.set_colorkey((255, 255, 255))  # hace transparente el fondo  
player_image = pygame.transform.scale(player_image, (50, 50))


# creacion de clase para el jugador
class Player(pygame.sprite.Sprite): # permite que goze la clasde de todas las funcionalidades
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50) # tamaño que se de 50x50 en la imagen de nave
        self.speed = 5
   
    def update(self): # que la nave pueda moverse de izquierda a derecha segun el jugador pulse
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed


# se crea los disparos que el jugador podra colocar, cositas blancas
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7


    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()  # si se sale el disparo lo elimina


#  se crea clase para la realizacion de las posiciones , inicio y forma de los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemigo1.png")
        self.image.set_colorkey((255, 255, 255))  # hace transparente el fondo blanco
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)
   
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            # permite colocar nuevamente al enemigo en la parte superiror al salir de la pantalla
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)


# dirrige los objetos que se tienen a los sprite por aparte
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()


# crea el jgador y lo dirige al sprite todo para su correcta ejecucion
player = Player()
all_sprites.add(player)


# crea enemigos con un numero especifico de creacion inicial
for i in range(15):  
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


# funcion para que cuando los enemigos toquen la nave se acabe el juego
def end_game():
    print("¡GAME OVER!")
    pygame.quit()
    exit()




def draw_button(text):
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
    pygame.draw.rect(screen, WHITE, button_rect) # color del boton
    font = pygame.font.Font(None, 74) # tamaño de la fuente
    text_surface = font.render(text, True, BLACK) 
    screen.blit(text_surface, (button_rect.centerx - text_surface.get_width() // 2, button_rect.centery - text_surface.get_height() // 2))
    return button_rect


def main_menu():
    while True:
        screen.fill(BLACK)
        button_rect = draw_button("PLAY") # texto que mostrara
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    game()


        pygame.display.flip()


def game():
    running = True
    while running:
        clock.tick(FPS)  
        screen.fill(BLACK)  # limpia la pantalla
       
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # permite que si se da espacio lnze una bala
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)


        # actualiza y permite seguir en funcion el sprite
        all_sprites.update()


        # colisiones entre el jugador y los enemigos
        for bullet in bullets:
            enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
            for enemy in enemies_hit:
                bullet.kill()  # permite eliminar el disparo al golpear al enemigo
                enemy = Enemy()  # permite crear un nuevo enemigo
                all_sprites.add(enemy)
                enemies.add(enemy)


        # Comprobar colisiones entre el jugador y los enemigos
        if pygame.sprite.spritecollideany(player, enemies):
            end_game() # se llama a la funcion para que se termine el juego al ser colisionados


        all_sprites.draw(screen)


        
        pygame.display.flip()


    pygame.quit()


main_menu()
