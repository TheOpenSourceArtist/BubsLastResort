from OSA import *
from random import choice

class IntroState(GameState):
    def __init__(self):
        super().__init__()
        self.background: Surface = pg.image.load(
            "gfx/gfxBackgroundIntro.bmp"
        )
        self.background.convert()
        self.curTick: int = 0
        self.lastTick: int = 0
        self.duration: int = 3000

        return
    #end __init__

    def render(self, surface):
        width: int = surface.get_width()
        height: int = surface.get_height()
        
        pg.transform.scale(self.background,(width,height),surface)
        
        return
    #end render

    def update(self) -> None:
        self.curTick = pg.time.get_ticks()

        if self.curTick - self.lastTick >= self.duration:
            self.exit()
        
        return
    #end update

    def enter(self):
        self.active = True
        self.visible = True
        
        return
    #end enter

    def exit(self):
        self.active = False
        self.visible = False
        
        return
    #end enter
#end IntroState

class TitleState(GameState):
    def __init__(self):
        super().__init__()

        return
    #end __init__

    def render(self, surface):
        surface.fill((0,128,255))
        
        return
    #end render

    def update(self) -> None:
        
        return
    #end update

    def enter(self):
        super().enter()
        
        return
    #end enter

    def exit(self):
        super().exit()
        
        return
    #end enter
#end TitleState

class BubsLastResort(Game):
    def __init__(self):
        super().__init__("Bub's Last Resort")
        self.gameStates["Intro"] = IntroState()
        self.gameStates["Title"] = TitleState()
        
        self.activeState = self.gameStates["Intro"]
        self.activeState.enter()
        
        return
    #end __init__

    def update(self)->None:
        super().update()

        if not self.activeState.active:
            self.activeState.exit()
            
            if self.activeState == self.gameStates['Intro']:
                self.activeState = self.gameStates['Title']
                self.activeState.enter()
            #end if
        #end if

        return
    #end update
#end TestGame

def main() -> None:
    game: Game = BubsLastResort()
    game.run()

    return
#end main

if __name__ == '__main__':
    main()
#end if
