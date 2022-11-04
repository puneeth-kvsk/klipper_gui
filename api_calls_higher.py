import basic_helper
import individual_commands
import api_calls_lower


# Take section process
def take_sections(thickness, counts):
    command_pool = []
    for count in range(0, counts):
        command_pool.extend(individual_commands.rotate_fly_wheel(1)) # Number of rotations hardcoded to 1
        command_pool.extend(individual_commands.move_block_towards_blade(thickness))
    return command_pool


# Tissue Teardown process
def teardown():
    command_pool = []
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())
    command_pool.extend(api_calls_lower.move_wire_gantry_to_dip_pos())
    command_pool.extend(api_calls_lower.move_wire_gantry_to_preteardown_pos())
    command_pool.extend(api_calls_lower.move_wire_gantry_to_postteardown_pos())
    return command_pool


# Slide pickup process
def slide_pickup():
    command_pool = []
    command_pool.extend(api_calls_lower.move_slide_to_pickup_position())
    command_pool.extend(basic_helper.delay_func(4000))
    command_pool.extend(api_calls_lower.move_slide_to_pivot_position())
    command_pool.extend(basic_helper.delay_func(4000))
    command_pool.extend(api_calls_lower.move_slide_to_final_position())
    return command_pool



#

