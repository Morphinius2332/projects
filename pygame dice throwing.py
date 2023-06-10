import pygame
import random

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dice Simulator")

# Set up the font
font = pygame.font.SysFont(None, 48)

# Set up the dice images
dice_images = [
    pygame.image.load("dice1.png"),
    pygame.image.load("dice2.png"),
    pygame.image.load("dice3.png"),
    pygame.image.load("dice4.png"),
    pygame.image.load("dice5.png"),
    pygame.image.load("dice6.png")
]

# Define the roll_dice function
def roll_dice():
    return random.randint(1, 6)

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Roll the dice
                dice_number = roll_dice()

                # Display the result
                screen.fill(WHITE)
                dice_image = dice_images[dice_number-1]
                screen.blit(dice_image, (screen_width/2 - dice_image.get_width()/2, screen_height/2 - dice_image.get_height()/2))
                result_text = font.render(f"The dice rolled a {dice_number}!", True, BLACK)
                screen.blit(result_text, (screen_width/2 - result_text.get_width()/2, 50))
                pygame.display.update()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
