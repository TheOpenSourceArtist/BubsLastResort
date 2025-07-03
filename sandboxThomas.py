from OSA import *

class Thomas(Animation):
    def __init__(self):
        super().__init__('gfx/animThomasWalk.bmp',[100,200])
        self.acceleration: pg.math.Vector2 = pg.math.Vector2(0,1)
        self.velocity: pg.math.Vector2 = pg.math.Vector2(0,0)
        self.jumpReady: bool = True
        self.jumpAcceleration: float = 5
        self.maxJumpSpeed: float = 20
        self.moveSpeed: float = 4
        
        return
    #end __init__
    
    def update(self) -> None:
        super().update()
        
        self.velocity += self.acceleration
        self.rect.center += self.velocity
        
        return
    #end update
#end Thomas
    
class Sandbox(GameState):
    def __init__(self, game: Game) -> None:
        super().__init__('Sandbox')
        self.renderSize: list[int] = game.renderSize
        self.displaySize: lit[int] = game.displaySize
        self.renderScale: list[float] = game.renderScale
        self.thomas: Thomas = Thomas()
        self.bgColor: list[int] = [120,210,220]
        
        game.gameStates['sandbox'] = self
        game.activeState = game.gameStates['sandbox']
        self.enter()
        
        return
    #end __init
    
    def handleKeyboard(self, keyboard: list[bool]) -> None:
        if keyboard[pg.K_SPACE] and self.thomas.jumpReady:
            self.thomas.velocity.y += -self.thomas.jumpAcceleration
            
            if self.thomas.velocity.y <= -self.thomas.maxJumpSpeed:
                self.thomas.jumpReady = False
            #end if
        #end if
                
        if keyboard[pg.K_RIGHT]:
            self.thomas.velocity.x = self.thomas.moveSpeed
        elif keyboard[pg.K_LEFT]:
            self.thomas.velocity.x = -self.thomas.moveSpeed
        else:
            self.thomas.velocity.x = 0
        #end if
        
        return
    #end handleKeyboard
    
    def update(self) -> None:
        self.thomas.update()
        
        if self.thomas.rect.bottom >= self.renderSize[1]:
            self.thomas.velocity.y = 0
            self.thomas.rect.bottom = self.renderSize[1]
            self.thomas.jumpReady = True
        #end if
        
        return
    #end update
    
    def render(self, renderBuffer) -> None:
        renderBuffer.fill(self.bgColor)
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
