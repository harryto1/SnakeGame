import pygame
import random
import time

# Initialize the game
pygame.init()


# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake!")
screen.fill((255, 255, 255))
pygame.display.flip()

# Set up the clock
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#Functions
def generate_apple():
    apple = pygame.Rect(random.randint(1, 799), random.randint(1, 599), 20, 20)
    return apple

def snake_movement():
    #Handle snake movement
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].x = snake_body[i - 1].x
        snake_body[i].y = snake_body[i - 1].y

    # Update the position of the snake's head
    snake_body[0].x += snake_speed_x
    snake_body[0].y += snake_speed_y



    #Handle snake going off the screen
    if snake_body[0].x > screen_width:
        snake_body[0].x = 0
    if snake_body[0].x < 0:
        snake_body[0].x = screen_width
    if snake_body[0].y > screen_height:
        snake_body[0].y = 0
    if snake_body[0].y < 0:
        snake_body[0].y = screen_height



# Set up the fonts
font = pygame.font.Font(None, 36)

#Objects
apple = generate_apple()
snake_position = [400, 300]
snake_body = [
]
for i in range(0, 50):
    snake_body.append(pygame.Rect(400 - i * 20, 300, 20, 20))



#Variables
snake_speed_x = 3
snake_speed_y = 0
change_to = 'RIGHT'
direction = 'RIGHT'

#Score
score = 0
initial_time = time.time()
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #KEYUP
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'LEFT':
        snake_speed_x = -3
        snake_speed_y = 0
    if direction == 'RIGHT':
        snake_speed_x = 3
        snake_speed_y = 0
    if direction == 'UP':
        snake_speed_y = -3
        snake_speed_x = 0
    if direction == 'DOWN':
        snake_speed_y = 3
        snake_speed_x = 0


    #Game Logic
    snake_movement()


    #Visuals
    screen.fill(BLACK)

    for body in snake_body:
        pygame.draw.rect(screen, GREEN, body)
    pygame.draw.rect(screen, RED, apple)

    if snake_body[0].colliderect(apple):
        apple = generate_apple()
        for i in range(25):
            snake_body.append(pygame.Rect(snake_body[-1].x, snake_body[-1].y, 20, 20))
        score += 1

    if time.time() - initial_time > 2:
        for body in snake_body[15:]:
            if snake_body[0].colliderect(body):
                running = False

    #Score Setup
    score_text = basic_font.render(f'Score: {score}', True, (255, 255, 255), (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()