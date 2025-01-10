import pygame 
import sys 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Thu th■p bao lì xì")

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60

class Game:
    def __init__(self):
        self.player = Player(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 60, 50, 50, 10, "player.png")
        self.objects = []
        self.object_width = 40
        self.object_height = 40
        self.object_speed = 5
        self.score = 0
        self.lives = 3
        self.catch_sound = pygame.mixer.Sound("catch.mp3")
        self.hit_sound = pygame.mixer.Sound("hit.mp3")

    def draw_text(self, surface, text, x, y, color=(0,0,0)):
        text_obj = font.render(text, True, color)
        surface.blit(text_obj, (x, y))

    def add_object(self):
        x = random.randint(0, SCREEN_WIDTH - self.object_width)
        is_bonus = random.choice([True, False])
        obj_type = "bonus" if is_bonus else "obstacle"
        image_path = "baolixi.png" if obj_type == "bonus" else "bom.png"
        self.objects.append(Object(x, -self.object_height, self.object_width, self.object_height, self.object_speed, obj_type, image_path))

    def check_collision(self, obj):
        if self.player.x < obj.x + obj.width and self.player.x + self.player.width > obj.x and self.player.y < obj.y + obj.height and self.player.y + self.player.height > obj.y:
            return True
        return False

    def update_objects(self):
        for obj in self.objects[:]:
            obj.move()
            if self.check_collision(obj):
                if obj.type == "bonus":
                    self.score += 10
                    self.catch_sound.play()
                else:
                    self.lives -= 1
                    self.hit_sound.play()
                self.objects.remove(obj)
            elif obj.y > SCREEN_HEIGHT:
                self.objects.remove(obj)

    def run(self):
        running = True
        while running:
            screen.fill((255, 255, 224))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            if random.randint(1, 60) == 1:
                self.add_object()

            self.update_objects()

            self.player.draw(screen)
            for obj in self.objects:
                obj.draw(screen)

            self.draw_text(screen, f"Score: {self.score}", 10, 10)
            self.draw_text(screen, f"Lives: {self.lives}", 10, 50)

            if self.lives <= 0:
                self.draw_text(screen, "Game Over!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, RED)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()