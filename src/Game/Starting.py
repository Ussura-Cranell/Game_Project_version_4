import pygame

from src.Game import GameInfo
from src.Game.Window import Window
from src.Game.Managers import EventManager, AnimationManager, ObjManager, SoundManager
from src.Game.UI.Button import Button

from src.Game.Sound import Sound

pygame.init()

gameinfo = GameInfo.GameInfo()
window = Window.Window()
eventmanager = EventManager.EventManager()
animationmanager = AnimationManager.AnimationManager()
objectmanager = ObjManager.GameObjectManager()
soundmanager = SoundManager.SoundManager()
soundstorage = Sound.SoundStorage()

def CreateMainMenu():
    from src.Game.MainMenu import MainMenu
    mainmenu = MainMenu.Init()
    mainmenu.start()
    return mainmenu.mode

def CreateEpisode0():
    from src.Game.Episodes.Episode0 import Episode0
    episode0 = Episode0.Init()
    episode0.start()
    return episode0.mode


mode = CreateMainMenu()
buttonid = Button.ButtonId

GameInfo.GameInfo().reset_all()

while True:
    if mode == buttonid.EPISODE_1:
        mode = CreateEpisode0()

    elif mode == buttonid.EPISODE_2:
        mode = CreateEpisode0()

    elif mode == buttonid.EPISODE_3:
        mode = CreateEpisode0()

    elif mode == buttonid.EXIT_BUTTON or mode == buttonid.PLAY_QUIT_MENU:
        mode = CreateMainMenu()

    # print(f'mode: {mode}')
