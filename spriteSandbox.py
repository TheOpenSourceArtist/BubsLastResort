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
        self.image.set_colorkey((255,0,255))

        return

    def render (self, surface):
        surface.blit(self.image, self.rect)

        return

    def update(self) -> None:
        self.rect.center += self.velocity

        return
    #end update

class TestState(GameState):
    def __init__(self):
        super().__init__()
        self.testSprite = Sprite('gfx/gfxSpriteNinjaCornRat.bmp', [80,63])
        self.testSprite.velocity = pg.math.Vector2.from_polar((3,0))
        self.anim = Animation('gfx/animSpriteNinjaCornRat.bmp',[80,63])
        self.animCheetah = Animation('gfx/animCheetahRanger.bmp',[58,100])
##        self.animCheetah.frameDelays[0] = 500
##        self.animCheetah.frameDelays[1] = 50

        return

    def render(self, surface):
        surface.fill((50,50,200))
        self.testSprite.render(surface)
        self.anim.render(surface,(100,100))
        self.animCheetah.render(surface,(300,300))

        return

    def update(self):
        self.testSprite.update()
        self.anim.update()
        self.animCheetah.update()
        
        return
    #end update

game = Game()
game.gameStates['Test'] = TestState()
game.activeState = game.gameStates['Test']
game.run()

   



  




        
