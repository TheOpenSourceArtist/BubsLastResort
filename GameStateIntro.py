from OSA import *
from random import choice

GAME_TITLE = "Bub's Last Resort"

class IntroState(GameState):
    def __init__(self):
        super().__init__()
        self.background: Surface = pg.image.load(
            "gfx/gfxBackgroundIntro.png"
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
        
        return
    #end enter

    def exit(self):
        self.active = False
        self.visible = False
        
        return
    #end enter
#end Red

class TestGame(Game):
    def __init__(self):
        super().__init__(GAME_TITLE)
        self.gameStates["Intro"] = IntroState()
        self.activeState = self.gameStates["Intro"]
        
        return
    #end __init__

    def update(self):
        super().update()

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
