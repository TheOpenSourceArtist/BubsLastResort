from OSA import *

#Sprite Class 
class Sprite (GameObject):
    def __init__(self, imgPath=None, spriteSize=[8,8]):
        super().__init__()

        self.rect = pg.Rect([0,0],spriteSize)
        self.velocity = pg.math.Vector2(0,0)
        self.orientation = float()

        if imgPath == None:
            self.masterImg = pg.surface.Surface(spriteSize)
            self.masterImg.fill([255,0,0])

        else:
            self.masterImg = pg.image.load(imgPath)

        self.image = pg.surface.Surface(spriteSize)
        self.image.blit(self.masterImg,(0,0))

        return

    def render (self, surface):
        surface.blit(self.image, self.rect)

        return

class TestState(GameState):
    def __init__(self):
        super().__init__()
        self.testSprite = Sprite(None, [30,20])

        return

    def render(self, surface):
        self.testSprite.render(surface)

        return

game = Game()
game.gameStates['Test'] = TestState()
game.activeState = game.gameStates['Test']
game.run()

   



  




        
