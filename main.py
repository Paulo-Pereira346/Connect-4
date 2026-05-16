import pygame
import sys
import subprocess

pygame.init()

WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Colors
BACKGROUND = (18, 18, 18)

BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
RED = (231, 76, 60)

WHITE = (255, 255, 255)

BUTTON_HOVER = (70, 70, 70)

title_font = pygame.font.SysFont("arialblack", 70)
button_font = pygame.font.SysFont("arial", 38)

clock = pygame.time.Clock()

# Buttons
button_width = 350
button_height = 75

buttons = {
    "PVP MODE": {
        "rect": pygame.Rect(275, 180, button_width, button_height),
        "color": BLUE
    },

    "AI EASY": {
        "rect": pygame.Rect(275, 300, button_width, button_height),
        "color": GREEN
    },

    "AI MEDIUM": {
        "rect": pygame.Rect(275, 420, button_width, button_height),
        "color": GREEN
    },

    "AI HARD": {
        "rect": pygame.Rect(275, 540, button_width, button_height),
        "color": RED
    }
}

running = True

while running:

    screen.fill(BACKGROUND)

    # Title
    title = title_font.render("CONNECT 4", True, WHITE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 60))

    mouse_pos = pygame.mouse.get_pos()

    # Draw buttons
    for text, button in buttons.items():

        rect = button["rect"]
        color = button["color"]

        # Hover effect
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER, rect.inflate(10, 10), border_radius=20)

        pygame.draw.rect(screen, color, rect, border_radius=18)

        text_surface = button_font.render(text, True, WHITE)

        screen.blit(
            text_surface,
            (
                rect.centerx - text_surface.get_width() // 2,
                rect.centery - text_surface.get_height() // 2
            )
        )

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if buttons["PVP MODE"]["rect"].collidepoint(event.pos):
                subprocess.run([sys.executable, "PVP.py"])

            elif buttons["AI EASY"]["rect"].collidepoint(event.pos):
                subprocess.run([sys.executable, "AI.py", "0"])

            elif buttons["AI MEDIUM"]["rect"].collidepoint(event.pos):
                subprocess.run([sys.executable, "AI.py", "1"])

            elif buttons["AI HARD"]["rect"].collidepoint(event.pos):
                subprocess.run([sys.executable, "AI.py", "2"])

    clock.tick(60)