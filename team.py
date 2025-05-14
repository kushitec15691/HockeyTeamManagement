import os
import datetime

# Data source file name
filename = "data_source.txt"

class Team:
    # Class-level counter for generating unique IDs
    _id_counter = 1

    def __init__(self, name, team_type, fee, fee_paid=False, id=0, date="0000-00-00", cancel_date="0000-00-00"):
        """
        Constructor for the Team class.

        Parameters:
        - name (str): Team name.
        - team_type (str): Team type (e.g., 'G' for Girls, 'B' for Boys).
        - fee (float): Participation fee in SEK.
        - fee_paid (bool, optional): Fee payment status. Default is False.
        - id (int, optional): Team ID. If not provided, a unique ID is generated.
        - date (str, optional): Team creation date. If not provided, the current date is used.
        - cancel_date (str, optional): Cancellation date. Default is "0000-00-00".
        """
        if (id == 0):
            self.__id = self.set_unique_id()
        else:
            self.__id = id

        if (date == "0000-00-00"):
            self.__date = self.set_datetime_now()
        else:
            self.set_date(date)

        self.__name = name
        self.__type = team_type
        self.__fee = fee
        self.__fee_paid = fee_paid

        if (cancel_date == "0000-00-00"):
            self.__cancellation_date = "0000-00-00"
        else:
            self.__cancellation_date = cancel_date

    @property
    def id(self):
        """Getter method for Team ID."""
        return self.__id

    @property
    def date(self):
        """Getter method for Team creation date."""
        return self.__date

    def set_date(self, value):
        """Setter method for Team creation date."""
        self.__date = value
        return self.__date

    @property
    def name(self):
        """Getter method for Team name."""
        return self.__name

    def set_name(self, value):
        """Setter method for Team name."""
        self.__name = value

    @property
    def type(self):
        """Getter method for Team type."""
        return self.__type

    def set_type(self, value):
        """Setter method for Team type."""
        self.__type = value

    @property
    def fee(self):
        """Getter method for Team participation fee."""
        return self.__fee

    def set_fee(self, value):
        """Setter method for Team participation fee."""
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an integer or a decimal")
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__fee = value

    @property
    def fee_paid(self):
        """Getter method for Team fee payment status."""
        return self.__fee_paid

    def set_fee_paid(self, value):
        """Setter method for Team fee payment status."""
        if value not in (True, False):
            raise ValueError("Fee paid status must be a boolean value.")
        self.__fee_paid = value

    @property
    def cancellation_date(self):
        """Getter method for Team cancellation date."""
        return self.__cancellation_date

    def set_cancellation_date(self, value, date):
        """
        Setter method for Team cancellation date.

        Parameters:
        - value (str): Cancellation identifier ("C" for cancellation).
        - date (str): Cancellation date in the format "YYYY-MM-DD".
        """
        if (value == "C"):
            self.__cancellation_date = date
            return self.__cancellation_date
        else:
            self.__cancellation_date = "0000-00-00"
            return self.__cancellation_date

    @staticmethod
    def set_unique_id():
        """Static method to generate a unique ID for a Team."""
        id = Team._id_counter
        Team._id_counter = Team._id_counter + 1
        return id

    @staticmethod
    def set_datetime_now():
        """Static method to generate the current date and time."""
        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime("%Y-%m-%d")
        return formatted_date

    def __str__(self):
        """
        String representation of the Team instance.

        Returns:
        str: Formatted string containing Team information.
        """
        if self.__type == "B":
            type_str = "Boys"
        elif self.__type == "G":
            type_str = "Girls"
        else:
            type_str = self.__type

        fee_paid = str(self.__fee_paid)
        if fee_paid == "True":
            fee_paid_str = "Yes"
        elif fee_paid == "False":
            fee_paid_str = "No"
        else:
            fee_paid_str = self.__fee_paid

        canceled_date = str(self.__cancellation_date)
        if canceled_date == "0000-00-00":
            canceled_date_str = ""
        else:
            canceled_date_str = "Team has been canceled participation on: " + canceled_date

        return f"Team ID: {self.__id}\nTeam Name: {self.__name}\nTeam Type: {type_str}\nFee (SEK): {self.__fee}\nFee Paid: {fee_paid_str} \n{canceled_date_str}"
