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
    # ce qui rend la fonction plus concise et plus facile à modifier à l'avenir. 
    # Chaque clé correspond à une option du menu et chaque valeur correspond à la description de l'option. 
    # La boucle for parcourt le dictionnaire et imprime chaque option avec sa description. 
    # Le code de couleur est défini en fonction de la clé 
    # Si c'est 'Q', le code de couleur rouge est utilisé, sinon le code de couleur bleu est utilisé).

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
        
        print("\n" * 3 + "\033[1m--- Gestion Tournois - ♝ Choisir une option ♝ ---\033[0m\n")
        print("──\033[0m")
        
        for key, value in menu_options.items():
            print(f"{key} - {value}")


    def new_player_submenu(self):
        """Displays the new player submenu"""
        menu_options = {
            '1': 'Ajouter un nouveau joueur ♛',
            '2': 'Mettre à jour un joueur existant ♞',
            'r': 'Saisir la touche \'r\' pour revenir au menu précédent'
        }
        
        print("\n" * 3 + "\033[1m--- Gestion Joueurs - ♝ Choisir une option ♝ ---\033[0m\n")
        print("──\033[0m")
        
        for key, value in menu_options.items():
            print(f"{key} - {value}")


    @staticmethod
    def create_tournament_header():
        print("\n" * 3 + "\033[1m┌── NOUVEAU TOURNOI ──┐\033[0m")

    @staticmethod
    def time_control_options():
        print("\n\033[96mChoisir la durée :\033[0m")
        print("──\033[0m")
        print("\033[94m[1] Bullet\033[0m")

        print("\033[94m[2] Blitz\033[0m")

        print("\033[94m[3] Rapid\033[0m")

        print("\n\033[91m[r] Saisir 'r' pour revenir au menu précédent\033[0m")

    @staticmethod
    def review_tournament(info, players):
        """Display all input info to review before saving to database

        @param info: input info list
        @param players: list of selected players
        """
        print("\n\n\033[1mUn nouveau tournoi a été enregistré :\033[0m\n")

        print(
            f"\033[96m{info[0].upper()}, {info[1].title()}\033[0m", end=' | ')

        print(f"Description : {info[2]}", end=' | ')

        print("\033[94mRounds : 4\033[0m", end=' | ')

        print(f"Durée : {info[3]}")

        print("\n\033[1mPlayers (8 total) :\033[0m\n")

        for item in players:
            print(
                f"\033[95mPlayer {players.index(item) + 1} : \033[0m", end='')

            print(f"{item['id']}", end=' | ')

            print(
                f"\033[96m{item['last_name']}, {item['first_name']}\033[0m", end=' | ')

            print(f"{item['date_of_birth']}", end=' | ')

            print(f"\033[93mRank : {item['rank']}\033[0m")

        print(
            "\n\033[92mEnregistrer dans la base de donnée ? [o/n] \033[0m", end='')

    @staticmethod
    def tournament_saved():
        print(
            "\n\033[92mLe Tournoi a été enregistré dans la base de donnée avec succès !\033[0m")

    @staticmethod
    def start_tournament_prompt():
        print("\n\033[96mCommencer maintenant ? [o/n] \033[0m", end='')

    @staticmethod
    def select_players(players, player_number):
        """Display all players to select

        @param players: list of players
        @param player_number: number of current player for new tournament (if editing player == "")
        """
        print(f"\n\033[96mSélectionner joueur {player_number} :\033[0m\n")

        for i in range(len(players)):
            print(f"\033[94m[{players[i]['id']}]\033[0m", end=' ')

            print(
                f"\033[96m{players[i]['last_name']}, {players[i]['first_name']}\033[0m", end=" | ")

            print(
                f"{players[i]['gender']} | {players[i]['date_of_birth']}", end=" | ")

            print(f"\033[93mRank : {players[i]['rank']}\033[0m")

        print("Saisir 'r' pour revenir au menu précédent")

    @staticmethod
    def select_tournament(tournaments):
        """Display all tournaments to select

        @param tournaments: tournaments list
        """
        print("\n" * 3 + "\033[1m--- CHOISIR UN TOURNOI ---\033[0m\n")

        for i in range(len(tournaments)):
            print(f"\033[94m[{tournaments[i]['id']}]\033[0m", end=' ')
            print(tournaments[i]['name'], end=' | ')
            print(tournaments[i]['location'], end=" | ")
            print(tournaments[i]['description'], end=' | ')
            print(f"Started on : {tournaments[i]['start_date']}", end=' | ')
            print(f"Ended on : {tournaments[i]['end_date']}", end=' | ')
            print(
                f"\033[93mRound {tournaments[i]['current_round']-1}/{tournaments[i]['rounds_total']}\033[0m")

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
        print(
            "\n\033[92mEnregistrer dans la base de donnée ? [o/n] \033[0m", end='')

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
            "\n\033[92mJoueur enregistré dans la base de donnée avec succès !\033[0m")

    @staticmethod
    def reports_menu():
        print(
            "\n" * 3 + "\033[1m--- RAPPORTS - ♝ Choisir une option ♝ ---\033[0m\n")
        print("──\033[0m")
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
            f"\n\033[96mChoisir {option} (Saisir [r] pour revenir au menu précédent) : \033[0m", end='')
        print("──\033[0m")

    @staticmethod
    def input_prompt():

        print(
            "\n\033[96mChoisir [option] et utiliser la touche ENTREE pour valider ! : \033[0m", end='')
        print("──\033[0m")

    @staticmethod
    def are_you_sure_exit():

        print(
            "\n\033[91mSouhaitez-vous vraiment quitter cette application ? [o/n] \033[0m", end='')
        print("──\033[0m")

    @staticmethod
    def input_error():

        print(
            "\n\033[91mErreur de saisie, merci de choisir une option valide.\033[0m")
        print("──\033[0m")

    @staticmethod
    def player_already_selected():

        print(
            "\n\033[91mCe joueur a déjà été sélectionné. Merci de sélectionner un autre joueur.\033[0m")

    @staticmethod
    def other_report():

        print(
            "\n\033[96mSouhaitez-vous consulter un autre rapport ? [o/n] \033[0m", end='')

    @staticmethod
    def update_rank():

        print("\n\033[92mMettre à jour les rangs ? [o/n] \033[0m", end='')

    @staticmethod
    def rank_update_header(player):

        print(f"\nMise à jour {player.last_name}, {player.first_name}")
