from prettytable import PrettyTable


class Reports:

    def __init__(self):

        self.table = PrettyTable()

        self.player_report_field_names = [
            "ID",
            "Last name",
            "First name",
            "Gender",
            "Date of birth",
            "Rank"
        ]

        self.tournament_report_field_names = [
            "ID",
            "Name",
            "Location",
            "Description",
            "Start date",
            "End date",
            "Time control",
            "Last round played",
            "Players (ID : Name)",
        ]

        self.matches_report_field_names = [
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

        self.rounds_report_field_names = [
            "Round #",
            "Started at",
            "Ended at",
            "Matches"
        ]

    def display_players(self, players, sorting):
        """Display player report (all sorting types)"""
        self.table.clear()
        self.table.field_names = self.player_report_field_names
        self.table.align = "l"

        for i in range(len(players)):
            self.table.add_row([
                players[i]["id"],
                players[i]["last_name"],
                players[i]["first_name"],
                players[i]["gender"],
                players[i]["date_of_birth"],
                players[i]["rank"]
            ])

        print("\n" + "=" * 80)
        print(f"- All players ({sorting}) -".center(80))
        print("=" * 80)
        print(self.table)

    def display_tournaments_report(self, tournaments):
        """Display tournament reports"""
        self.table.clear()
        self.table.field_names = self.tournament_report_field_names
        self.table.align = "l"

        for i in range(len(tournaments)):
            participants = []
            players = tournaments[i]["players"]
            for k in range(len(players)):
                participants.append(
                    str(players[k]["id"]) + " : " + players[k]["last_name"])

            self.table.add_row([
                tournaments[i]["id"],
                tournaments[i]["name"],
                tournaments[i]["location"],
                tournaments[i]["description"],
                tournaments[i]["start_date"],
                tournaments[i]["end_date"],
                tournaments[i]["time_control"],
                str(tournaments[i]["current_round"]-1) +
                "/" + str(tournaments[i]["rounds_total"]),
                participants
            ])

        print("\n" + "=" * 80)
        print("- All tournaments -".center(80))
        print("=" * 80)
        print(self.table)

    def display_matches_report(self, matches):
        """Display matches in tournament report"""
        self.table.clear()
        self.table.field_names = self.matches_report_field_names
        self.table.align = "l"

        for i in range(len(matches)):
            matches[i].insert(3, "vs.")
            self.table.add_row(matches[i])

        print("\n" + "=" * 80)
        print(f"- All played matches ({len(matches)} total) -".center(80))
        print("=" * 80)
        print(self.table)

    def display_rounds_report(self, rounds):
        """Display rounds in tournament report"""
        self.table.clear()
        self.table.field_names = self.rounds_report_field_names
        self.table.align = "l"

        for i in range(len(rounds)):
            for j in range(4):
                if j == 0:
                    self.table.add_row([
                        rounds[i][0],
                        rounds[i][1],
                        rounds[i][2],
                        rounds[i][3][j]
                    ])
                else:
                    self.table.add_row([
                        ' ',
                        ' ',
                        ' ',
                        rounds[i][3][j]
                    ])

        print("\n" + "=" * 80)
        print("- All played rounds -".center(80))
        print("=" * 80)
        print(self.table)

    @staticmethod
    def report_header(info):
        """Header for tournament reports

        @param info: tournament (dict)
        """
        print("\n")

        h_1 = "{}, {} | Description: {}".format(
            info['name'].upper(), info['location'].title(),
            info['description'])
        h_2 = (
            "Start date: {} | End date: {} | Time control: {} | "
            "Rounds played: {}/{}"
        ).format(
            info['start_date'], info['end_date'], info['time_control'],
            info['current_round'] - 1, info['rounds_total'])

        print("=" * 80)
        print(h_1.center(80))
        print(h_2.center(80))
        print("=" * 80)
