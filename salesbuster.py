#To run this you need PyGame, it won't load without it.
#PyGame actually is a pain to install, Google instructions for your OS
#Installing it on Linux is easier than Windows, by the way.

#(c) 2016 under the MIT license.
#Be free, leave this in if you make changes:
#Originally found on github.com/o355/pythonstuff

import pygame, sys
from pygame.locals import *

def thegame():
    pygame.init()

    screen = pygame.display.set_mode((640, 460))
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Sales Buster - version 2.0.1')
    font = pygame.font.SysFont(None, 28)

    main_clock = pygame.time.Clock()

    score = 0
    lives = 25
    player = pygame.Rect(300, 400, 60, 10)
    player_speed = 10
    alive = True

    bubble = pygame.image.load("assets\sb_bubble.jpg").convert_alpha()
    paddle = pygame.image.load("assets\sb_paddle.jpg").convert_alpha()
    ball2 = pygame.image.load("gabe-newell.jpg").convert_alpha()

    move_left = False
    move_right = False

    def draw_screen():
        screen.fill((255, 255, 255))
    def draw_player():
        screen.blit(paddle, player)

    def draw_text(display_string, font, surface, x, y):
        text_display = font.render(display_string, 1, (0, 0, 0))
        text_rect = text_display.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_display, text_rect)

    x_position = 320
    y_position = 380
    last_x = x_position
    last_y = y_position
    ball = pygame.draw.circle(screen, (0, 0, 0), (x_position, y_position), 5, 0)
    screen.blit(ball2, (x_position, y_position))
    ball_can_move = False

    speed = [5,-5]


    #values for all bubbles to use
    all_bubbles = []
    number_of_bubbles = 9999999999999
    bubble_radius = 20
    bubble_edge = 1
    initial_bubble_position = 30
    bubble_spacing = 12

    def create_bubbles():
        bubble_x = initial_bubble_position
        bubble_y = initial_bubble_position

        for rows in range(0, 17):
            for columns in range(0, 39):
                bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble_x, bubble_y), bubble_radius, bubble_edge)


                bubble_x += bubble_spacing
                all_bubbles.append(bubble)
            bubble_y += bubble_spacing
            bubble_x = initial_bubble_position

    create_bubbles()

    def draw_bubbles():
        for bubble in all_bubbles:
            bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble.x, bubble.y), bubble_radius, bubble_edge)
            screen.blit(bubble, (bubble.x, bubble.y))

    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
                return 0
            #Keyboard input for players
            if event.type == KEYDOWN:
                if event.key == K_a:
                    move_right = False
                    move_left = True
                if event.key == K_d:
                    move_left = False
                    move_right = True
            if event.type == KEYUP:
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False
                if alive:
                    if event.key == K_SPACE:
                        ball_can_move = True
                if not alive:
                    if event.key == K_RETURN:
                        lives = 3
                        alive = True
                        score = 0
                        ball_can_move = False
                        for x in range(0, len(all_bubbles)):
                            all_bubbles.pop()
                        create_bubbles()

        #Ensure consistent frames per second
        main_clock.tick(50)

        #Move the player
        if move_left and player.left > 0:
            player.x -= player_speed
        if move_right and player.right < 640:
            player.x += player_speed

        #Move the ball
        if ball_can_move:
            last_x = x_position
            last_y = y_position

            x_position += speed[0]
            y_position += speed[1]
            if ball.x <= 0:
                x_position = 15
                speed[0] = -speed[0]
            elif ball.x >= 640:
                x_position = 625
                speed[0] = -speed[0]
            if ball.y <= 0:
                y_position = 15
                speed[1] = -speed[1]
            elif ball.y >= 460:
                lives -= 1
                score -= 667.68
                ball_can_move = False

            #Test collisions with the player
            if ball.colliderect(player):
                y_position -= 15
                speed[1] = -speed[1]

            #Move direction vector
            move_direction = ((x_position - last_x), (y_position - last_y))

            #Test collisions with the bubbles
            for bubble in all_bubbles:
                if ball.colliderect(bubble):
                    if move_direction[1] > 0:
                        speed[1] = -speed[1]
                        y_position -= 10
                    elif move_direction[1] < 0:
                        speed[1] = -speed[1]
                        y_position += 10
                    all_bubbles.remove(bubble)
                    score += 421.68
                    break

        else:
            x_position = player.x + 30
            y_position = 380

        if lives <= 0:
            alive = False

        draw_screen()
        draw_player()
        draw_bubbles()
        ball = pygame.draw.circle(screen, (0, 0, 0), (x_position, y_position), 6, 0)

        if alive:
            draw_text('Money saved: $%s' % (score), font, screen, 5, 5)
            draw_text('Sales left: %s' % (lives), font, screen, 510, 5)
        else:
            draw_text('Gabe laughs.', font, screen, 255, 5)
            draw_text('Press enter to save again.', font, screen, 180, 50)

        pygame.display.update()

thegame()