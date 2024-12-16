import pygame

screen_x = 640
screen_y = 480
screen = pygame.display.set_mode((screen_x, screen_y))

#screen.fill(pygame.Color(0, 225, 0))


# pygame setup
pygame.init()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
Scale_player = pygame.Rect(player_pos.x,player_pos.y,50,50)
Scale_fruit = pygame.Rect(100,100,50,50)
Scale_fruit2 = pygame.Rect(500,400,50,50)
fruit_color = "orange"
clock = pygame.time.Clock()
running = True
dt = 0
is_first_collide = False
is_first_collide2 = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("red")




    player = pygame.draw.rect(screen, "green", Scale_player)
    
    collide = Scale_player.colliderect(Scale_fruit)
    # "not is_first_ player" равнозначно "is_first_player == True"
    if not collide and  not is_first_collide:
        fruit = pygame.draw.rect(screen, fruit_color, Scale_fruit)
    else:
        is_first_collide = True

    print("Значение collide ",collide)
    print("значение is_first_collde " ,is_first_collide)


    collide2 = Scale_player.colliderect(Scale_fruit2)
    # "not is_first_ player" равнозначно "is_first_player == True"
    if not collide2 and  not is_first_collide:
        fruit = pygame.draw.rect(screen, (143, 0, 252, 255), Scale_fruit2)
    else:
        is_first_collide2 = True

    



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if Scale_player.y < 50:
            Scale_player.y = 50
        Scale_player.y -= 500 * dt
    if keys[pygame.K_s] :
        if Scale_player.y > screen_y -100:
            Scale_player.y = screen_y -100
        Scale_player.y += 500 * dt
    if keys[pygame.K_a] :
        if Scale_player.x < 50:
            Scale_player.x = 50
        Scale_player.x -= 500 * dt
    if keys[pygame.K_d] :
        if Scale_player.x > screen_x -100:
            Scale_player.x = screen_x -100
        Scale_player.x += 500 * dt

    fruit_color = "red" if collide else "orange"

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(10) / 1000

pygame.quit()

#основной цикл
running = True
while running:
    #создаём событие запуска
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

#если цикл завершиться то игра остановиться
pygame.quit()