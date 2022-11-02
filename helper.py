import low_level_functions as hal

home_axis_command = 'G28'
absolute_position_command = 'G90'
relative_position_command = 'G91'
move_axis_command = 'G1'
get_current_position = 'M114'
endstop_status = 'M119'


# Position Fetching Function
def get_current_positions_all():
    command_pool = [hal.gcodeUrl + get_current_position]
    return command_pool


# HOMING COMMANDS


# Home axis
def home_axis(axis):
    command_pool = [None]
    command_pool.extend(hal.set_vel_accel_auto(axis))
    command_pool.append(hal.gcodeUrl + home_axis_command + axis)
    # Adjust slide angle to perfect horizontal while homing
    if axis == 'J':
        command_pool.append(move_axis_to('J', 30))
    return command_pool


# Home all
def home_all():
    command_pool = [None]
    command_pool.extend(home_axis('I'))
    command_pool.extend(home_axis('H'))
    command_pool.extend(home_axis('J'))
    command_pool.extend(home_axis('Y'))
    command_pool.extend(home_axis('X'))
    command_pool.extend(home_axis('N'))
    command_pool.extend(home_axis('K'))
    return command_pool

# HOMING COMMANDS END

# AXIS MOVEMENT COMMANDS


# Move axis to
def move_axis_to(axis, value):
    command_pool = [None]
    command_pool.extend(hal.set_vel_accel_auto(str(axis)))
    command_pool.extend([hal.gcodeUrl + absolute_position_command, hal.gcodeUrl + move_axis_command + axis + str(value)])
    return command_pool


# Move axis forward by
def move_axis_forward_by(axis, value):
    command_pool = [None]
    command_pool.extend(hal.set_vel_accel_auto(str(axis)))
    command_pool.extend([hal.gcodeUrl + relative_position_command, hal.gcodeUrl + move_axis_command + axis + str(value)])
    return command_pool


# Move axis backward by
def move_axis_backward_by(axis, value):
    command_pool = [None]
    command_pool.extend(hal.set_vel_accel_auto(str(axis)))
    command_pool.extend([hal.gcodeUrl + relative_position_command, hal.gcodeUrl + move_axis_command + axis + str(value)])
    return command_pool


# Move multiple axes to
def move_multiple_axes_to(params):
    command_pool = [None]

    for key in params:
        command_pool.extend(hal.set_vel_accel_auto(key))
        break

    command_pool.append(hal.gcodeUrl + move_axis_command)
    for key, value in params.items():
        command_pool[2] += key + str(value)
    print(command_pool)
    return command_pool

# HIGHER LEVEL CALLS

# MOVE WIRE GANTRY CALLS

# MOVE WIRE - create example for each

# Move Wire to
def move_wire_to(value):
    command_pool = move_axis_to('Y', value)
    return command_pool


# Move Wire Up by
def move_wire_up_by(value):
    command_pool = move_axis_backward_by('Y', value)
    return command_pool


# Move Wire Down by
def move_wire_down_by(value):
    command_pool = move_axis_forward_by('Y', value)
    return command_pool


# MOVE WIRE END


# MOVE GANTRY

# Move Gantry to
def move_gantry_to(value):
    command_pool = move_axis_to('X', value)
    return command_pool


# Move Gantry Forward by - towards blade
def move_gantry_forward_by(value):
    command_pool = move_axis_forward_by('X', value)
    return command_pool


# Move Gantry Backward to - away from blade
def move_gantry_backward_by(value):
    command_pool = move_axis_backward_by('X', value)
    return command_pool

# MOVE GANTRY END

# MOVE SLIDE GANTRY


# Move slide gantry to
def move_slide_gantry_to(value):
    command_pool = move_axis_to('H', value)
    return command_pool


# Move slide gantry forward by
def move_slide_gantry_forward_by(value):
    command_pool = move_axis_forward_by('H', value)
    return command_pool


# Move slide gantry backward by
def move_slide_gantry_backward_by(value):
    command_pool = move_axis_backward_by('H', value)
    return command_pool


# Move slide to
def move_slide_to(value):
    command_pool = move_axis_to('I', value)
    return command_pool


# Move slide up by
def move_slide_up_by(value):
    command_pool = move_axis_backward_by('I', value)
    return command_pool


# Move slide down by
def move_slide_down_by(value):
    command_pool = move_axis_forward_by('I', value)
    return command_pool


# Move slide angle to
def move_slide_angle_to(value):
    command_pool = move_axis_to('I', value+30)  # Offset for slide angle is 30
    return command_pool


# Move slide angle up by
def move_slide_angle_up_by(value):
    command_pool = move_axis_backward_by('I', value)
    return command_pool


# Move slide angle down by
def move_slide_angle_down_by(value):
    command_pool = move_axis_forward_by('I', value)
    return command_pool


# FLY WHEEL COMMANDS


# Rotate Fly Wheel
def rotate_fly_wheel(count):
    command_pool = move_axis_forward_by('K', count*10)  # Fly wheel to motor rotation is of ratio 1:10
    return command_pool


# BLOCK COMMANDS


# Move block towards blade by
def move_block_towards_blade(value):
    command_pool = move_axis_forward_by('L', value)
    return command_pool


# Move block away from blade
def move_block_away_from_blade(value):
    command_pool = move_axis_backward_by('L', value)
    return command_pool
