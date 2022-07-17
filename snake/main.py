
from . import graphics
from . import theme
from . import gameloop
from . import game
from . import parser
from . import stage


def exit():
    graphics.exit()


def run():
    try:
        parser.init()
        stage.init()
        graphics.init()
        theme.init()
        game.reset()
        gameloop.start()

    except KeyboardInterrupt:
        exit()

run()
