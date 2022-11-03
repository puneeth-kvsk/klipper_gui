import low_level_functions
import basic_helper
import api_calls_lower
from concurrent.futures import ThreadPoolExecutor
import time

while 1:
    input_command = input("Enter command:")

    if input_command == 'home axis':
        axis = input('Enter axis:')

        commands = basic_helper.home_axis(axis.upper())
        api_calls_lower.execute_urls(commands, 0)

    elif input_command == 'home multiple':
        axes = input("Enter the axes to home:")

        commands = api_calls_lower.home_multiple(axes)
        api_calls_lower.execute_urls(commands, 0)

    elif input_command == 'home all':
        commands = api_calls_lower.home_all()
        api_calls_lower.execute_urls(commands, 0)

    elif input_command == 'home wire gantry':
        commands = api_calls_lower.home_wire_gantry()
        api_calls_lower.execute_urls(commands, 0.01)

    elif input_command == 'home slide gantry':
        commands = api_calls_lower.home_slide_gantry()
        api_calls_lower.execute_urls(commands, 0.01)

    elif input_command == 'home flywheel and block':
        commands = api_calls_lower.home_flywheel_and_block()
        api_calls_lower.execute_urls(commands, 0.01)

    elif input_command == 'move axis to':
        axis = input("Enter axis:")
        value = input("Enter Value:")

        commands = basic_helper.move_axis_to(axis.upper(), str(value))
        api_calls_lower.execute_urls(commands, 0)

    elif input_command == 'move slide gantry':
        h_value = input("Enter H move distance:")
        i_value = input("Enter I move distance:")
        j_value = input("Enter J move distance:")

        commands = api_calls_lower.move_slide_gantry_to(h_value, i_value, j_value)
        api_calls_lower.execute_urls(commands, 0)

    elif input_command == 'move wire gantry':
        y_value = input("Enter Y move distance:")
        x_value = input("Enter X move distance:")

        commands = api_calls_lower.move_wire_gantry_to(y_value, x_value)
        api_calls_lower.execute_urls(commands, 0)

    else:
        print("Entered Command does not exist!")
