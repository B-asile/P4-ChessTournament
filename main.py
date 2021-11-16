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


# Gestion des matchs deja fait .....
# verifier si dans la reprise des matchs ils ajoute bien que ceux du bon tournois
# modifier la création des listes 1 et 2 dans le 2eme choix de créations de match