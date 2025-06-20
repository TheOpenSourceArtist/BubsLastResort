from OSA import *

class TestState(GameState):
    def __init__(self):
        super().__init__()
        #self.testSprite = Sprite('gfx/gfxSpriteNinjaCornRat.bmp', [80,63])
        self.testSprite = Animation('gfx/animThomasWalk.bmp', [100,200])
        self.testSprite.frameDelays = [50 for x in self.testSprite.frameDelays]
        self.testSprite.velocity = pg.math.Vector2.from_polar((3,0))
        self.anim = Animation('gfx/animSpriteNinjaCornRat.bmp',[80,63])
        self.animCheetah = Animation('gfx/animCheetahRangerWalk.bmp',[50,100])
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

    def handleInputs(self,keyboard,mousebutton,mousepos):
        if(keyboard[pg.K_SPACE]):
            self.testSprite.frameDelays = [20 for x in self.testSprite.frameDelays]
        else:
            self.testSprite.frameDelays = [200 for x in self.testSprite.frameDelays]
        return
    #end

game = Game()
game.gameStates['Test'] = TestState()
game.activeState = game.gameStates['Test']
game.run()

   



  




        
