from hockey_cup_service import HockeyCupService
from input_validation import InputValidatorService
from style_sheet import print_menu_title


class UserInterface():
    # Create a instance of the
    hockey_cup_service = HockeyCupService()
    # Chek Historical data and load to in to the memory
    hockey_cup_service.load_from_file(1)

    # Get the last saved Id and set to gloabal variable
    hockey_cup_service.get_last_id_from_historical_data()

    while True:
        # To print the main title of the menu
        print_menu_title()

        # The user interface shall consist of different menu options. The menu options shall be
        # possibly to use in an arbitrary order. One option has to be for quitting the program.
        # The user interface must be easy to use for a person that is not familiar with the program.

        print(f"1. Create New Team")
        print(f"2. Display Existing Team Information By Team ID")
        print(f"3. Update Existing Team By Team No")
        print(f"4. Delete Existing Team By Team No")
        print(f"5. Display All Teams")
        print(f"6. Display Girls Teams Only")
        print(f"7. Display Boys Teams Only")
        print(f"8. Display Analytics")
        print(f"9. Cancel Team Participation For the Event")
        print(f"10. Save Entered Records to the File")
        print(f"11. Load from the File")
        print(f"12. Exit/Quit")

        user_option = input(f"\nPlease select an option by entering the corresponding number:")

        if user_option == '1':
            # Create a new team
            print(f"1. Create New Team")
            team_name_input = InputValidatorService.validate_team_name_input()
            team_type_input = InputValidatorService.validate_team_type_input()
            fee_input = InputValidatorService.validate_participation_fee_input()
            fee_status = InputValidatorService.validate_fee_status_input()
            hockey_cup_service.create_team(team_name_input, team_type_input, fee_input, fee_status)

        elif user_option == '2':
            print(f"2. Show Existing Team Information By Team ID\n")
            # Read team information
            team_id = InputValidatorService.validate_team_id_input()
            hockey_cup_service.read_team(team_id)
            input(f"To return to the Main Menu, kindly press the Enter key..")
        elif user_option == '3':
            print(f"3. Update Existing Team By Team No\n")
            team_id = InputValidatorService.validate_team_id_input()
            print(f"Here is the current details of the team\n")
            valid_team = hockey_cup_service.read_team(team_id, 1)
            if (valid_team == 1):
                confirm = InputValidatorService.validate_user_conferamtion_input(
                    f"Are you sure you want to update Team  [Y/N]?  \n")
                if (confirm == 'Y'):
                    # print(f"Here is the current details of the team\n")
                    # hockey_cup_service.read_team(team_id,1)
                    newname = input(f"Do you want to update the name  [Y/N]?  \n")
                    if (newname == 'Y'):
                        team_name_input = InputValidatorService.validate_team_name_input("new")
                        hockey_cup_service.update_team(team_id, team_name_input, "N", 1)

                    newtype = InputValidatorService.validate_user_conferamtion_input(
                        f"Do you want to update the type  [Y/N]?  \n")
                    if (newtype == 'Y'):
                        team_type_input = InputValidatorService.validate_team_type_input("new")
                        hockey_cup_service.update_team(team_id, team_type_input, "T", 1)

                    newfee = InputValidatorService.validate_user_conferamtion_input(
                        f"Do you want to update the fee  [Y/N]?\n")
                    if (newfee == 'Y'):
                        fee_input = InputValidatorService.validate_participation_fee_input("new")
                        hockey_cup_service.update_team(team_id, fee_input, "F", 1)

                    newfeestatus = InputValidatorService.validate_user_conferamtion_input(
                        f"Do you want to update the fee status [Y/N]?\n")
                    if (newfeestatus == 'Y'):
                        fee_status = InputValidatorService.validate_fee_status_input()
                        hockey_cup_service.update_team(team_id, fee_status, "S", 1)

                    print(f"Here is the updated details of the team\n")
                    hockey_cup_service.read_team(team_id)

                    input(f"To return to the Main Menu, kindly press the Enter key..")

            else:
                input(f"To return to the Main Menu, kindly press the Enter key..")

        elif user_option == '4':
            # Delete a team
            print(f"4. Delete Existing Team By Team No\n")
            team_id = InputValidatorService.validate_team_id_input()
            confirm = InputValidatorService.validate_user_conferamtion_input(
                "Are you sure you want to delete Team  [Y/N]?\n")
            if (confirm == 'Y'):
                hockey_cup_service.delete_team(team_id)

        elif user_option == '5':
            # List all teams
            print(f"5. List All Teams\n")
            hockey_cup_service.list_teams_info()

        elif user_option == '6':
            # List girls teams
            print(f"6. List Girls Teams Only\n")
            hockey_cup_service.list_girls_teams_Info()

        elif user_option == '7':
            # List boys teams
            print(f"7. List Boys Teams Only\n")
            hockey_cup_service.list_boys_teams_Info()

        elif user_option == '8':
            # Show team info
            print(f"8. Analytics\n")
            hockey_cup_service.show_team_analytics()
        elif user_option == '9':
            # Cancel team participation
            print(f"9. Cancel Team Participation For the Event\n")
            cancelparticipation = InputValidatorService.validate_user_conferamtion_input(
                f"Are you sure you want to cancel the team's participation in the event? Please note that once canceled, the team cannot be re-activated. [Y/N]?\n")
            if (cancelparticipation == 'Y'):
                team_id = InputValidatorService.validate_team_id_input()
                date = InputValidatorService.validate_cancelation_date_input()
                hockey_cup_service.cancel_team_participation(team_id, date)
        elif user_option == '10':
            # Save data to a file
            savedatatextfile = InputValidatorService.validate_user_conferamtion_input(
                f"Do you want to save data in the text file [Y/N]?\n")
            if (savedatatextfile == 'Y'):
                print(f"10. Save Records to the File\n")
                hockey_cup_service.save_to_file()
        elif user_option == '11':
            # Load data from a file
            loaddatatextfile = InputValidatorService.validate_user_conferamtion_input(
                f"Do you want to load data historical data from text file [Y/N]?\n")
            if (loaddatatextfile == 'Y'):
                print(f"11. Load from File\n")
                hockey_cup_service.load_from_file()
        elif user_option == '12':
            # Exit the program
            print(f"12. Quit")
            quit = InputValidatorService.validate_user_conferamtion_input(
                f"Would you like to save the changes to the text file for future use [Y/N]?\n")
            if (quit == 'Y'):
                hockey_cup_service.save_to_file(1)

            print("Thank you for using Hockey Cup Team Management System")
            exit()
        else:
            # Handle invalid user_options
            print("Invalid user_option. Please try again.\n")
