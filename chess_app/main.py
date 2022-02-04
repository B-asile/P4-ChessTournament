from chess_app.game_control import Controller
from chess_app.models.data_base import DB
from chess_app.view import View
from chess_app.models.player import Player
from chess_app.models.tournament import Tournament
from chess_app.models.match import Match


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

