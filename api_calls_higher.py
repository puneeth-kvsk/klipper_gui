import individual_commands


# Take sections
def take_sections(thickness, counts):
    command_pool = []
    for count in range(0, counts):
        command_pool.extend(individual_commands.rotate_fly_wheel(1)) # Number of rotations hardcoded to 1
        command_pool.extend(individual_commands.move_block_towards_blade(thickness))
    return command_pool
