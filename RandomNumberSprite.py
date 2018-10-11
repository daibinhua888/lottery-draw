import pygame

font_200=pygame.font.Font(None,200)
white_color=118,238,0

class RandomNumberSprite(pygame.sprite.Sprite):
    def __init__(self,target,position):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.number=0
        self.status='UNKNOW'
        self.position=position
        self.rect = pygame.Rect(position[0], position[1], 80, 168)

    def begin(self):
        self.status='ROLLING'

    def isDone(self):
        if self.status == 'DONE':
            return True
        return False

    def isInitialized(self):
        if self.status == 'UNKNOW':
            return False
        return True

    def switchTo(self, number):
        self.number=number

    def draw(self):
        random_str = str(self.number)
        random_text = font_200.render(random_str, True, white_color)
        self.target_surface.blit(random_text, self.position)

    def isMousePositionHit(self, pos):
        print(pos)
        return self.rect.collidepoint(pos)

    def stop(self):
        self.status='DONE'