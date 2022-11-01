import helper
from concurrent.futures import ThreadPoolExecutor
import time

#command_pool = [helper.home(1, 0), helper.home(2, 0), helper.get_pos(1), helper.get_pos(2)]

#number_of_commands = len(command_pool)

#delay = 2


#with ThreadPoolExecutor(max_workers=number_of_commands) as pool:
#    for number in number_of_commands:
#        pool.submit(helper.get_url, command_pool[number])
#        time.sleep(delay)

while(1):
    input_command = input("Enter command:")

    if input_command == 'home all':
        commands = helper.home_all()

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(helper.get_url, commands[command])

    elif input_command == 'home axis':
        axis = input('Enter axis:')

        commands = helper.home_axis(axis.upper())

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(helper.get_url, commands[command])

    elif input_command == 'move axis to':
        axis = input("Enter axis:")
        value = input("Enter Value:")

        commands = helper.move_axis_to(axis.upper(), str(value))

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(helper.get_url, commands[command])

    elif input_command == 'set maximum velocity and acceleration':
        print('\nH: V=300, A=1500\nI: V=300, A =1500\nJ: V=300, A=1500\nK: V=3, A=200\nL: V=3, A=150\nX: V=300, A=1500\nY: V=300, A=1500\nN: V=3, A=150\n')
        velocity = input("Enter Velocity:")
        acceleration = input("Enter Acceleration")

        commands = helper.set_max_vel_accel(str(velocity), str(acceleration))

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(helper.get_url, commands[command])

    # complete this shit later
    if input_command == 'move wire to safe position':
        commands = helper.move_wire_to_safe_position()

        with ThreadPoolExecutor(max_workers=len(commands)) as pool:
            for command in range(0, len(commands)):
                pool.submit(helper.get_url, commands[command])
                time.sleep(2)

