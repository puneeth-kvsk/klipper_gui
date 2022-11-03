import basic_helper

# HIGHER LEVEL CALLS

# MOVE WIRE GANTRY CALLS

# MOVE WIRE - create example for each


# Move Wire to
def move_wire_to(value):
    command_pool = basic_helper.move_axis_to('Y', value)
    return command_pool


# Move Wire Up by
def move_wire_up_by(value):
    command_pool = basic_helper.move_axis_backward_by('Y', value)
    return command_pool


# Move Wire Down by
def move_wire_down_by(value):
    command_pool = basic_helper.move_axis_forward_by('Y', value)
    return command_pool


# MOVE WIRE END


# MOVE GANTRY

# Move Gantry to
def move_gantry_to(value):
    command_pool = basic_helper.move_axis_to('X', value)
    return command_pool


# Move Gantry Forward by - towards blade
def move_gantry_forward_by(value):
    command_pool = basic_helper.move_axis_forward_by('X', value)
    return command_pool


# Move Gantry Backward to - away from blade
def move_gantry_backward_by(value):
    command_pool = basic_helper.move_axis_backward_by('X', value)
    return command_pool

# MOVE GANTRY END

# MOVE SLIDE GANTRY


# Move slide gantry to
def move_slide_gantry_to(value):
    command_pool = basic_helper.move_axis_to('H', value)
    return command_pool


# Move slide gantry forward by
def move_slide_gantry_forward_by(value):
    command_pool = basic_helper.move_axis_forward_by('H', value)
    return command_pool


# Move slide gantry backward by
def move_slide_gantry_backward_by(value):
    command_pool = basic_helper.move_axis_backward_by('H', value)
    return command_pool


# Move slide to
def move_slide_to(value):
    command_pool = basic_helper.move_axis_to('I', value)
    return command_pool


# Move slide up by
def move_slide_up_by(value):
    command_pool = basic_helper.move_axis_backward_by('I', value)
    return command_pool


# Move slide down by
def move_slide_down_by(value):
    command_pool = basic_helper.move_axis_forward_by('I', value)
    return command_pool


# Move slide angle to
def move_slide_angle_to(value):
    command_pool = basic_helper.move_axis_to('I', value + 30)  # Offset for slide angle is 30
    return command_pool


# Move slide angle up by
def move_slide_angle_up_by(value):
    command_pool = basic_helper.move_axis_backward_by('I', value)
    return command_pool


# Move slide angle down by
def move_slide_angle_down_by(value):
    command_pool = basic_helper.move_axis_forward_by('I', value)
    return command_pool


# FLY WHEEL COMMANDS


# Rotate Fly Wheel
def rotate_fly_wheel(count):
    command_pool = basic_helper.move_axis_forward_by('K', count * 10)  # Fly wheel to motor rotation is of ratio 1:10
    return command_pool


# BLOCK COMMANDS


# Move block towards blade by
def move_block_towards_blade(value):
    command_pool = basic_helper.move_axis_forward_by('L', value)
    return command_pool


# Move block away from blade
def move_block_away_from_blade(value):
    command_pool = basic_helper.move_axis_backward_by('L', value)
    return command_pool
