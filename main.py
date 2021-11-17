from Controller import Controller
from Model import Model
from View import View


def main():
    my_view = View()
    my_model = Model()
    game = Controller(my_view, my_model)
    my_view.setController(game)
    game.run()


if __name__ == '__main__':
    main()

# finir de reprendre le model MVC
# certains codes dans le model a passer dans la view