import pygame
import os
from PIL import Image

pygame.init()

height = 600
width = 1100
screen = pygame.display.set_mode((width, height))

running = [pygame.image.load(os.path.join("bola.png"))]
player = [pygame.image.load(os.path.join("player.png"))]

bg = pygame.image.load(os.path.join("slebew.jpg"))

class Ball:
    x = 80
    y = 310

    def __init__(self):
        self.run_img = running
        self.ball_run = True
        self.step_index = 0
        self.image = self.run_img[0]
        self.ball_rect = self.image.get_rect()
        self.ball_rect.x = self.x
        self.ball_rect.y = self.y

    def update(self):
        if self.ball_run:
            self.step_index += 1

        if self.step_index >= len(self.run_img):
            self.step_index = 0

        self.image = self.run_img[self.step_index]

    def draw(self, screen):
        screen.blit(self.image, self.ball_rect)

def main():
    run = True
    clock = pygame.time.Clock()
    ball = Ball()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(bg, (0, 0))  # Menampilkan background
        userinput = pygame.key.get_pressed()

        ball.draw(screen)
        ball.update()

        pygame.display.update()
        clock.tick(30)

main()

# Mengubah ukuran gambar bola
image = Image.open("bola.png")
new_width = 200  # Ganti dengan lebar baru yang diinginkan
new_height = 200  # Ganti dengan tinggi baru yang diinginkan
resized_image = image.resize((new_width, new_height))
resized_image.save("bola_resized.png")
image.close()
