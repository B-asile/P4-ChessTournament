from controller import Controller
from model import Model
from view import View


def main():
    my_view = View()
    my_model = Model()
    game = Controller(my_view, my_model)
    my_view.setController(game)
    game.run()


if __name__ == '__main__':
    main()


# Nettoyer les fonctions du view qui ne sont pas utilisées dans le controller
# et revoir la nommenclature des fonction Display & Input
# et séparer les display en premier les input en second pour préparer la division du module View
# Test général de toutes les fonctionnalitées