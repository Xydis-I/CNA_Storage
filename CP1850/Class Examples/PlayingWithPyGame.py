# -*- coding: utf-8 -*-
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Monkey Fever")
pygame.mouse.set_visible(False)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill((170, 238, 187))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    
    # if pygame.font:
    #     font = pygame.font.Font(None, 64)
    #     text = font.render("Jump To Here", True, (10,10,10))
    #     textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    #     background.blit(text, textpos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    
    

pygame.quit()