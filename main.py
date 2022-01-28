from controller import Controller
from model import Model
from view import View


def main():
    my_view = View()
    my_model = Model()
    game = Controller(my_view, my_model)
    my_view.set_controller(game)
    game.run()
# test

if __name__ == '__main__':
    main()