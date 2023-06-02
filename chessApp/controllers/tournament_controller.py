from datetime import datetime

from chessApp.models.player_model import Player
from chessApp.models.round_model import Round
from chessApp.views.round_view import RoundViews
from chessApp.views.menu_view import MenuViews
from chessApp.controllers.user_Input_validation import UserInputValidation

prompt = "...\n" \



class TournamentController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.round_view = RoundViews()

        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, t):
        """Tournoi (T) Structure principale
        Commencez à partir du premier tour ou du tournoi
        en fonction du numéro de round
        Définissez les minuteries de démarrage et de fin et enregistrer sur DB
        """
        if t.current_round == 1:
            t.start_date = self.timer
            t.update_timer(t.start_date, 'start_date')

            self.first_round(t)
            t.current_round += 1
            t.update_tournament_db()

            while t.current_round <= t.rounds_total:
                self.next_rounds(t)
                t.current_round += 1
                t.update_tournament_db()

        elif 1 < t.current_round <= t.rounds_total:
            while t.current_round <= t.rounds_total:
                self.next_rounds(t)
                t.current_round += 1
                t.update_tournament_db()

            t.end_date = self.timer
            t.update_timer(t.end_date, 'end_date')
            self.tournament_end(t)

        elif t.current_round > t.rounds_total:
            self.tournament_end(t)

    def first_round(self, t):
        """Premier tour: les meilleurs joueurs contre les joueurs inférieurs
        Obtenez des paires et mettez le tour pour enregistrer sur DB"""
        r = Round("Round 1", self.timer, "TBD")
        t.sort_players_by_rank()
        top_players, bottom_players = t.split_players()
        self.round_view.round_header(t, r.start_datetime)

        for i in range(t.rounds_total):
            r.get_match_pairing(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_opponents(
                top_players[i], bottom_players[i])

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)
        scores_list = []

        if user_input == "ok":
            r.end_datetime = self.timer
            t.rounds.append(r.set_round())
            t.merge_players(top_players, bottom_players)

            self.end_of_round(scores_list, t)

        elif user_input == "r":
            self.back_to_menu()

    def next_rounds(self, t):
        """Counds suivants: définir les accords possibles
        Obtenez des paires et mettez le tour pour enregistrer sur DB"""
        r = Round(("Round " + str(t.current_round)), self.timer, "TBD")
        t.sort_players_by_score()
        self.round_view.round_header(t, r.start_datetime)

        available_list = t.players
        players_added = []

        k = 0
        while k < t.rounds_total:
            if available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added = \
                        self.match_other_option(
                            available_list, players_added, r)
                    t.players = players_added

                except IndexError:
                    available_list, players_added = \
                        self.match_first_option(
                            available_list, players_added, r)
                    t.players = players_added

            elif available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added = \
                    self.match_first_option(available_list, players_added, r)
                t.players = players_added

            k += 1

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)
        scores_list = []

        if user_input == "ok":
            r.end_datetime = self.timer
            t.rounds.append(r.set_round())
            self.end_of_round(scores_list, t)

        elif user_input == "back":
            self.back_to_menu()

    def match_first_option(self, available_list, players_added, r):
        """Option d'appariement principal

        @param disponible_list: Liste des joueurs non définis
        @Param Players_Added: Liste des joueurs déjà en match
        @param r: rond actuel
        @return: listes mises à jour
        """
        r.get_match_pairing(available_list[0], available_list[1])
        available_list[0], available_list[1] = self.update_opponents(
            available_list[0], available_list[1])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added

    def match_other_option(self, available_list, players_added, r):
        """Alternative pairing option

        @param available_list: list of players not set in match
        @param players_added: list of players already in match
        @param r: current round
        @return: updated lists
        """
        r.get_match_pairing(available_list[0], available_list[2])
        available_list[0], available_list[2] = self.update_opponents(
            available_list[0], available_list[2])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added

    def end_of_round(self, scores_list: list, t):
        """Fin du tour: Mettez à jour les scores des joueurs

        @param t: tournoi actuel
        @param scores_list: liste des scores
        @return: Liste des joueurs avec des scores mis à jour
        """
        for i in range(t.rounds_total):
            self.round_view.score_options(i + 1)
            response = self.input_scores()
            scores_list = self.get_score(response, scores_list)

        t.players = self.update_scores(t.players, scores_list)

        return t.players

    def input_scores(self):
        """Score d'entrée"""
        self.round_view.score_input_prompt()
        response = input()
        return response

    def get_score(self, response, scores_list: list):
        """Scores d'entrée pour chaque match en rond actuel

        @param réponse: entrée utilisateur (STR)
        @param scores_list: liste des scores
        @return: Liste mise à jour des scores
        """
        if response == "0":
            scores_list.extend([0.5, 0.5])
            return scores_list
        elif response == "1":
            scores_list.extend([1.0, 0.0])
            return scores_list
        elif response == "2":
            scores_list.extend([0.0, 1.0])
            return scores_list
        elif response == "back":
            self.back_to_menu()
        else:
            self.menu_view.input_error()
            self.input_scores()

    @staticmethod
    def update_scores(players, scores_list: list):
        """Mettre à jour les scores des joueurs

        Players @param: liste des joueurs
        @param scores_list: liste des scores
        @return: liste des joueurs avec des scores mis à jour
        """
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def update_player_lists(player_1, player_2, available_list, players_added):
        """Mettre à jour les listes des joueurs:
        Ajouter un joueur indisponible à la liste respective
        Supprimer la liste respective du formulaire de joueur disponible

        @param joueur_1: joueur 1 (dict)
        @param joueur_2: le joueur 2 (dict)
        @param disponible_list: liste des joueurs non définis
        @Param Players_Added: Liste des joueurs déjà en match
        @return: liste des joueurs disponibles, liste des joueurs indisponibles
        """
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)

        return available_list, players_added

    @staticmethod
    def update_opponents(player_1, player_2):
        player_1["opponents"].append(player_2["id"])
        player_2["opponents"].append(player_1["id"])

        return player_1, player_2

    def tournament_end(self, t):
        """Fin du tournoi: afficher les résultats finaux
        Offrir à l'utilisateur pour mettre à jour les rangs

        @param t: le tournoi actuel dict
        """
        t.sort_players_by_rank()
        t.sort_players_by_score()

        self.round_view.display_results(t)

        self.menu_view.update_rank()
        user_input = UserInputValidation.get_validated_input(prompt)

        players = t.players

        if user_input == "n":
            self.back_to_menu()

        elif user_input == "o":
            while True:
                self.update_ranks(players)

    def update_ranks(self, players):
        """Mettre à jour les rangs des joueurs et enregistrer sur DB

        @Param Players: Liste des joueurs de tournoi
        """
        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = UserInputValidation.get_validated_input(prompt)

        if user_input == "r":
            self.back_to_menu()
        else:
            for i in range(len(players)):
                if int(user_input) == players[i]["id"]:
                    p = players[players.index(players[i])]
                    p = Player(
                        p['id'],
                        p['last_name'],
                        p['first_name'],
                        p['date_of_birth'],
                        p['gender'],
                        p['rank']
                    )

                    self.menu_view.rank_update_header(p)
                    self.menu_view.input_prompt_text("new rank")

                    if user_input == "back":
                        self.back_to_menu()

                    else:
                        p.update_player_db(int(user_input), "rank")
                        players[i]["rank"] = int(user_input)
        # Cette ligne est maintenant en dehors de la boucle 'for'
        # Elle n'est exécutée qu'après que tous les joueurs ont été mis à jour.
        return players

    @staticmethod
    def back_to_menu():
        from chessApp.controllers.menu_controller import MenuController
        MenuController().main_menu_start()
