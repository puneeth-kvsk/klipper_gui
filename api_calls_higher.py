import individual_commands
import api_calls_lower


# Take sections
def take_sections(thickness, counts):
    command_pool = []
    for count in range(0, counts):
        command_pool.extend(individual_commands.rotate_fly_wheel(1)) # Number of rotations hardcoded to 1
        command_pool.extend(individual_commands.move_block_towards_blade(thickness))
    return command_pool


# Move wire gantry to safe position
def move_wire_gantry_to_safe_pos():
    command_pool = []
    command_pool.extend(api_calls_lower.move_wire_gantry_to(95, 12))
    #print(command_pool)
    return command_pool


#

