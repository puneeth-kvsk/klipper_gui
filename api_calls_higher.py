import basic_helper
import individual_commands
import api_calls_lower


# Execute Commands
def execute_commands(my_list):
    api_calls_lower.execute_urls(my_list, 0.05)


# Take section process
def take_sections(thickness, counts):
    command_pool = []
    for count in range(0, counts):
        command_pool.extend(individual_commands.rotate_fly_wheel(1))  # Number of rotations hardcoded to 1
        command_pool.extend(individual_commands.move_block_towards_blade(thickness))
    return command_pool


# First Tissue Pickup
def first_tissue_pickup():
    command_pool = []
    command_pool.extend(api_calls_lower.move_slide_to_first_pickup_position())      # Move slide to first pickup position    
    command_pool.extend(api_calls_lower.move_wire_gantry_to_dip_pos())              # Move wire gantry to dip position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_preteardown_pos())      # Move wire gantry to preteardown position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_postteardown_pos())     # Move wire gantry to postteardown position
    command_pool.extend(basic_helper.delay_func(1000))                              # Delay  of 1 second
    command_pool.extend(api_calls_lower.hot_pool_gate_open())                       # Open hot pool gate
    command_pool.extend(basic_helper.delay_func(1000))                              # Delay  of 1 second
    command_pool.extend(api_calls_lower.move_wire_gantry_to_first_pickup_pos())
    command_pool.extend(api_calls_lower.hot_pool_gate_close())
    command_pool.extend(api_calls_lower.move_slide_to_first_pivot_position())
    command_pool.extend(api_calls_lower.burn_wire(1000))
    command_pool.extend(api_calls_lower.move_slide_to_first_final_position())
    command_pool.extend(basic_helper.delay_func(1000))
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())
    command_pool.extend(basic_helper.delay_func(1000))
    return command_pool


# Second Tissue Pickup
def second_tissue_pickup():
    command_pool = []
    command_pool.extend(api_calls_lower.move_slide_to_second_pickup_position())      # Move slide to first pickup position    
    command_pool.extend(api_calls_lower.move_wire_gantry_to_dip_pos())              # Move wire gantry to dip position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_preteardown_pos())      # Move wire gantry to preteardown position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_postteardown_pos())     # Move wire gantry to postteardown position
    command_pool.extend(basic_helper.delay_func(1000))                              # Delay  of 1 second
    command_pool.extend(api_calls_lower.hot_pool_gate_open())                       # Open hot pool gate
    command_pool.extend(basic_helper.delay_func(1000))                              # Delay  of 1 second
    command_pool.extend(api_calls_lower.move_wire_gantry_to_second_pickup_pos())
    command_pool.extend(api_calls_lower.hot_pool_gate_close())
    command_pool.extend(api_calls_lower.move_slide_to_second_pivot_position())
    command_pool.extend(api_calls_lower.burn_wire(1000))
    command_pool.extend(api_calls_lower.move_slide_to_second_final_position())
    command_pool.extend(basic_helper.delay_func(1000))
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())
    command_pool.extend(basic_helper.delay_func(1000))
    return command_pool


# Discard Pump
def discard_tissue():
    command_pool = []
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())  # Move wire gantry to safe position
    command_pool.extend(api_calls_lower.discard_pump_actuation())        # Discard pump on and off
    return command_pool
