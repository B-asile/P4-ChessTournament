from model import Model
from Playercls import Playercls
from Tournamentcls import Tournamentcls
from DB import DB
from view import View
from controller import Controller


def main():
    my_view = View()
    my_model = Model()
    chess = Controller(my_view, my_model)
    my_view.setController(chess)
    chess.run()


if __name__ == '__main__':
    main()
