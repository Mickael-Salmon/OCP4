from chessApp.models.tournament_model import Tournament
from chessApp.views.menu_view import MenuViews
from chessApp.views.reports_view import Reports


class ReportsController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.reports_view = Reports()

    def all_players_name(self, players):
        """Rapport des joueurs (trié par nom de famille)

        @param players: liste des joueurs
        """
        players = sorted(players, key=lambda x: x.get('last_name'))
        self.reports_view.display_players(players, "by name")

    def all_players_rank(self, players):
        """Rapport des joueurs (trié par rang)

        @param players: liste des joueurs
        """
        players = sorted(players, key=lambda x: x.get('rank'))
        self.reports_view.display_players(players, "by rank")

    def tournament_players(self):
        """Joueurs d'un rapport de tournoi
        Sélectionnez le tournoi pour afficher les joueurs

        @return: Liste des joueurs du tournoi sélectionné
        """
        user_input, tournaments = self.tournament_select()

        for i in range(len(tournaments)):
            if user_input == str(tournaments[i]['id']):
                return tournaments[i]["players"]

    def all_tournaments(self):
        """Tous les tournois rapportent"""
        self.reports_view.display_tournaments_report(Tournament.load_tournament_db())

    def tournament_rounds(self):
        """Tous les rondes d'un tournoi"""
        user_input, tournaments = self.tournament_select()

        self.reports_view.report_header(tournaments[int(user_input) - 1])
        self.reports_view.display_rounds_report(tournaments[int(user_input) - 1]["rounds"])

    def tournament_matches(self):
        """Tous les matchs d'un tournoi"""
        user_input, tournaments = self.tournament_select()

        self.reports_view.report_header(tournaments[int(user_input) - 1])

        rounds = tournaments[int(user_input) - 1]["rounds"]
        round_matches = []
        for i in range(len(rounds)):
            round_matches.append(rounds[i][3])

        matches = []
        for i in range(len(round_matches)):
            for k in range(4):
                matches.append(round_matches[i][k])

        self.reports_view.display_matches_report(matches)

    def tournament_select(self):
        """Chargez tous les tournois pour la sélection

        @return: Sélection des utilisateurs, liste de tous les tournois
        """
        tournaments = Tournament.load_tournament_db()
        self.menu_view.select_tournament(tournaments)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "r":
            self.back_to_menu()

        else:
            return user_input, tournaments

    @staticmethod
    def back_to_menu():
        from chessApp.controllers.menu_controller import MenuController
        MenuController().main_menu_start()
