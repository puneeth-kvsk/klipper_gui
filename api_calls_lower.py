import requests
import basic_helper
from concurrent.futures import ThreadPoolExecutor
import time


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


# Home Wire Gantry
def home_wire_gantry():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('Y'))
    command_pool.extend(basic_helper.home_axis('X'))
    return command_pool


# Home Slide gantry
def home_slide_gantry():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('I'))
    command_pool.extend(basic_helper.home_axis('H'))
    command_pool.extend(basic_helper.home_axis('J'))
    return command_pool


# Home Flywheel and Block
def home_flywheel_and_block():
    command_pool = []
    command_pool.extend(basic_helper.home_axis('N'))
    command_pool.extend(basic_helper.home_axis('K'))
    return command_pool


# Move slide gantry
def move_slide_gantry_to(h_value, i_value, j_value):
    params = {'H': h_value, 'I': i_value, 'J': j_value}
    command_pool = basic_helper.move_multiple_axes_to(params)
    return command_pool


# Move Wire Gantry
def move_wire_gantry_to(x_value, y_value):
    params = {'Y': y_value, 'X': x_value}
    command_pool = basic_helper.move_multiple_axes_to(params)
    return command_pool



