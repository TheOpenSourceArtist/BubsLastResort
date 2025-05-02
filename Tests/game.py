from OSA import *
from random import choice

class Button(GameObject):
    def __init__(self):
        super().__init__()
        self.states = {'initial'}

        return
    #end __init__
#end Button

class Red(GameState):
    def __init__(self):
        super().__init__()
        self.title = 'Red'
        self.tileTest: TileSet = TileSet("smileSet.bmp",[32,32])
        self.animationTest: Animation = Animation("smileSet.bmp",[32,32])
        self.animationTest.frameDelays = [500,50,50,500]
        
        return
    #end __init__

    def render(self, surface):
        surface.fill((255,0,0))
        surface.blit(self.tileTest.tiles[0],(0,0))
        surface.blit(self.tileTest.tiles[1],(32,0))
        surface.blit(self.tileTest.tiles[2],(0,32))
        surface.blit(self.tileTest.tiles[3],(32,32))
        self.animationTest.render(surface,(0,100))
        
        return
    #end render

    def update(self) -> None:
        self.animationTest.update()
        
        return
    #end update

    def enter(self):
        super().enter()
        pg.display.set_caption(self.title)
        
        return
    #end enter
#end Green

class Green(GameState):
    def __init__(self):
        super().__init__()
        self.title = 'Green'
        
        return
    #end __init__

    def render(self, surface):
        surface.fill((0,255,0))
        
        return
    #end render

    def enter(self):
        super().enter()
        pg.display.set_caption(self.title)
        
        return
    #end enter
#end Green

class Blue(GameState):
    def __init__(self):
        super().__init__()
        self.title = 'Blue'
        
        return
    #end __init__

    def render(self, surface):
        surface.fill((0,0,255))
        
        return
    #end render

    def enter(self):
        super().enter()
        pg.display.set_caption(self.title)
        
        return
    #end enter
#end Green

class TestGame(Game):
    def __init__(self):
        super().__init__('Test Game')
        self.gameStates = {
            'red': Red()
            ,'green': Green()
            ,'blue': Blue()
        }
        self.activeState = self.gameStates['red']
        self.activeState.enter()
        self.curStateTick = 0
        self.lastStateTick = 0
        self.stateDelay = 1000
        
        return
    #end __init__

    def update(self):
        super().update()
        
##        self.curStateTick = pg.time.get_ticks()
##
##        if self.curStateTick - self.lastStateTick >= self.stateDelay:
##            self.activeState.exit()
##            self.activeState = self.gameStates[choice(['red','green','blue'])]
##            self.activeState.enter()
##            self.lastStateTick = self.curStateTick
##        #end if

        return
    #end update
#end TestGame

def main() -> None:
    game: TestGame = TestGame()
    game.run()

    return
#end main

if __name__ == '__main__':
    main()
#end if
