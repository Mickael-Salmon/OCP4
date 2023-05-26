class UserInputValidation:
    """Fonction globale pour la validation des entrées utilisateur"""

    @staticmethod
    def get_validated_input(prompt):
        """Validate user input."""
        valid_inputs = [
            "q", "r", "1", "2", "3", "4", "5",
            "6", "7", "8", "o", "n"
        ]

        while True:
            print(prompt)
            user_input = input().lower()

            if user_input.isdigit() or user_input in valid_inputs:
                return user_input

            print("♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜")
