from controller import Controller
from models.data_base import DB
from view import View
from models.player import Player
from models.tournament import Tournament
from models.match import Match


def main():
    my_view = View()
    my_data_base = DB()
    my_player = Player()
    my_tournament = Tournament()
    my_match = Match()
    game = Controller(my_view, my_data_base, my_player, my_tournament, my_match)
    my_view.set_controller(game)
    game.run()
# test

if __name__ == '__main__':
    main()