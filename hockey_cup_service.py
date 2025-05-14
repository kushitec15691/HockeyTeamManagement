import os
from team import Team
from input_validation import InputValidatorService

# Data source file name added here
filename = "data_source.txt"


class HockeyCupService:
    def __init__(self):
        self.team_array = {}

    def get_last_id_from_historical_data(self):
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    last_line = None
                    for line in file:
                        last_line = line  # Update the last line with the current line

                # Check if the file was not empty
                if last_line is not None:
                    first_col = last_line.split(',')[0]
                    last_id = int(first_col)
                    last_id = last_id + 1
                    Team._id_counter = last_id

        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def check_historical_data_availability(self):
        try:
            if os.path.exists(filename):
                self.team_array.clear()  # Clear the existing team_array before loading
                with open(filename, 'r') as file:
                    content = file.read()
                    if content:
                        confirm = input(
                            f"There is historical data in the text file. Would you like to load it before proceeding? [Y/N] \n")
                        if (confirm == 'Y'):
                            self.load_from_file()

        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def create_team(self, name, team_type, fee, fee_paid):
        try:
            team = Team(name, team_type, fee, fee_paid)
            self.team_array[team.id] = team
            print(f"\nTeam has created successfully with the Team Id: {team.id} \n")
            input(f"Do you want to return to the Main Menu? Then kindly press the Enter key....")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def read_team(self, id, option=0):
        try:
            if len(self.team_array) == 0:
                print(f"\nWe are unable to find the teams.\n")
            else:
                if id in self.team_array:
                    print(self.team_array[id])
                    return 1
                else:
                    print(f"\nWe are unable to find the team. Please enter the valid team ID.\n")
            if (option == 0):
                input(f"Do you want to return to the Main Menu? Then kindly press the Enter key....")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def update_team(self, id, new_value, field, option=0):
        try:
            if id in self.team_array:
                team = self.team_array[id]
                if (field == "N"):
                    team.set_name(new_value)
                elif (field == "T"):
                    team.set_type(new_value)
                elif (field == "F"):
                    team.set_fee(new_value)
                elif (field == "S"):
                    team.set_fee_paid(new_value)
                else:
                    print(f"Field not found.\n")

                print(f"Team information successfully updated!.\n")
            else:
                print(f"We are unable to find the team. Please enter the valid team ID.\n")
            if (option == 0):
                input(f"Do you want to return to the Main Menu? Then kindly press the Enter key....")

        except ValueError as e:
            print(f"An unexpected error occurred:{str(e)}\n")

    def delete_team(self, id):
        try:
            if id in self.team_array:
                del self.team_array[id]
                print(f"Team information successfully deleted.\n")
            else:
                print(f"Team not found.\n")
            input(f"To return to the Main Menu, kindly press the Enter key..")
        except ValueError as e:
            print(f"An unexpected error occurred:{str(e)}\n")

    def list_teams_info(self):
        try:
            if len(self.team_array) == 0:
                print(f"Teams not found.\n")
            else:
                for team in self.team_array.values():
                    print(f"{team}")
                    print(f"{'-' * 34}")
            input(f"Do you want to return to the Main Menu? Then kindly press the Enter key....")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def list_girls_teams_Info(self):
        try:
            if len(self.team_array) == 0:
                print(f"\nTeams not found. Please attempt to load from the text file and try again\n")
            else:
                girls_team_array = [team for team in self.team_array.values() if team.type == 'G']
                if len(girls_team_array) > 0:
                    for team in girls_team_array:
                        print(f"{team}")
                        print(f"{'-' * 34}")
                else:
                    print(f"\nGirls teams not found.\n")
            input(f"To return to the Main Menu, kindly press the Enter key..")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def list_boys_teams_Info(self):
        try:
            if len(self.team_array) == 0:
                print(f"\nTeams not found. Please attempt to load from the text file and try again\n")
            else:
                boys_team_array = [team for team in self.team_array.values() if team.type == 'B']
                if len(boys_team_array) > 0:
                    for team in boys_team_array:
                        print(f"{team}")
                        print(f"{'-' * 34}")
                else:
                    print(f"\nBoys teams not found.\n")
            input(f"To return to the Main Menu, kindly press the Enter key..")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def show_team_analytics(self):
        try:
            if len(self.team_array) == 0:
                print(f"\nTeams not found. Please attempt to load from the text file and try again\n")
            else:
                total_team_count = len(self.team_array)
                paid_team_count = sum(1 for team in self.team_array.values() if
                                      team.cancellation_date == '0000-00-00' and team.fee_paid == True)
                cancelled_team_count = sum(
                    1 for team in self.team_array.values() if team.cancellation_date != '0000-00-00')
                paid_percentage = (paid_team_count / total_team_count) * 100 if total_team_count > 0 else 0

                print(f"Number of total teams : {total_team_count}\n")
                print(f"Number of canceled team (Not Active Team Only): {cancelled_team_count}\n")
                print(f"Number of paid team: {paid_team_count}\n")
                print(f"Percentage of Paid Teams: {paid_percentage:.2f}%\n")
                input(f"To return to the Main Menu, kindly press the Enter key..")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def cancel_team_participation(self, id, date):
        try:
            if id in self.team_array:
                self.team_array[id].set_cancellation_date("C", date)
                print(f"\nTeam participation successfully canceled.\n")
            else:
                print(f"\nTeam not found.")
            input(f"Do you want to return to the Main Menu? Then kindly press the Enter key....")
        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def save_to_file(self, option=0):
        try:
            if (len(self.team_array) > 0):
                with open(filename, "w") as file:
                    for team in self.team_array.values():
                        team_info = f"{team.id},{team.name},{team.type},{team.fee},{team.fee_paid},{team.date},{team.cancellation_date}\n"
                        file.write(team_info)

                print(f"\nThe data has been successfully saved to the text file (File name: Data_Source.txt)\n")

            else:
                print(f"\nOops..No data found for saving.\n")

            if (option == 0):
                input(f"Do you want to return to the Main Menu? Then kindly press the Enter key....")

        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

    def load_from_file(self, option=0):
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        team_data = line.strip().split(",")
                        id, name, team_type, fee, fee_paid, date, cancellation_date = team_data
                        id = int(id)
                        if id not in self.team_array:
                            team_obj = Team(name, team_type, fee, fee_paid, id, date, cancellation_date)
                            self.team_array[id] = team_obj

                print(f"\nTeam loaded successfully.\n")
            else:
                if (option == 0):
                    print(f"\nOops..Data source text file not found.\n")

        except ValueError as e:
            print(f"\nAn unexpected error occurred:{str(e)}\n")

