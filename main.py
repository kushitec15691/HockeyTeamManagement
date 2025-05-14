from userinterface import UserInterface

#region - Main Menu

def main():
    """
    Main function to initialize and run the User Interface.

    This function creates an instance of the UserInterface class and invokes its run() method.

    Parameters:
    None

    Returns:
    None
    """
    # instantiate new object of UserInterface Class
    interface = UserInterface()
    # Invoke run() function of UserInterface Class
    interface.run()

if __name__ == "__main__":
    main()

#endregion
