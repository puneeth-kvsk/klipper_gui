import helper
import api_calls
from concurrent.futures import ThreadPoolExecutor
import time

while 1:
    input_command = input("Enter command:")

    if input_command == 'home axis':
        axis = input('Enter axis:')

        commands = helper.home_axis(axis.upper())

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])
                time.sleep(0.01)

    elif input_command == 'home all':
        commands = helper.home_all()

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])
                time.sleep(0.01)

    elif input_command == 'move slide basic':
        commands = api_calls.move_slide_in_2d_plane(50, 50)

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])
                #time.sleep(0.01)

    elif input_command == 'move axis to':
        axis = input("Enter axis:")
        value = input("Enter Value:")

        commands = helper.move_axis_to(axis.upper(), str(value))

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])

    # this can be removed because it might not be used
    elif input_command == 'set maximum velocity and acceleration':
        print('\nH: V=300, A=1500\nI: V=300, A =1500\nJ: V=300, A=1500\nK: V=3, A=200\nL: V=3, A=150\nX: V=300, A=1500\nY: V=300, A=1500\nN: V=3, A=150\n')
        velocity = input("Enter Velocity:")
        acceleration = input("Enter Acceleration")

        commands = helper.set_max_vel_accel(str(velocity), str(acceleration))

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])

    # complete this shit later
    if input_command == 'move wire to safe position':
        commands = helper.move_wire_to_safe_position()

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])
                time.sleep(2)

    elif input_command == 'move wire to':
        #axis = input("Enter axis:")
        value = input("Enter Value:")

        commands = helper.move_wire_to(str(value))

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(api_calls.get_url, commands[command])


