import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (40, 40, 40)

# Font
font = pygame.font.SysFont(None, 36)

# Player settings
player_size = 20
player_pos = [50, 50]
player_speed = 5

# Score
score = 0

# Maze walls
walls = [
    pygame.Rect(100, 0, 20, 500),
    pygame.Rect(200, 100, 20, 500),
    pygame.Rect(300, 0, 20, 500),
    pygame.Rect(400, 100, 20, 500),
    pygame.Rect(0, 100, 500, 20),
    pygame.Rect(100, 300, 400, 20)
]

# Dots (food)
dots = []
for x in range(30, WIDTH, 40):
    for y in range(30, HEIGHT, 40):
        dot_rect = pygame.Rect(x, y, 5, 5)
        if not any(dot_rect.colliderect(wall) for wall in walls):
            dots.append(dot_rect)

# Ghost settings
ghosts = []
for _ in range(3):
    gx = random.randint(0, WIDTH - 20)
    gy = random.randint(0, HEIGHT - 20)
    ghosts.append({'rect': pygame.Rect(gx, gy, 20, 20), 'dir': random.choice(['up', 'down', 'left', 'right'])})

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pac-Man
    keys = pygame.key.get_pressed()
    old_pos = player_pos[:]
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    player_rect = pygame.Rect(player_pos[0] - 10, player_pos[1] - 10, 20, 20)

    # Wall collision for Pac-Man
    for wall in walls:
        if player_rect.colliderect(wall):
            player_pos = old_pos
            player_rect = pygame.Rect(player_pos[0] - 10, player_pos[1] - 10, 20, 20)

    # Draw maze walls
    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)

    # Draw and update dots
    for dot in dots[:]:
        if player_rect.colliderect(dot):
            dots.remove(dot)
            score += 10
        pygame.draw.rect(screen, WHITE, dot)

    # Move and draw ghosts
    for ghost in ghosts:
        rect = ghost['rect']
        dir = ghost['dir']
        if dir == 'up':
            rect.y -= 2
        elif dir == 'down':
            rect.y += 2
        elif dir == 'left':
            rect.x -= 2
        elif dir == 'right':
            rect.x += 2

        # Wall collision for ghosts
        for wall in walls:
            if rect.colliderect(wall):
                ghost['dir'] = random.choice(['up', 'down', 'left', 'right'])

        pygame.draw.rect(screen, RED, rect)

        # Collision with Pac-Man
        if rect.colliderect(player_rect):
            game_over_text = font.render("Game Over!", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, player_pos, player_size)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    # Win condition
    if not dots:
        win_text = font.render("You Win!", True, BLUE)
        screen.blit(win_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()