import low_level_functions

home_axis_command = 'G28'
absolute_position_command = 'G90'
relative_position_command = 'G91'
delay_command = 'G4P'
move_axis_command = 'G1'
speed_12000 = 'F12000'
speed_2000 = 'F2000'
speed_3000 = 'F3000'
speed_6000 = 'F6000'
get_current_position_command = 'M114'
endstop_status_command = 'M119'
pump_actuation_command = 'M106S'


# Position Fetching Function
def get_current_positions_all():
    command_pool = [low_level_functions.gcodeUrl + get_current_position_command]
    return command_pool


# Delay Function
def delay_func(delay):
    command_pool = [low_level_functions.gcodeUrl + delay_command + str(delay)]
    return command_pool


# HOMING COMMANDS
# Home axis
def home_axis(axis):
    command_pool = []
    command_pool.extend(low_level_functions.set_max_vel_accel_auto(axis))
    command_pool.append(low_level_functions.gcodeUrl + home_axis_command + axis)
    # Adjust slide angle to perfect horizontal while homing
    if axis == 'J':
        command_pool.extend(move_axis_to('J', 0))
    return command_pool


# HOMING COMMANDS END

# AXIS MOVEMENT COMMANDS


# Move axis to
def move_axis_to(axis, value, speed):
    command_pool = []

    if speed == 2000:
        speed == speed_2000
    elif speed == 3000:
        speed == speed_3000
    elif speed == 6000:
        speed == speed_6000
    else:
        speed == speed_12000

    command_pool.extend(low_level_functions.set_max_vel_accel_auto(str(axis)))
    if axis == 'J':
        command_pool.extend([low_level_functions.gcodeUrl + absolute_position_command, low_level_functions.gcodeUrl + move_axis_command + speed + axis + str(value + 30)])
    else:
        command_pool.extend([low_level_functions.gcodeUrl + absolute_position_command, low_level_functions.gcodeUrl + move_axis_command + speed + axis + str(value)])
    return command_pool


# Move axis forward by
def move_axis_forward_by(axis, value, speed):
    command_pool = []

    if speed == 2000:
        speed == speed_2000
    elif speed == 3000:
        speed == speed_3000
    elif speed == 6000:
        speed == speed_6000
    else:
        speed == speed_12000
        
    command_pool.extend(low_level_functions.set_max_vel_accel_auto(str(axis)))
    command_pool.extend([low_level_functions.gcodeUrl + relative_position_command, low_level_functions.gcodeUrl + move_axis_command + speed + axis + str(value)])
    return command_pool


# Move axis backward by
def move_axis_backward_by(axis, value, speed):
    command_pool = []

    if speed == 2000:
        speed == speed_2000
    elif speed == 3000:
        speed == speed_3000
    elif speed == 6000:
        speed == speed_6000
    else:
        speed == speed_12000

    command_pool.extend(low_level_functions.set_max_vel_accel_auto(str(axis)))
    command_pool.extend([low_level_functions.gcodeUrl + relative_position_command, low_level_functions.gcodeUrl + move_axis_command + speed + axis + str(value)])
    return command_pool


# Move multiple axes to
def move_multiple_axes_to(params, speed):
    command_pool = []

    if speed == 2000:
        speed == speed_2000
    elif speed == 3000:
        speed == speed_3000
    elif speed == 6000:
        speed == speed_6000
    else:
        speed == speed_12000

    for key in params:
        command_pool.extend(low_level_functions.set_max_vel_accel_auto(key))
        break

    command_pool.append(low_level_functions.gcodeUrl + move_axis_command + speed)
    for key, value in params.items():
        if key == 'J':
            command_pool[2] += key + str(int(value) + 30)
        else:
            command_pool[2] += key + str(value)
    return command_pool

