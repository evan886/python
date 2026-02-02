from  helper import validate_and_execute,user_input_message
import  logging
import  os
logger = logging.getLogger("MAIN")
logger.error("Err occurred in the app")


# print(os.name)

user_input = ""
while user_input != "exit":
    user_input= input(user_input_message)
    days_and_unit = user_input.split(":")
    # print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
    validate_and_execut(days_and_unit_dictionary) #because impor va---
    #helper.validate_and_execut(days_and_unit_dictionary)
    # validate_and_execute()