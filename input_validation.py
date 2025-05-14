import re

_id_counter = 0


class InputValidatorService:
    """
        InputValidatorService class provides methods for validating various user inputs related to team information.

        Methods:
        - validate_team_id_input(): Validates user input for Team ID.
        - validate_team_name_input(str=''): Validates user input for Team Name.
        - validate_team_type_input(str=''): Validates user input for Team Type.
        - validate_participation_fee_input(str=''): Validates user input for Participation Fee.
        - validate_fee_status_input(str=''): Validates user input for Fee Status.
        - validate_cancelation_date_input(str=''): Validates user input for Cancellation Date.
        - validate_user_confirmation_input(str=''): Validates user input for user confirmation (Y-Yes, N-No).
        """
    def validate_team_id_input():
        """
          Validates user input for Team ID.

          Returns:
          int: Validated Team ID.
        """
        while True:
            try:
                id = int(input(f"Enter the Team ID: "))
                return id
            except ValueError as e:
                print(f"Enter a valid Team ID.")

    def validate_team_name_input(str=''):

        while True:
            team_name_input = input(f"Enter the {str} team name : ")
            if re.match(r'^(?![\s-]*$)[A-Za-z0-9 -]+$', team_name_input) is not None:
                return team_name_input
            else:
                print(f"Invalid input. Please enter the valid team name.")
                # Prompt the user again
                continue

    def validate_team_type_input(str=''):
        while True:
            team_type_input = input(f"Enter the {str} team type (e.g., Girls-G, Boys-B) : ")
            if team_type_input in ["G", "B"]:
                return team_type_input
            else:
                print(f"Invalid input. Please enter a valid team type (e.g., Girls-G, Boys-B).")
                # Prompt the user again
                continue

    def validate_participation_fee_input(str=''):
        while True:
            try:
                fee_input = float(input(f"Enter the {str} participation fee (SEK): "))
                if fee_input <= 0:
                    raise ValueError(f"Participation fee should be greater than 0.")
                return fee_input
            except ValueError as e:
                print(f"Please enter a valid participations fee (SEK).")

    def validate_fee_status_input(str=''):
        while True:
            fee_status = input(f"Enter the {str} fee paid status (e.g., Yes-Y, No-N): ")
            if fee_status in ["Y", "N"]:
                if (fee_status == "Y"):
                    return True
                else:
                    return False

            else:
                print(f"Invalid input. Please enter a valid fee status (Y, N).")
                # Prompt the user again
                continue

    def validate_cancelation_date_input(str=''):
        while True:
            cancel_date = input(f"Enter the {str} cancelation date (YYYY-MM-DD): ")
            if re.match(r'\d{4}-\d{2}-\d{2}', cancel_date):
                return cancel_date
            else:
                print(f"Invalid input. Please enter a valid cancelation date (YYYY-MM-DD).")
                # Prompt the user again
                continue

    def validate_user_conferamtion_input(str=''):
        while True:
            fee_status = input(f" {str}  ")
            if fee_status in ["Y", "N"]:
                if (fee_status == "Y"):
                    return "Y"
                else:
                    return "N"

            else:
                print(f"Invalid input. Please enter a valid input (Y-Yes, N-No).")
                # Prompt the user again
                continue