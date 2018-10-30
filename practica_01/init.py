# run this file to start the calculator

#     _____      _            _       _
#    / ____|    | |          | |     | |
#   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __
#   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
#   | |___| (_| | | (__| |_| | | (_| | || (_) | |
#    \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
#       by Carlos Escalante
#

import operaciones_matematicas as OM
import util as u
import properties as prop

API = OM.init_operations_dictionary()
API['sum'] = API['suma']
# TODO: Continue adding aliases to improve UX

exit_signal = False
user_input = None
operacion_seleccionada = None
counter = 0
operando1 = 0
operando2 = 0

u.print_welcome_message()

while exit_signal != True:
    message = prop.first_question if counter == 0 else prop.ask_question_again
    user_input = str(input(u.bgcolors.OKBLUE + message + u.bgcolors.ENDC))
    counter = 1

    if user_input in prop.truthy_values:  # user wants to exit the program
        operacion_seleccionada = input(prop.ask_for_operation)

        while operacion_seleccionada not in API:
            u.print_error(prop.key_error_message)
            operacion_seleccionada = input(prop.ask_for_operation)
        else:
            operando1 = int(input("Digite numero 1: \n"))
            operando2 = int(input("Digite numero 2: \n"))

        try:
            result = API[operacion_seleccionada](operando1, operando2)
            u.print_success(f"Seleccionó: {operacion_seleccionada}")
            print(f"El Resultado es {result} \n")
        except ZeroDivisionError:
            u.print_error(prop.zero_division_message)
        except KeyError:
            u.print_error(prop.key_error_message)

    else:  # user wants to exit
        exit_signal = True
        u.print_error("Hasta luego, lo esperamos de vuelta!")




