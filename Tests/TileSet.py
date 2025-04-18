"""
    TileSet.py
    

    Author: Thomas Richardson
    Date: 2025-04-18
    Version: 0.1.0
"""

#-------------------------------------------------------------------------------
#   Import Modules
#-------------------------------------------------------------------------------

from OSA import *

#-------------------------------------------------------------------------------
#   Class Definitions
#-------------------------------------------------------------------------------

class TileSet(GameObject):
    def __init__(self, tileSetImage, tileSize) -> None:
        #initialize as the parent class
        super().__init__()

        #load the tileSetImage
        self.tileSize: list[int] = tileSize
        self.master: Surface = pg.image.load(tileSetImage)
        self.numTiles: list[int] = [
            int((self.master.get_width() / self.tileSize[0]))
            ,int((self.master.get_height() / self.tileSize[1]))
        ]
        
        self.tiles: list[Surface] = [
            self.master.subsurface(
                pg.Rect(
                    self.tileSize[0] * (i % self.numTiles[0])
                    ,self.tileSize[1] * (i % self.numTiles[1])
                    ,self.tileSize[0]
                    ,self.tileSize[1]
                )
            )
            for i in range(self.numTiles[0] * self.numTiles[1])
        ]
        
        return
    #end __init__
#end TileSet

#-------------------------------------------------------------------------------
#   Function Definitions
#-------------------------------------------------------------------------------

def main() -> None:
    game: Game = Game('Test Game', displaySize = [800,600])
    game.run()

    return
#end main

#-------------------------------------------------------------------------------
#   Program Entry Point
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
#end if
