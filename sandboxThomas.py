from OSA import *

class Thomas(Sprite):
    def __init__(self):
        super().__init__("gfx/gfxThomasStanding.bmp",[100,200])
        self.bounds = None
        self.ddy = 2
        self.dy = 0
        
        return
    #end __init__
    
    def update(self):
        self.dy += self.ddy
        self.rect.y += self.dy
        
        return
    #end update
#end Thomas
    
class Sandbox(GameState):
    def __init__(self):
        super().__init__("Sandbox")
        self.bgColor = [50,125,250]
        self.gameObjects.append(Sprite('gfx/bgTest.bmp',[800,600]))
        self.gameObjects.append(Thomas())
        
        return
    #end __init
    
    def handleBounds(self,bounds):
        for obj in self.gameObjects:
            if obj.rect.bottom >= bounds[1]:
                obj.rect.bottom = bounds[1]
        
        return
    #end handleBounds
#end Sandbox

def main() -> None:
    #create a new game
    game: Game = Game("Thomas Sandbox",[800,600],[800,600])
    
    #initialize game objects
    game.gameStates['Sandbox'] = Sandbox()
    game.activeState = game.gameStates['Sandbox']
    
    #run the game
    game.run()
    
    return None
#end main

if __name__ == '__main__':
    main()
#end if
