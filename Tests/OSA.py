"""
    OSA.py
    A game framework and state machine that utilizes the core functionality
    of Pygame. OSA provides a modular framework design that makes it easy
    to transition between game states and create sandbox envirnments for
    testing and running code.

    Author: Thomas Richardson
    Date: 2025-04-17
    Version: 0.1.0
"""

#-------------------------------------------------------------------------------
#   Import Modules
#-------------------------------------------------------------------------------

import pygame as pg

#-------------------------------------------------------------------------------
#   Class Definitions
#-------------------------------------------------------------------------------

class GameObject:
    def __init__(self) -> None:

        return
    #end __init__

    def render(self, surface) -> None:

        return
    #end render

    def update(self) -> None:

        return
    #end update
#end GameObject

class GameState:
    def __init__(self) -> None:

        return
    #end __init__

    def render(self, surface) -> None:

        return
    #end render

    def update(self) -> None:

        return
    #end update

    def handleInputs(self, keyboard, mouse, mousePos) -> None:

        return
    #end handleInputs

    def handleBounds(self, bounds) -> None:

        return
    #end handleBounds

    def mixAudio(self) -> None:
        
        return
    #end mixAudio

    def enter(self) -> None:

        return
    #end enter

    def exit(self) -> None:

        return
    #end exit
#end GameState

class Game:
    #byte string for the logo data
    icon = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff8x\r\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff8x\r\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\xc4\xc4\xc4\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00f\xc7\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self,title = '',displaySize=[800,600],gameStates=dict()):
        #initialize pygame
        pg.init()

        #set up game display
        self.title: str = title
        pg.display.set_caption(self.title)
        pg.display.set_icon(pg.image.frombytes(Game.icon,(32,32),"RGBA"))
        self.displaySize: list(int) = list(displaySize)
        self.display: Surface = pg.display.set_mode(self.displaySize)
        self.renderSize: list(int) = list(displaySize)
        self.renderScale: list(float) = [
            float(self.displaySize[i]) / float(self.renderSize[i])
            for i in range(2)
        ]
        self.renderBuffer: Surface = pg.surface.Surface(self.renderSize)

        #set up game sound

        #set up game inputs
        self.fps: int = 60
        self.clock: Clock = pg.time.Clock()
        self.keyboard: list(bool) = pg.key.get_pressed()
        self.mouseButton: list(bool) = pg.mouse.get_pressed()
        self.mousePos: list(int) = pg.mouse.get_pos()
        self.running: bool = True

        #set up game states
        self.gameStates: dict(GameState) = dict(gameStates)
        self.activeState: GameState = None

        return
    #end __init__

    def render(self) -> None:
        #clear the render buffer
        self.renderBuffer.fill((0,0,0))

        #run the render method on the active game state
        if isinstance(self.activeState,GameState):
            self.activeState.render(self.renderBuffer)
        #end if

        #blit the scaled render buffer to the display
        pg.transform.scale(
            self.renderBuffer, self.displaySize, self.display
        )

        #update the display
        pg.display.flip()

        return
    #end render

    def update(self) -> None:
        #run the update method on the active game state
        if isinstance(self.activeState,GameState):
            self.activeState.update()
        #end if

        return
    #end render

    def handleEvents(self) -> None:
        #poll events until the event queue is empty
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            #end if
        #end for
        
        return
    #end handleEvents

    def handleInputs(self) -> None:
        #update keyboard and mouse button states
        self.keyboard = pg.key.get_pressed()
        self.mousebutton = pg.mouse.get_pressed()

        #get the cursor position
        self.mousePos = pg.mouse.get_pos()
        self.mousePos = [
            int(self.mousePos[i] / self.renderScale[i])  for i in range(2)
        ]

        #call the handleInputs method on the active Game State
        if isinstance(self.activeState,GameState):
            self.activeState.handleInputs(
                self.keyboard,self.mouseButton,self.mousePos
            )
        #end if
        
        return
    #end handleEvents

    def handleBounds(self) -> None:
        #call the handleBounds method on the active Game State
        if isinstance(self.activeState, GameState):
            self.activeState.handleBounds(self.renderSize)
        #end if

        return
    #end handlBounds

    def mixAudio(self) -> None:
        #call the mixAudio method on the active Game State
        if isinstance(self.activeState, GameState):
            self.activeState.mixAudio()
        #end if
        
        return
    #end mixAudio

    def run(self) -> None:
        #begin the main game loop
        while self.running:
            self.handleEvents()
            self.handleInputs()
            self.update()
            self.handleBounds()
            self.mixAudio()
            self.render()
            self.clock.tick(self.fps)
        #end while

        self.quit()

        return
    #end run

    def quit(self) -> None:
        pg.quit()

        return
    #end quit
#end Game

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
