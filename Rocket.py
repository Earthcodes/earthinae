import pygame
import random
import math


def meteorAttack():
    # initialize the pygame
    pygame.init()

    # set the size of the screen and creates it
    xsize = 1000
    ysize = 750
    screen = pygame.display.set_mode((xsize, ysize))

    # Title and Icon
    pygame.display.set_caption("Meteor-Attack")
    icon = pygame.image.load("space-invaders.png")
    pygame.display.set_icon(icon)

    # images from flaticon.com under space invaders


    # Creates the player (image, position and speed)
    playerImg = pygame.image.load("space-invaders.png")
    playerX = xsize / 2 - 30
    playerY = ysize + 180
    playerX_change = 0
    playerY_change = 0


    # meteor
    meteorImg =[]
    meteorX = []
    meteorY = []
    meteorX_change = []
    meteorY_change = []

    num_of_meteors = 6

    # creates each meteor (image, position and speed)
    for i in range(num_of_meteors):
        meteorImg.append(pygame.image.load("meteor.png"))
        meteorX.append(random.randint(0, 736))
        meteorY.append(random.randint(0, 100))
        meteorX_change.append(random.randint(-2, 2) / 10)
        meteorY_change.append(random.randint(6, 10) / 10)



    # Creating the bullet
    global bullet_state
    bulletImg = pygame.image.load("bullet.png")
    bulletX = 0
    bulletY = 480
    bulletY_change = -1
    bullet_state = "ready"

    # score
    score_value = 0
    font = pygame.font.Font("freesansbold.ttf", 50)

    # position of the text
    textX = 10
    textY = 10

    # displays the actual score
    def show_score(x, y):
        score = font.render("score: " + str(score_value), True, (0, 0, 0))
        screen.blit(score, (int(x), int(y)))

    # displays the player
    def player(x, y):
        screen.blit(playerImg, (int(x), int(y)))

    # displays the meteors
    def meteor(x, y, i):
        screen.blit(meteorImg[i], (int(x), int(y)))

    # displays the bullet when fired
    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (int(x + 16), int(y + 10)))

    # calculates if a bullet hits a meteor
    def isCollision(meteorX, meteorY, bulletX, bulletY):
        distance = math.sqrt(math.pow(meteorX - bulletX, 2) + math.pow(meteorY - bulletY, 2))
        if distance < 37 and bullet_state == "fire":
            return True
        else:
            return False


    # Game Loop
    running = True
    while running:
        # background colour
        screen.fill((30, 50, 60))

        # checks inputs
        for event in pygame.event.get():
            # this function enables the close button (red x on the top right corner)
            if event.type == pygame.QUIT:
                running = False
                # this function enables the close button (red x on the top right corner)

            # checks if a key is pressed down
            if event.type == pygame.KEYDOWN:
                # if a key (awsd) is pressed, moves the player accordingly
                if event.key == pygame.K_a:
                    playerX_change = -0.35
                if event.key == pygame.K_d:
                    playerX_change = 0.35
                if event.key == pygame.K_w:
                    playerY_change = -0.35
                if event.key == pygame.K_s:
                    playerY_change = 0.35
                # if the  space key is pressed fires the bullet
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)

            # if a key (awsd) is stopped being pressed, stops the player movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    playerX_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    playerY_change = 0
        playerX += playerX_change
        playerY += playerY_change

        # player field restriction, checks that the player is always on the screen
        if playerX < 0:
            playerX = 0
        elif playerX > xsize - 64:
            playerX = xsize - 64
        if playerY < 0:
            playerY = 0
        elif playerY > ysize - 64:
            playerY = ysize - 64

        # meteor movement
        for i in range(num_of_meteors):
            meteorX[i] += meteorX_change[i]
            meteorY[i] += meteorY_change[i]

            # checks if a meteor has been hit with a bullet
            collision = isCollision(meteorX[i], meteorY[i], bulletX, bulletY)
            if collision:
                bullet_state = "ready"
                bulletY = 480
                score_value += 1
                meteorX[i] = random.randint(0, 736)
                meteorY[i] = random.randint(10, 100)

            meteor(meteorX[i], meteorY[i], i)
        for i in range(num_of_meteors):
            if (meteorX[i] > xsize) or (meteorX[i] < 0) or (meteorY[i] > ysize) or (meteorY[i] < 0):
                meteorX[i] = random.randint(0, 736)
                meteorY[i] = random.randint(10, 100)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY += bulletY_change

        # checks if the player is hit
        if math.sqrt(math.pow(meteorX[i] - playerX, 2) + math.pow(meteorY[i] - playerY, 2)) <= 64:
            succes = False
            break
        # score you have to reach to win the game
        if score_value >= 15:
            succes = True
            break

        # displays the player and the score and updates the display
        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    if __name__ == "__main__":
        meteorAttack()
meteorAttack()