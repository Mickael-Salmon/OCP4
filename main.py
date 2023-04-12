from chessApp.controllers.menu_controller import MenuController
from chessApp.views.menu_view import MenuViews


def main():
    MenuViews.app_title()
    MenuController().main_menu_start()


if __name__ == "__main__":
    main()
