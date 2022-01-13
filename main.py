from controller import Controller
from data_base import DB
from view import View
from player import Player
from tournament import Tournament
from match import Match


def main():
    my_view = View()
    my_data_base = DB()
    my_player = Player()
    my_tournament = Tournament()
    my_match = Match()
    game = Controller(my_view, my_data_base, my_player, my_tournament, my_match)
    my_view.set_controller(game)
    game.run()


if __name__ == '__main__':
    main()