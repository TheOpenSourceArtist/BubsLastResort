import OSA

def main() -> None:
    #create a new game
    game: Game = OSA.Game("Thomas Sandbox",[1200,900],[800,600])
    game.gameStates[''].bgColor = [22,4,75]
    
    #initialize game objects
    sprtThomas: Sprite = OSA.Sprite("gfx/gfxThomasStanding.bmp",[50,100])
    game.gameStates[''].gameObjects.append(sprtThomas)
    
    #run the game
    game.run()
    
    return None
#end main

if __name__ == '__main__':
    main()
#end if