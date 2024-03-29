from prettytable import PrettyTable


class RoundViews:

    def __init__(self):
        self.table = PrettyTable()

        self.round_field_names = [
            "Match #",
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

        self.results_field_names = [
            "Tournament ranking",
            "Name",
            "Final Score",
            "Global ranking"
        ]

    def display_matches(self, matches):
        """Display matches for current round as table

        @param matches: list of matches tuples
        """
        self.table.clear()
        self.table.field_names = self.round_field_names

        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i+1))
            row.insert(4, "vs.")

            self.table.add_row(row)

        print(self.table)

    def display_results(self, t):
        """Display results at the end of the tournament

        @param t: current tournament
        """
        self.table.clear()
        self.table.field_names = self.results_field_names

        for i in range(len(t.players)):
            self.table.add_row([
                i + 1,
                t.players[i]["last_name"] + ", " + t.players[i]["first_name"],
                t.players[i]["score"],
                t.players[i]["rank"]
            ])

        print("\n\n- FINAL SCORES -\n")
        print(f"{t.name.upper()}, {t.location.title()} | Description:")
        print(f"{t.description}")
        print("Start:", t.start_date, "|")
        print("End:", t.end_date, "| Time control:", t.time_control)
        print(self.table)

    @staticmethod
    def round_header(t, start_time):
        """Display tournament info as a round header

        @param t: current tournament
        @param start_time: tournament start time (str)
        """
        print("\n\n")

        h_1 = "{}, {} | Description: {}".format(
            t.name.upper(), t.location.title(), t.description)
        h_2 = "Start date and time: {} | Time control: {}\n".format(
            t.start_date, t.time_control)
        h_3 = "- ROUND {}/{} | {} -".format(
            t.current_round, t.rounds_total, start_time)

        print(h_1.center(100, " "))
        print(h_2.center(100, " "))
        print(h_3.center(100, " "))

    @staticmethod
    def round_over():
        print("\nRound terminé ? [ok]")
        print("Retour au menu principal ? [r]")

    @staticmethod
    def score_options(match_number):
        print("\nMatch ", match_number)
        print('[0] Egalité')
        print('[1] JOUEUR 1 GAGNE')
        print('[2] JOUEUR 2 GAGNE')
        print("\n[r] Saisir la touche 'r' pour revenir au menu principal")

    @staticmethod
    def score_input_prompt():
        print('\nSaisir le résultat :', end=' ')
