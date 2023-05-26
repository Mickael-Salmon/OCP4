class MenuViews:

    def __init__(self):
        pass

    @staticmethod
    def app_title():
        MenuViews()
        print("────────────────────────────────────────────\033[0m")
        print("───── ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ ──────")
        print("────────────────────────────────────────────\033[0m")
        print("───── ♜ ♞ ♝ ♛ GESTION TOURNOIS ♚ ♝ ♞ ♜ ─────")
        print("────────────────────────────────────────────\033[0m")
        print("───── ♟ ♟ ♟ ♟      ECHECS      ♟ ♟ ♟ ♟ ─────")
        print("────────────────────────────────────────────\033[0m")

    # Cette version utilise un dictionnaire pour stocker les options du menu
    # Chaque clé correspond à une option du menu et chaque valeur correspond
    # à la description de l'option
    # La boucle for parcourt le dictionnaire
    # et imprime chaque option avec sa description
    # Le code de couleur est défini en fonction de la clé
    # Si c'est 'Q', le code de couleur rouge est utilisé,
    # sinon le code de couleur bleu est utilisé).

    @staticmethod
    def main_menu():
        menu_options = {
            '1': 'Gestion des tournois',
            '2': 'Gestion des joueurs',
            '3': 'Gestion des rapports',
            'Q': 'Quitter le programme'
        }
        print("\n\n\033[1m┌─────── ♛ MENU PRINCIPAL ♛ ───────┐\033[0m\n")
        for key, value in menu_options.items():
            color_code = '\033[94m' if key != 'Q' else '\033[91m'
            print(f"{color_code}[{key}] {value}\033[0m")

    @staticmethod
    def gestion_tournois_menu():
        menu_options = {
            '1': 'Créer un nouveau tournoi',
            '2': 'Reprendre un tournoi commencé',
            'r': 'Saisir \'r\' pour revenir au menu précédent'
        }
        print("\n\n\033[1m┌─────── ♚ GESTION DES TOURNOIS ♚ ───────┐\033[0m\n")
        for key, value in menu_options.items():
            color_code = '\033[94m' if key != 'r' else '\033[91m'
            print(f"{color_code}[{key}] {value}\033[0m")

    @staticmethod
    def gestion_joueurs_menu():
        menu_options = {
            '1': 'Créer un nouveau joueur',
            '2': 'Modifier un joueur existant',
            'r': 'Saisir \'r\' pour revenir au menu précédent'
        }
        print("\n\n\033[1m┌─────── ♝ GESTION DES JOUEURS ♝ ───────┐\033[0m\n")
        for key, value in menu_options.items():
            color_code = '\033[94m' if key != 'r' else '\033[91m'
            print(f"{color_code}[{key}] {value}\033[0m")

    def new_tournament_submenu(self):
        """Displays the new tournament submenu"""
        menu_options = {
            '1': 'Créer un nouveau tournoi ♜',
            '2': 'Reprendre un tournoi en cours ♚',
            'r': 'Saisir \'r\' pour revenir au menu précédent'
        }
        print("\n" * 3 + "\033[1m--- ♝ Gestion Tournois ♝ ---\033[0m\n")
        for key, value in menu_options.items():
            print(f"{key} - {value}")

    def new_player_submenu(self):
        """Displays the new player submenu"""
        menu_options = {
            '1': 'Ajouter un nouveau joueur ♛',
            '2': 'Mettre à jour un joueur existant ♞',
            'r': 'Saisir la touche \'r\' pour revenir au menu précédent'
        }
        print("\n" * 3 + "\033[1m--- ♝ Gestion Joueurs ♝ ---\033[0m\n")
        for key, value in menu_options.items():
            print(f"{key} - {value}")

    @staticmethod
    def create_tournament_header():
        print("\n" * 3 + "\033[1m┌── NOUVEAU TOURNOI ──┐\033[0m")

    @staticmethod
    def time_control_options():
        menu_options = {
            '1': 'Bullet',
            '2': 'Blitz',
            '3': 'Rapid',
            'r': 'Saisir \'r\' pour revenir au menu précédent'
        }
        print("\n\033[96mChoisir la durée :\033[0m")
        for key, value in menu_options.items():
            color_code = '\033[94m' if key != 'r' else '\033[91m'
            print(f"{color_code}[{key}] {value}\033[0m")

    @staticmethod
    def review_tournament(info, players):
        """Display all input info to review before saving to database

        @param info: input info list
        @param players: list of selected players
        """
        print("\n\n\033[1mUn nouveau tournoi a été enregistré :\033[0m\n")
        tournament_info = [
            f"\033[96m{info[0].upper()}, {info[1].title()}\033[0m",
            f"Description : {info[2]}",
            "\033[94mRounds : 4\033[0m",
            f"Durée : {info[3]}"
        ]
        # Utilisation de la méthode .join() pour afficher les éléments
        # de la liste séparés par un séparateur
        print(" | ".join(tournament_info))
        print("\n\033[1mPlayers (8 total) :\033[0m\n")
        # player_info_keys = ['id', 'last_name',
        # 'first_name', 'date_of_birth', 'rank']
        for item in players:
            player_info = [
                f"\033[95mPlayer {players.index(item) + 1} : \033[0m",
                f"{item['id']}",
                f"\033[96m{item['last_name']}, {item['first_name']}\033[0m",
                f"{item['date_of_birth']}",
                f"\033[93mRank : {item['rank']}\033[0m"
            ]
            print(" | ".join(player_info))
        print("\n\033[92mEnregistrer dans la base ? [o/n] \033[0m", end='')

    @staticmethod
    def tournament_saved():
        print(
            "\n\033[92mLe Tournoi a été enregistré avec succès !\033[0m")

    @staticmethod
    def start_tournament_prompt():
        print("\n\033[96mCommencer maintenant ? [o/n] \033[0m", end='')

    @staticmethod
    def select_players(players, player_number):
        """Display all players to select

        @param players: list of players
        @param player_number: number of current player for new tournament
        (if editing player == "")
        """
        print(f"\n\033[96mSélectionner joueur {player_number} :\033[0m\n")
        for i in range(len(players)):
            player_id = f"\033[94m[{players[i]['id']}]\033[0m"
            player_name = (
                f"{players[i]['last_name']}, {players[i]['first_name']}")
            player_gender_dob = (
                f"{players[i]['gender']} | {players[i]['date_of_birth']}")
            player_rank = f"\033[93mRank : {players[i]['rank']}\033[0m"

            print(player_id, end=' ')
            print(player_name, end=" | ")
            print(player_gender_dob, end=" | ")
            print(player_rank)

        print("Saisir 'r' pour revenir au menu précédent")

    @staticmethod
    def select_tournament(tournaments):
        """Display all tournaments to select

        @param tournaments: tournaments list
        """
        print("\n" * 3 + "\033[1m--- CHOISIR UN TOURNOI ---\033[0m\n")
        for i in range(len(tournaments)):
            tournament_id = f"\033[94m[{tournaments[i]['id']}]\033[0m"
            tournament_name = tournaments[i]['name']
            location = tournaments[i]['location']
            description = tournaments[i]['description']
            start_date = f"Started on : {tournaments[i]['start_date']}"
            end_date = f"Ended on : {tournaments[i]['end_date']}"
            current_round = tournaments[i]['current_round'] - 1
            rounds_total = tournaments[i]['rounds_total']
            rounds_info = f"Round {current_round}/{rounds_total}"

            print(tournament_id, end=' ')
            print(tournament_name, end=' | ')
            print(location, end=" | ")
            print(description, end=' | ')
            print(start_date, end=' | ')
            print(end_date, end=' | ')
            print(rounds_info)

        print("\n\033[91m[r] Saisir 'r' pour revenir au menu précédent\033[0m")

    @staticmethod
    def create_new_player_header():
        print("\n" * 3 + "\033[1m- NOUVEAU JOUEUR-\033[0m\n")

    @staticmethod
    def review_player(info):
        """Display all input info to review before saving to database
        @param info: player info list
        """
        print("\n\n\033[1mNouveau joueur créé :\033[0m\n")
        print(f"\033[96m{info[0]}, {info[1]}\033[0m", end=' | ')
        print(f"Date de naissance : {info[2]}", end=' | ')
        print(f"Genre : {info[3]}", end=' | ')
        print(f"\033[93mRang : {info[4]}\033[0m")
        print("Enregistrer dans la base de donnée ? [o/n]", end='')

    @staticmethod
    def update_player_info(p, options):
        """Player info editing prompts

        @param p: currently edited player
        @param options: editable options
        """
        print("\n\n\033[1m--- METTRE A JOUR UN JOUEUR EXISTANT ---\033[0m\n")
        print(f"\033[96mMise à jour {p.last_name}, {p.first_name}\033[0m\n")
        for i in range(len(options)):
            print(f"\033[94m[{i+1}] Mise à jour {options[i]}\033[0m")
        print("\n\033[91m[r] Saisir 'r' pour revenir au menu précédent\033[0m")

    @staticmethod
    def player_saved():
        print(
            "Joueur enregistré dans la base de donnée avec succès !")

    @staticmethod
    def reports_menu():
        print(
            "\n" * 3 + "--- RAPPORTS - ♝ Choisir une option ♝ ---")
        print("\033[94m[1] Afficher tous les joueurs ♝\033[0m")
        print("\033[94m[2] Afficher tous les joueurs par tournoi\033[0m")
        print("\033[94m[3] Afficher tous les tournois\033[0m")
        print("\033[94m[4] Afficher tous les rounds dans un tournoi\033[0m")
        print("\033[94m[5] Afficher toutes les parties dans un tournoi\033[0m")
        print("\n\033[91m[r] Saisir 'r' pour revenir au menu précédent\033[0m")

    @staticmethod
    def reports_player_sorting():
        print("\n\033[96m[1] Classer par nom\033[0m")
        print("\033[96m[2] Classer par rang\033[0m")
        print("\n\033[91m[r] Saisir 'r' pour revenir au menu précédent\033[0m")

    @staticmethod
    def input_prompt_text(option):
        print(
            f"Choisir {option} (Saisir [r] pour le menu précédent) : ", end='')

    @staticmethod
    def input_prompt():
        print(
            "\n\033[96mNuméro + ENTREE ! : \033[0m", end='')

    @staticmethod
    def are_you_sure_exit():
        print(
            "\n\033[91mQuitter l'application ? [o/n] \033[0m", end='')

    @staticmethod
    def input_error():
        print(
            "\n\033[91mErreur, merci de choisir une option valide.\033[0m")

    @staticmethod
    def player_already_selected():
        print(
            "\n\033[91mDéjà sélectionné. Merci de choisir un autre.\033[0m")

    @staticmethod
    def other_report():
        print(
            "\n\033[96mConsulter un autre rapport ? [o/n] \033[0m", end='')

    @staticmethod
    def update_rank():
        print("\n\033[92mMettre à jour les rangs ? [o/n] \033[0m", end='')

    @staticmethod
    def rank_update_header(player):
        print(f"\nMise à jour {player.last_name}, {player.first_name}")
