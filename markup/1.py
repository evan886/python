

# def days_to_units(num_of_days,conversion_unit):
#     if conversion_unit == "hours":
#      return f"{num_of_days} days are {num_of_days * 24} hours"
#     elif conversion_unit == "minutes":
#         return f"{num_of_days} days are {num_of_days * 24 * 60} hours"
#     else:
#         return "unsupported unit"


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



# user_input = ""
# while user_input != "exit":
#     user_input= input("hey enter a number of days and conversion unit \n")
#     days_and_unit = user_input.split(":")
#     # print(days_and_unit)
#     days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
#     print(days_and_unit_dictionary)
#     validate_and_execute()

#
# my_list =["20","30","100"]
# print(my_list[2])
#
# my_dictionary = {"days":20 , "unit": "hours","msg" : "all"}
#
# print(my_dictionary["msg"])
    # for num_of_days_element in user_input.split(","):
    #     validate_and_execute()


# # # print(f"{2*3}") indented
# def evan(nday):
#     # if nday > 0:
#     # # if nday > 0:
#     return f"{nday} from evan funciton"
#     # elif nday == 0:
#     #     return "you enter a  0 here"
#     # else:
#     #     return "no conversin for you"
#
# # print(my_var)
# def val():
#     if user_input.isdigit():
#         if user_input > 0:
#             my_var = evan(int(user_input))
#             print(my_var)
#         elif user_input == 0:
#             print('you enter a  0 here')
#     else:
#         print("your input is not a no.")
#
# user_input = input("hey enter a number \n")
# val()


# user_input1 = int(user_input)
# my_var = evan(int(user_input))
# print(my_var)

#
# print(user_input)

#variable
#var1 =  4 * 5
# print(f"{var1}")
#
# print(var1)