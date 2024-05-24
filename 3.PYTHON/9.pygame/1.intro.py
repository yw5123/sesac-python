import pygame

# pygame setup
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

game_over = False

while not game_over:

    # 이벤트 (창의 모든 이벤트를 핸들링하다가 QUIT가 되면 game_over 변수의 값을 바꿈)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 화면(display), screen (화면에 그릴 정보를 갖고 있는 변수)
    screen.fill('blue')

    pygame.draw.circle(screen, "white", player_pos, 40)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player_pos.y -= 10
    if key[pygame.K_DOWN]:
        player_pos.y += 10

    pygame.display.flip()

    clock.tick(60)  # FPS 60 fps