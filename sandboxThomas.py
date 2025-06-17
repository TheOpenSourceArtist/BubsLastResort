from OSA import *

class Thomas(Sprite):
    def __init__(self):
        super().__init__("gfx/gfxThomasStanding.bmp",[50,100])
        self.image = pg.transform.scale(self.image,[125,250])
        
        return
    #end __inint__
#end Thomas

def main() -> None:
    #create a new game
    game: Game = Game("Thomas Sandbox",[800,600],[800,600])
    game.gameStates[''].bgColor = [50,125,250]
    
    #initialize game objects
    sprtThomas: Sprite = Thomas()
    game.gameStates[''].gameObjects.append(sprtThomas)
    
    #run the game
    game.run()
    
    return None
#end main

if __name__ == '__main__':
    main()
#end if
