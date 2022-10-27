import helper
from concurrent.futures import ThreadPoolExecutor
import time

command_pool = [helper.home(1, 0), helper.home(2, 0), helper.get_pos(1), helper.get_pos(2)]

number_of_commands = len(command_pool)

delay = 2


with ThreadPoolExecutor(max_workers=number_of_commands) as pool:
    for number in number_of_commands:
        pool.submit(helper.get_url, command_pool[number])
        time.sleep(delay)
