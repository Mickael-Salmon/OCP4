from chessApp.controllers.reports_controller import ReportsController
from chessApp.controllers.tournament_controller import TournamentController
from chessApp.models.player_model import Player
from chessApp.models.tournament_model import Tournament
from chessApp.views.menu_view import MenuViews
from chessApp.controllers.user_Input_validation import UserInputValidation

prompt = "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜.\n" \

class MenuController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.tour_cont = TournamentController()
        self.reports_cont = ReportsController()

    def main_menu_start(self):
        """Sélecteur de menu principal:
        Redirige vers le sous-menus respectif"""

        self.menu_view.main_menu()
        self.menu_view.input_prompt()
        prompt = "Veuillez entrer un numéro d'option : "
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "1":
            self.new_tournament_submenu()

        elif user_input == "2":
            self.new_player_submenu()

        elif user_input == "3":
            self.reports_menu()

        elif user_input == "Q" or user_input == "q":
            self.menu_view.are_you_sure_exit()
            user_input = UserInputValidation.get_validated_input(prompt)

            if user_input == "o":
                exit()
            elif user_input == "n":
                self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.main_menu_start()

    def new_tournament_submenu(self):
        """Affiche le nouveau sous-menu de tournoi"""

        self.menu_view.new_tournament_submenu()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "1":
            self.new_tournament()

        elif user_input == "2":
            # Call the method to handle the second option
            self.resume_tournament()

        # Other options...

        elif user_input == "r":
            self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.new_tournament_submenu()

    def new_player_submenu(self):
        """Affiche le nouveau sous-menu de joueur"""

        self.menu_view.new_player_submenu()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "1":
            self.new_player()

        elif user_input == "2":
            # Call the method to handle the second option
            self.update_player()

        # Other options...

        elif user_input == "r":
            self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.new_tournament_submenu()

    def new_tournament(self):
        """Créez un nouveau tournoi, sérialisez et enregistrez sur DB"""
        self.menu_view.create_tournament_header()
        tournament_info = []
        options = [
            "name",
            "location",
            "description"
        ]

        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = UserInputValidation.get_validated_input(prompt)

            if user_input == "r":
                self.main_menu_start()

            else:
                tournament_info.append(user_input)

        tournament_info.append(self.input_time_control())
        tour_players = self.select_players(8)

        self.menu_view.review_tournament(tournament_info, tour_players)
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "o":
            tournament = Tournament(
                t_id=0,
                name=tournament_info[0],
                location=tournament_info[1],
                start_date="Not started",
                end_date="TBD",
                description=tournament_info[2],
                time_control=tournament_info[3],
                players=tour_players,
                current_round=1,
                rounds=[]
            )
            tournament.save_tournament_db()
            self.menu_view.tournament_saved()

            self.menu_view.start_tournament_prompt()
            user_input = UserInputValidation.get_validated_input(prompt)

            if user_input == "o":
                self.tour_cont.start_tournament(tournament)
            elif user_input == "n":
                self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def input_time_control(self):
        """Sélectionnez le contrôle du temps pour le nouveau tournoi

        @return: contrôle du temps (str)
        """
        self.menu_view.time_control_options()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "1":
            return "Classique"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Rapide"
        elif user_input == "r":
            self.main_menu_start()
        else:
            self.menu_view.input_error()
            self.input_time_control()

    def select_players(self, players_total):
        """Sélectionnez des joueurs pour le nouveau tournoinouveau tournoinouveau tournoinouveau tournoinouveau tournoi

        @param players_total: nombre de joueurs (int)
        @return: Liste des joueurs sélectionnés
        """
        players = Player.load_player_db()
        id_list = []
        for i in range(len(players)):
            id_list.append(players[i]["id"])

        tour_players = []

        i = 0
        while i < players_total:
            self.menu_view.select_players(players, i+1)
            self.menu_view.input_prompt()
            user_input = input()

            if user_input == "r":
                self.main_menu_start()

            elif not user_input.isdigit():
                self.menu_view.input_error()

            elif int(user_input) in id_list:
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1

            else:
                self.menu_view.player_already_selected()

        return tour_players

    def resume_tournament(self):
        """Sélectionnez le tournoi existant pour reprendre"""
        tournament_list = Tournament.load_tournament_db()

        self.menu_view.select_tournament(tournament_list)
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "r":
            self.main_menu_start()

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["id"]):
                t = tournament_list[i]
                t = Tournament(
                    t["id"],
                    t["name"],
                    t["location"],
                    t["start_date"],
                    t["end_date"],
                    t["description"],
                    t["time_control"],
                    t["current_round"],
                    t["players"],
                    t["rounds"],
                    t["rounds_total"]
                )
                self.tour_cont.start_tournament(t)

    def new_player(self):
        """Créer un nouveau joueur, sérialiser et enregistrer sur DB"""
        self.menu_view.create_new_player_header()
        player_info = []
        options = [
            "Nom de famille",
            "Prénom",
            "Date de naissance (dd/mm/yyyy)",
            "Genre [M/F/O]",
            "rang"
        ]
        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()
            if user_input == "r":
                self.main_menu_start()
            else:
                player_info.append(user_input)

        MenuViews.review_player(player_info)
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "o":
            player = Player(
                p_id=0,
                last_name=player_info[0],
                first_name=player_info[1],
                birthday=player_info[2],
                gender=player_info[3],
                rank=int(player_info[4])
            )

            player.save_player_db()
            self.menu_view.player_saved()
            self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def update_player(self):
        """Mettre à jour les informations existantes des joueurs"""
        players = Player.load_player_db()

        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "r":
            self.main_menu_start()

        p = players[int(user_input) - 1]
        p = Player(
            p['id'],
            p['last_name'],
            p['first_name'],
            p['date_of_birth'],
            p['gender'],
            p['rank']
        )

        options = [
            "Nom",
            "Prénom",
            "Date de naissance",
            "Genre",
            "Rang"
        ]
        self.menu_view.update_player_info(p, options)
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "r":
            self.main_menu_start()

        elif int(user_input) <= len(options):
            updated_info = (options[int(user_input) - 1]).replace(" ", "_")
            self.menu_view.input_prompt_text(
                f"new {options[int(user_input) - 1]}")
            user_input = UserInputValidation.get_validated_input(prompt)

            if user_input == "r":
                self.main_menu_start()

            else:
                p.update_player_db(user_input, updated_info)
                self.menu_view.player_saved()

                self.update_player()

        else:
            self.menu_view.input_error()
            self.update_player()

    def reports_menu(self):
        """Rapports Sélecteur de menu"""
        self.menu_view.reports_menu()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "1":
            self.player_reports_sorting(Player.load_player_db())

        elif user_input == "2":
            self.player_reports_sorting(self.reports_cont.tournament_players())

        elif user_input == "3":
            self.reports_cont.all_tournaments()

        elif user_input == "4":
            self.reports_cont.tournament_rounds()

        elif user_input == "5":
            self.reports_cont.tournament_matches()

        elif user_input == "r":
            self.main_menu_start()

        else:
            self.menu_view.input_error()
            self.reports_menu()

        self.menu_view.other_report()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "o":
            self.reports_menu()

        elif user_input == "n":
            self.main_menu_start()

    def player_reports_sorting(self, players):
        """Sélectionnez l'option de tri (nom ou rang) pour les joueurs

        @param players: liste des joueurs
        """
        self.menu_view.reports_player_sorting()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "1":
            self.reports_cont.all_players_name(players)

        elif user_input == "2":
            self.reports_cont.all_players_rank(players)

        elif user_input == "r":
            self.main_menu_start()

    def new_menu(self):
        """Logique de contrôle du nouveau menu"""
        # Votre logique de contrôle du nouveau menu
        pass
