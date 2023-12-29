import pygame
from settings import WIDTH, HEIGHT


COLOR = "#888888"
GRAVITY = 0.35


class Hero(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))

    def update(self, left, right):
        if left:
            self.xvel = -5  # Лево = x- n

        if right:
            self.xvel = 5 # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel

    def get_position(self):
        return self.x, self.y

    def set_position(self, pos):  # изменение координат
        self.x, self.y = pos

    # def render(self, screen):  # отрисовка персонажа

