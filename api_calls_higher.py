import basic_helper
import individual_commands
import api_calls_lower


# Take section process
def take_sections(thickness, counts):
    command_pool = []
    for count in range(0, counts):
        command_pool.extend(individual_commands.rotate_fly_wheel(1))  # Number of rotations hardcoded to 1
        command_pool.extend(individual_commands.move_block_towards_blade(thickness))
    return command_pool


# Tissue Teardown phase 1
def teardown_phase_one():
    command_pool = []
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())          # Move wire gantry to safe position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_dip_pos())           # Move wire gantry to dip position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_preteardown_pos())   # Move wire gantry to preteardown position
    command_pool.extend(api_calls_lower.move_wire_gantry_to_postteardown_pos())  # Move wire gantry to postteardown position
    return command_pool


# Tissue Teardown phase 2
def teardown_phase_two():
    command_pool = []
    delay = input("Enter wire burn time:")
    command_pool.extend(api_calls_lower.hot_pool_gate_open())                    # Open pool gate
    command_pool.extend(api_calls_lower.move_wire_gantry_to_slide_pickup_pos())  # Move wire gantry to slide pickup position
    command_pool.extend(api_calls_lower.move_slide_to_pivot_position())          # Pivot slide
    command_pool.extend(api_calls_lower.burn_wire(delay))                        # Burn wire
    command_pool.extend(api_calls_lower.move_slide_to_final_position())          # Pickup slide
    return command_pool


# Final process
def final_process():
    command_pool = []
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())  # Move wire gantry to safe position
    command_pool.extend(api_calls_lower.hot_pool_gate_close())           # Close pool gate
    command_pool.extend(api_calls_lower.move_slide_to_final_position())  # Move slide to final position
    return command_pool


# Discard Pump
def discard_tissue():
    command_pool = []
    command_pool.extend(api_calls_lower.move_wire_gantry_to_safe_pos())  # Move wire gantry to safe position
    command_pool.extend(api_calls_lower.discard_pump_actuation())        # Discard pump on and off
    return command_pool
