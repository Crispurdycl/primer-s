import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir variables
WIDTH = 500
HEIGHT = 500
SNAKE_SIZE = 10
FPS = 15

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Definir la serpiente y la comida
snake = [(WIDTH / 2, HEIGHT / 2)]
food = (random.randint(0, WIDTH / SNAKE_SIZE - 1) * SNAKE_SIZE, 
        random.randint(0, HEIGHT / SNAKE_SIZE - 1) * SNAKE_SIZE)
direction = "right"
score = 0

# Dibujar la serpiente y la comida en la pantalla
def draw():
    screen.fill(BLACK)
    for s in snake:
        pygame.draw.rect(screen, GREEN, (s[0], s[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.update()

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
while running:
    # Actualizar la posición de la serpiente
    if direction == "right":
        snake.append((snake[-1][0] + SNAKE_SIZE, snake[-1][1]))
    elif direction == "left":
        snake.append((snake[-1][0] - SNAKE_SIZE, snake[-1][1]))
    elif direction == "up":
        snake.append((snake[-1][0], snake[-1][1] - SNAKE_SIZE))
    elif direction == "down":
        snake.append((snake[-1][0], snake[-1][1] + SNAKE_SIZE))

    # Comprobar si la serpiente ha chocado con algo
    if snake[-1][0] < 0 or snake[-1][0] >= WIDTH or snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or snake[-1] in snake[:-1]:
        running = False
    elif snake[-1] == food:
        # La serpiente ha comido la comida
        score += 1
       
