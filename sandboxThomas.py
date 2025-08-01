from OSA import *

class Thomas(Animation):
    def __init__(self):
        super().__init__('gfx/animThomasWalk.bmp',[100,200])
        self.acceleration: pg.math.Vector2 = pg.math.Vector2(0,3)
        self.velocity: pg.math.Vector2 = pg.math.Vector2(0,0)
        self.jumpReady: bool = True
        self.jumpAcceleration: float = self.acceleration.y * 4
        self.moveSpeed: float = 5
        self.flipped: bool = False
        self.lastVel: pg.math.Vector2 = pg.math.Vector2(0,0)
        self.jumpMaxHeight: int = 60
        self.jumpStartHeight: int = 0
        self.frameDelays = [100 for x in self.frameDelays]
        
        
        return
    #end __init__
    
    def update(self) -> None:
        self.lastVel = self.velocity
        self.velocity += self.acceleration
        super().update()
        
        return
    #end update
    
    def render(self, renderBuffer: pg.surface.Surface) -> None:
        temp:pg.surface.Surface = pg.transform.flip(self.tiles[self.currentFrame],self.flipped,False)
        temp.set_colorkey(COLOR_TRANSPARENT)
        renderBuffer.blit(temp,self.rect)
        
        return
    #end render
#end Thomas
    
class Sandbox(GameState):
    def __init__(self, game: Game) -> None:
        super().__init__('Sandbox')
        self.renderSize: list[int] = game.renderSize
        self.displaySize: lit[int] = game.displaySize
        self.renderScale: list[float] = game.renderScale
        self.thomas: Thomas = Thomas()
        self.bgColor: list[int] = [120,210,220]
        self.bg = Sprite("gfx/testBG.bmp",[800,600])
        
        game.gameStates['sandbox'] = self
        game.activeState = game.gameStates['sandbox']
        self.enter()
        
        return
    #end __init
    
    def handleKeyboard(self, keyboard: list[bool]) -> None:
        if keyboard[pg.K_SPACE]:
            if self.thomas.velocity.y == 0 and self.thomas.lastVel.y == 0 and self.thomas.jumpReady:
                self.thomas.jumpStartHeight = self.thomas.rect.bottom
            
            if (self.thomas.jumpStartHeight - self.thomas.rect.bottom) < self.thomas.jumpMaxHeight:
                if self.thomas.jumpReady:
                    self.thomas.velocity.y += -self.thomas.jumpAcceleration
            else:
                self.thomas.jumpReady = False
        else:
            self.thomas.jumpReady = False
            
            if self.thomas.velocity.y == 0 and self.thomas.lastVel.y == 0:
                self.thomas.jumpReady = True
                self.thomas.velocity.y = 0
                
            
        if keyboard[pg.K_RIGHT]:
            self.thomas.velocity.x = self.thomas.moveSpeed
            self.thomas.flipped = False
        elif keyboard[pg.K_LEFT]:
            self.thomas.velocity.x = -self.thomas.moveSpeed
            self.thomas.flipped = True
        else:
            self.thomas.velocity.x = 0
        #end if
        
        return
    #end handleKeyboard
    
    def update(self) -> None:
        self.thomas.update()
        
        if self.thomas.rect.bottom >= self.renderSize[1] - 150:
            self.thomas.velocity.y = 0
            self.thomas.rect.bottom = self.renderSize[1] - 150
        #end if
        
        return
    #end update
    
    def render(self, renderBuffer) -> None:
        renderBuffer.fill(self.bgColor)
        self.bg.render(renderBuffer)
        self.thomas.render(renderBuffer)
        
        return
    #end render
#end Sandbox

def main() -> None:
    #create a new game
    game: Game = Game("Thomas Sandbox",[800,600],[800,600])
    
    #initialize game objects
    sandbox: Sandbox = Sandbox(game)
    
    #run the game
    game.run()
    
    return None
#end main

if __name__ == '__main__':
    main()
#end if
