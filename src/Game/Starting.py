from src.Game import GameInfo
from src.Game.Window import Window
from src.Game.Managers import EventManager, AnimationManager, ObjManager, SoundManager
from src.Game.UI.Button import Button


GameInfo.GameInfo()
Window.Window()
EventManager.EventManager()
AnimationManager.AnimationManager()
ObjManager.GameObjectManager()
SoundManager.SoundManager()

def CreateMainMenu():
    from src.Game.MainMenu import MainMenu
    mainmenu = MainMenu.Init()
    mainmenu.start()
    return mainmenu.mode

def CreateEpisode0():
    from src.Game.Episodes.Episode0 import Episode0
    episode0 = Episode0.Init()
    mode = episode0.start()
    return mode

# CreateEpisode0()

mode = CreateMainMenu()
buttonid = Button.ButtonId

GameInfo.GameInfo().reset_all()

while True:
    if mode == buttonid.EPISODE_1:
        print(f'start: {buttonid.EPISODE_1}')
        mode = CreateEpisode0()

    elif mode == buttonid.EPISODE_2:
        print(f'start: {buttonid.EPISODE_2}')
        mode = CreateEpisode0()

    elif mode == buttonid.EPISODE_3:
        print(f'start: {buttonid.EPISODE_3}')
        mode = CreateEpisode0()

    elif mode == buttonid.EXIT_BUTTON or mode == buttonid.PLAY_QUIT_MENU:
        print('EXIT_BUTTON')
        mode = CreateMainMenu()

    print(f'mode: {mode}')
