#whole game is a function that it can be implemented easily into the main frame of the game

def bounce():
    #game is in a try frame because it gets quited after 20 points.
    try:
        # Sprite Classes for platform game
        import random
        #Title
        TITLE = 'Jumpy'

        #Dimensions
        WIDTH = 800
        HEIGHT = 600
        FPS = 100

        #Colors
        #Primary Colors
        RED = (255,0,0)
        GREEN = (25,255,0)
        BLUE = (0,0,255)

        #Secondary Colors
        lime = (0,255,0)
        forest_green = (34,139,34)

        #Other Colors
        WHITE = (255,255,255)
        BLACK = (0,0,0)

        RAND_COLOR_ARRAY = [GREEN,lime,forest_green]

        #Creates the start plattform
        PLATFORM_WIDTH = 75
        PLATFORM_HEIGHT = 20
        PLATFORM_LIST = [(0,HEIGHT-40,WIDTH,40,random.choice(RAND_COLOR_ARRAY)),
                        (WIDTH/2-50, HEIGHT * 3/4, PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY)),
                        (400,200, PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY)),
                        (PLATFORM_HEIGHT,300,PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY)),
                        (600,50,PLATFORM_WIDTH,PLATFORM_HEIGHT,random.choice(RAND_COLOR_ARRAY))]

        # Makes the properties of the player
        PLAYER_ACC = 0.5
        PLAYER_FRICTION = -0.12
        PLAYER_GRAV = 0.5
        #import of pygame, is important for the game to work
        import pygame as pg

        vec = pg.math.Vector2

        #creates the playe and defines his colour, width and height
        class Player(pg.sprite.Sprite):
            def __init__(self, game):
                self.game = game
                pg.sprite.Sprite.__init__(self)
                self.image = pg.Surface((30, 40))
                self.image.fill(WHITE)


                self.rect = self.image.get_rect()
                self.rect.center = (WIDTH / 3, HEIGHT / 4)

                self.pos = vec(WIDTH / 2, HEIGHT / 2)
                self.vel = vec(0, 0)
                self.acc = vec(0, 0)

            def update(self):
                self.acc = vec(0, PLAYER_GRAV)
                keys = pg.key.get_pressed()
                #moves player from left to right
                if keys[pg.K_a]:
                    self.acc.x = -PLAYER_ACC
                if keys[pg.K_d]:
                    self.acc.x = PLAYER_ACC

                # Gives the player friction
                self.acc.x += self.vel.x * PLAYER_FRICTION

                # Equations of motion
                self.vel += self.acc
                self.pos += self.vel + 2 * self.acc

                # Wrap around the sides of the screen
                if self.pos.x > WIDTH:
                    self.pos.x = 0

                if self.pos.x < 0:
                    self.pos.x = WIDTH

                # The rectangles new position
                self.rect.midbottom = self.pos

            #makes the player jump
            def jump(self):
                self.rect.x += 4
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if hits:
                    self.vel.y = -19.5


        class Platform(pg.sprite.Sprite):
            def __init__(self, x, y, w, h, color):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.Surface((w, h))
                self.image.fill(color)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

        #imports random module for allocation of platfroms
        import random




        class Game:
            def __init__(self):
                #starts the game and creates a screen
                self.running = True
                self.gameOver = False
                pg.init()
                pg.mixer.init()
                self.screen = pg.display.set_mode((WIDTH, HEIGHT))
                pg.display.set_caption(TITLE)
                self.clock = pg.time.Clock()

            def new(self):
                # Start a New Game

                # Groups
                self.all_sprites = pg.sprite.Group()
                self.platforms = pg.sprite.Group()

                # Player object
                self.player = Player(self)
                self.all_sprites.add(self.player)
                self.PLAYER_SCORE = 0

                # Platform Object
                for plat in PLATFORM_LIST:
                    p = Platform(*plat)
                    self.platforms.add(p)
                    self.all_sprites.add(p)

            def run(self):
                #this is the game loop
                self.playing = True
                while self.playing:
                    self.clock.tick(FPS)
                    self.events()
                    self.update()
                    self.draw()
                    if self.gameOver:
                        print(self.PLAYER_SCORE)

                        #start here


            def update(self):
                # Game Loop - Update
                self.all_sprites.update()
                # This checks if player hits a platform
                if self.player.vel.y > 0:
                    hits = pg.sprite.spritecollide(self.player, self.platforms, False)
                    if hits:
                        self.player.pos.y = hits[0].rect.top + 1
                        self.player.vel.y = 0

                # If player reaches the top quarter of the screen the window scrolls up
                if self.player.rect.top < HEIGHT / 4:
                    self.player.pos.y += abs(self.player.vel.y)
                    for plat in self.platforms:
                        plat.rect.y += abs(self.player.vel.y)
                        if plat.rect.top > HEIGHT:
                            self.PLAYER_SCORE += 1
                            print(self.PLAYER_SCORE)
                            # Quites game after 20 points to go to next level in main frame code
                            x = self.PLAYER_SCORE
                            player = [x]
                            if x == 20:

                                pg.quit()







                            plat.kill()

                # Spawns new platforms

                while len(self.platforms) < 6:
                    p = Platform(random.randint(10, 700), -(random.randint(20, 100)), PLATFORM_WIDTH, PLATFORM_HEIGHT,
                                 random.choice(RAND_COLOR_ARRAY))
                    self.platforms.add(p)
                    self.all_sprites.add(p)

                if self.player.rect.top > HEIGHT:
                    self.playing = False

            def events(self):
                # Game Loop - Events
                for event in pg.event.get():
                    # Check for closing window
                    if event.type == pg.QUIT:
                        pg.quit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            self.player.jump()

            def draw(self):
                # Game Loop - draw
                # Drawing

                self.screen.fill(BLACK)
                self.all_sprites.draw(self.screen)
                #displays the game score
                self.display_text(("Points:" + str(self.PLAYER_SCORE)), 0, 0, 40, WHITE)

                # After everything has been drawn, flip the display
                pg.display.flip()

            def show_go_screen(self):

                gameOverLoop = False

                while not gameOverLoop:
                    #creates the start screen of the game
                    self.screen.fill(BLACK)
                    self.display_text('Enjoy the next jumps ', WIDTH / 3.3 + 30, HEIGHT / 4, 30, WHITE)
                    self.display_text("A and D to move left and right and SPACE to Jump", WIDTH / 3 - 20, HEIGHT / 3, 15, WHITE)
                    self.display_text("Press any button to continue...", WIDTH / 3 + 50, HEIGHT * 2 / 3, 15, WHITE)
                    pg.display.flip()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()

                        if event.type == pg.KEYUP:
                            self.gameOver = False
                            gameOverLoop = True

            #defines hoe the text should be
            def display_text(self, message, x, y, size, color):
                font = pg.font.SysFont("Arial", size)
                text = font.render(message, False, color)
                self.screen.blit(text, (x, y))


        g = Game()

        g.show_go_screen()

        while g.running:
            g.new()
            g.run()
            g.show_go_screen()
    #out put after game gets quited, that the whole game can continue.
    except:
        x = 10
#this starts the game.
bounce()
