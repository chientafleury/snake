import pygame
import random
import time

# Inisialisasi pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game - Makan Apel")

# Ular
snake_block = 20
snake_speed = 10

# Fungsi untuk menggambar ular
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Fungsi utama game
def game_loop():
    game_over = False
    game_close = False

    # Posisi awal ular
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Perubahan posisi
    x1_change = 0
    y1_change = 0

    # Body ular (awalnya panjang 1)
    snake_list = []
    length_of_snake = 1

    # Posisi apel (random)
    apple_x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
    apple_y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 50)
            message = font.render("Game Over! Press Q-Quit or P-Play Again", True, RED)
            screen.blit(message, [screen_width / 60, screen_height / 10])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:  # Hindari gerakan berlawanan
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Jika menabrak border, game over
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        # Gambar apel
        pygame.draw.rect(screen, RED, [apple_x, apple_y, snake_block, snake_block])

        # Update posisi ular
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Hapus ekstra segment jika ular tidak makan
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Cek tabrakan dengan tubuh sendiri
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)

        # Tampilkan skor
        font = pygame.font.SysFont(None, 35)
        score = font.render(f"Skor: {length_of_snake - 1}", True, WHITE)
        screen.blit(score, [10, 10])

        pygame.display.update()

        # Cek jika ular makan apel
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, screen_width - snake_block) / snake_block) * snake_block
            apple_y = round(random.randrange(0, screen_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1  # Tambah panjang ular

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Jalankan game
game_loop()