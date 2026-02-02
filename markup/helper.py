def days_to_units(num_of_days,conversion_unit):
    if conversion_unit == "hours":
     return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} hours"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        #  we want to  do conversion
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculation_value)
        elif user_input_number == 0:
            print("your enterd a 0")
        else:
            print("you entered a negative number. ")
    except ValueError:
        print(" your input is not a valid number")

user_input_message = "Hey ,user, enter number of days adn conversion unit \n"







