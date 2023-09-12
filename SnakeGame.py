import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 40
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the clock
clock = pygame.time.Clock()

# Snake variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)

# Food variables
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Initialize the font for displaying the score
pygame.font.init()
font = pygame.font.Font(None, 36)

# Game variables
score = 0
game_over = False  # Add a game over flag

# Exit button dimensions
exit_button_rect = pygame.Rect(WIDTH - 100, 10, 90, 30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            if exit_button_rect.collidepoint(event.pos):
                running = False  # quit game when exit button pressed

    if not game_over:  # update if the game is not over
        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        # Check for collisions and update the score
        if snake[0] == food:
            score += 1
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        if (
            snake[0][0] < 0
            or snake[0][0] >= GRID_WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= GRID_HEIGHT
            or snake[0] in snake[1:]
        ):
            game_over = True  # Set game over flag

    # Draw everything
    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    pygame.draw.rect(
        screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Display the score on the screen
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display the "Exit" button
    pygame.draw.rect(screen, WHITE, exit_button_rect)
    exit_text = font.render("Exit", True, BLACK)
    screen.blit(exit_text, (WIDTH - 90, 15))

    # Display the "Game Over" pop-up when the game is over
    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        score_text = font.render(f"Your Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 70, HEIGHT // 2 + 20))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit the game
pygame.quit()
sys.exit()
