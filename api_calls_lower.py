import requests
import basic_helper
import low_level_functions
from concurrent.futures import ThreadPoolExecutor
import time

hot_pool_gate_open_angle = 35
hot_pool_gate_close_angle = 135

# Fetch URL
def get_url(url):
    return requests.post(url)


# Execute URLs
def execute_urls(commands, delay):
    with ThreadPoolExecutor(max_workers=len(commands)) as pool:
        for command in range(0, len(commands)):
            pool.submit(get_url, commands[command])
            time.sleep(delay)


# Home all
def home_all():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('I'))
    command_pool.extend(basic_helper.home_axis('H'))
    command_pool.extend(basic_helper.home_axis('J'))
    command_pool.extend(basic_helper.home_axis('Y'))
    command_pool.extend(basic_helper.home_axis('X'))
    command_pool.extend(basic_helper.home_axis('N'))
    command_pool.extend(basic_helper.home_axis('K'))
    return command_pool


# Home multiple
def home_multiple(axes):
    command_pool = []
    for axis in range(0, len(axes)):
        command_pool.extend(basic_helper.home_axis(axes[axis].upper()))
    return command_pool


# SLIDE GANTRY ROUTINES
# Home Slide gantry
def home_slide_gantry():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('I'))
    command_pool.extend(basic_helper.home_axis('H'))
    command_pool.extend(basic_helper.home_axis('J'))
    return command_pool


# Move slide gantry
def move_slide_gantry_to(h_value, i_value, j_value):
    params = {'H': h_value, 'I': i_value, 'J': j_value}
    command_pool = basic_helper.move_multiple_axes_to(params)
    return command_pool


# Move slide to pickup position
def move_slide_to_pickup_position():
    command_pool = []
    command_pool.extend(move_slide_gantry_to(190, 110, 30))
    return command_pool


# Move slide to pivot position
def move_slide_to_pivot_position():
    command_pool = []
    command_pool.extend(move_slide_gantry_to(200.498, 95.007, 40))
    return command_pool


# Move slide to final position
def move_slide_to_final_position():
    command_pool = []
    command_pool.extend(move_slide_gantry_to(185.177, 82.1515, 40))
    return command_pool
# SLIDE GANTRY ROUTINES END


# FLYWHEEL ROUTINES
# Home Flywheel and Block
def home_flywheel_and_block():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('N'))
    command_pool.extend(basic_helper.home_axis('K'))
    return command_pool
# FLYWHEEL ROUTINES END


# WIRE GANTRY ROUTINES
# Home Wire Gantry
def home_wire_gantry():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('Y'))
    command_pool.extend(basic_helper.home_axis('X'))
    return command_pool


# Move Wire Gantry
def move_wire_gantry_to(x_value, y_value):
    params = {'Y': y_value, 'X': x_value}
    command_pool = basic_helper.move_multiple_axes_to(params)
    return command_pool


# Move wire gantry to safe position
def move_wire_gantry_to_safe_pos():
    command_pool = []
    command_pool.extend(move_wire_gantry_to(95, 12))
    return command_pool


# Move wire gantry to dip position
def move_wire_gantry_to_dip_pos():
    command_pool = []
    command_pool.extend(move_wire_gantry_to(118,21))
    return command_pool


# Move wire gantry to pre-teardown position
def move_wire_gantry_to_preteardown_pos():
    command_pool = []
    command_pool.extend(move_wire_gantry_to(131, 15.5))
    return command_pool


# Move wire gantry to post-teardown process
def move_wire_gantry_to_postteardown_pos():
    command_pool = []
    command_pool.extend(move_wire_gantry_to(131, 14.5))
    return command_pool


# Move wire gantry to slide pickup position
def move_wire_gantry_to_slide_pickup_pos():
    command_pool = []
    #command_pool.extend(move_wire_gantry_to(, ))  # To be filled with hardcoded values
    return command_pool

# WIRE GANTRY ROUTINES END


# POOL GATE ROUTINES
# Pool gate open
def hot_pool_gate_open():
    command_pool = []
    command_pool.extend(low_level_functions.gcodeUrl + 'SET_SERVO SERVO=config_name ANGLE=' + str(hot_pool_gate_open_angle))
    return command_pool


# Pool gate close
def hot_pool_gate_close():
    command_pool = []
    command_pool.extend(low_level_functions.gcodeUrl + 'SET_SERVO SERVO=config_name ANGLE=' + str(hot_pool_gate_close_angle))
    return command_pool


# Burn wire
def burn_wire(delay):
    command_pool = []
    command_pool.extend(low_level_functions.gcodeUrl + 'SET_PIN PIN=wire_power VALUE=1')
    command_pool.extend(basic_helper.delay_func(delay))
    command_pool.extend(low_level_functions.gcodeUrl + 'SET_PIN PIN=wire_power VALUE=0')
    return command_pool


# Discard Pump
def discard_pump_actuation():
    command_pool = []
    command_pool.extend(low_level_functions.gcodeUrl + basic_helper.pump_actuation_command + '120')
    command_pool.extend((basic_helper.delay_func(1000)))
    command_pool.extend(low_level_functions.gcodeUrl + basic_helper.pump_actuation_command + '0')
    return command_pool