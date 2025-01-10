import pygame, random, sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Thu th■p bao lì xì")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60

class Object:
    def __init__(self, x, y, width, height, speed, objtype, imagepath):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.objtype = objtype
        self.image = pygame.image.load(imagepath)
        self.image = pygame.transform.scale(self.imagepath,(self.width, self.height))

    def draw(self, surface):
        surface.blit(self.image, (self.width, self.height))

    def move(self):
        self.y += self.speed

objects = []
lives = 3

def main():
    global score, lives
    running = True

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if random.randint(1, 60) == 1:
            objects.append(Object(random.randint(0, SCREEN_WIDTH - 40), -40, 40, 40, 5, "bonus", "baolixi.png"))
        for obj in objects[:]:
            obj.move()
            obj.draw(screen)
            if obj.y > SCREEN_HEIGHT:
                objects.remove(obj)

            if check_collision(player, obj):
                if obj.type == "bonus":
                    score += 10
                else:
                    lives -= 1
                objects.remove(obj)

        if lives <= 0:
            print("Game Over!")
            running = False
        
        keys = pygame.key.get_pressed()

        player.move(keys)
        player.draw(screen)

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()