import requests

http_link = 'http://192.168.6.228:'
printer1 = '7125'
printer2 = '7126'

X = 'X'
Y = 'Y'
Z = 'Z'

gcodeUrl = 'http://192.168.6.228:7125/printer/gcode/script?script='

printerInformationUrl = '/printer/info'

home_axis_command = 'G28'
move_axis_command = 'G1'
get_current_position = 'M114'
endstop_status = 'M119'


def get_url(url):
    return requests.post(url)


# Home printer's axes
# 0:X axis, 1:Y axis, 2:Z axis, 3:All Axes
def home():
    command_pool = [gcodeUrl + 'G28Y', gcodeUrl + 'G28X', gcodeUrl + 'G28H', gcodeUrl + 'G28I', gcodeUrl + 'G28J']
    return command_pool


def move_wire_to_safe_position():
    command_pool = [gcodeUrl + 'G90', gcodeUrl + 'G1Y0F12000', gcodeUrl + 'G1X70F12000']
    return command_pool


# Get Printer's motor positions
def get_pos(printer):
    if printer == 1:
        return http_link + printer1 + gcodeUrl + get_current_position

    if printer == 2:
        return http_link + printer2 + gcodeUrl + get_current_position
