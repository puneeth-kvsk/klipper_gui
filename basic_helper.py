import low_level_functions as low_level

home_axis_command = 'G28'
absolute_position_command = 'G90'
relative_position_command = 'G91'
move_axis_command = 'G1F12000'
get_current_position = 'M114'
endstop_status = 'M119'


# Position Fetching Function
def get_current_positions_all():
    command_pool = [low_level.gcodeUrl + get_current_position]
    return command_pool


# HOMING COMMANDS


# Home axis
def home_axis(axis):
    command_pool = []
    command_pool.extend(low_level.set_max_vel_accel_auto(axis))
    command_pool.append(low_level.gcodeUrl + home_axis_command + axis)
    # Adjust slide angle to perfect horizontal while homing
    if axis == 'J':
        command_pool.extend(move_axis_to('J', 0))
    return command_pool


# HOMING COMMANDS END

# AXIS MOVEMENT COMMANDS


# Move axis to
def move_axis_to(axis, value):
    command_pool = []
    #command_pool.extend(low_level.set_vel_accel_auto(str(axis)))
    command_pool.extend(low_level.set_max_vel_accel_manual())
    if axis == 'J':
        command_pool.extend([low_level.gcodeUrl + absolute_position_command, low_level.gcodeUrl + move_axis_command + axis + str(value + 30)])
    else:
        command_pool.extend([low_level.gcodeUrl + absolute_position_command, low_level.gcodeUrl + move_axis_command + axis + str(value)])
    return command_pool


# Move axis forward by
def move_axis_forward_by(axis, value):
    command_pool = []
    command_pool.extend(low_level.set_max_vel_accel_auto(str(axis)))
    command_pool.extend([low_level.gcodeUrl + relative_position_command, low_level.gcodeUrl + move_axis_command + axis + str(value)])
    return command_pool


# Move axis backward by
def move_axis_backward_by(axis, value):
    command_pool = []
    command_pool.extend(low_level.set_max_vel_accel_auto(str(axis)))
    command_pool.extend([low_level.gcodeUrl + relative_position_command, low_level.gcodeUrl + move_axis_command + axis + str(value)])
    return command_pool


# Move multiple axes to
def move_multiple_axes_to(params):
    command_pool = []

    for key in params:
        command_pool.extend(low_level.set_max_vel_accel_auto(key))
        break

    command_pool.append(low_level.gcodeUrl + move_axis_command)
    for key, value in params.items():
        if key == 'J':
            command_pool[2] += key + str(int(value) + 30)
        else:
            command_pool[2] += key + str(value)
    return command_pool

