from OSA import *

class Platform:
    def __init__(self, size: list[int] = [100,25]) -> None:
        self.rect: pg.Rect = pg.Rect([0,0],size)
        self.velocity: pg.math.Vector2 = pg.math.Vector2(0,0)
        self.img: pg.surface.Surface = pg.surface.Surface(size)
        self.color: list[int] = [255,0,0]
        self.img.fill(self.color)

        return
    #end end

    def collide(self, other: Sprite) -> bool:

        return self.rect.colliderect(other.rect)
    #end collide

    def render(self, surface: pg.surface.Surface) -> None:
        surface.blit(self.img,self.rect)

        return
    #end render
    
    def update(self) -> None:
        self.rect.center += self.velocity
        
        return
    #end update
#end Platform

class Thomas(Entity):
    def __init__(self):
        super().__init__('gfx/animThomasWalk.bmp',[100,200])
        self.flipped: bool = False        
        
        return
    #end __init__
    
#     def update(self) -> None:
#         super().update()
#         
#         return
#     #end update
    
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
        self.platform: Platform = Platform([200,20])
        self.platform.rect.center = [x / 2 for x in self.renderSize]
        self.floor: Platform = Platform([game.renderSize[0],25])
        self.floor.rect.bottom = game.renderSize[1]
        self.floor.velocity.y = -5
        
        game.gameStates['sandbox'] = self
        game.activeState = game.gameStates['sandbox']
        self.enter()
        
        return
    #end __init
    
    def handleKeyboard(self, keyboard: list[bool]) -> None:          
        if keyboard[pg.K_RIGHT]:
            self.thomas.velocity.x = self.thomas.moveSpeed
            self.thomas.flipped = False
        elif keyboard[pg.K_LEFT]:
            self.thomas.velocity.x = -self.thomas.moveSpeed
            self.thomas.flipped = True
        else:
            self.thomas.velocity.x = 0
        #end if
            
        self.thomas.jump(keyboard[pg.K_SPACE])
        
        return
    #end handleKeyboard
    
    def update(self) -> None:
        self.floor.update()
        
        if self.floor.rect.top <= 0:
            self.floor.velocity.y *= -1
        elif self.floor.rect.bottom >= self.renderSize[1]:
            self.floor.velocity.y *= -1
            
        self.thomas.update()
        
        if self.floor.rect.colliderect(self.thomas.rect):
            self.thomas.rect.bottom = self.floor.rect.top
            if self.thomas.jumpState == JUMPSTATE_FREEFALL:
                self.thomas.jumpState = JUMPSTATE_GROUNDED
        elif self.platform.rect.colliderect(self.thomas.rect):
            self.thomas.rect.bottom = self.platform.rect.top
            if self.thomas.jumpState == JUMPSTATE_FREEFALL:
                self.thomas.jumpState = JUMPSTATE_GROUNDED
        else:
            if self.thomas.jumpState == JUMPSTATE_GROUNDED:
                self.thomas.jumpState = JUMPSTATE_FREEFALL
        #end if
        
        return
    #end update
    
    def render(self, renderBuffer) -> None:
        renderBuffer.fill(self.bgColor)
        self.bg.render(renderBuffer)
        self.floor.render(renderBuffer)
        self.thomas.render(renderBuffer)
        self.platform.render(renderBuffer)
        
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
