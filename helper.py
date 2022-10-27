import requests

http_link = 'http://192.168.29.157:'
printer1 = '7125'
printer2 = '7126'

X = 'X'
Y = 'Y'
Z = 'Z'

gcodeUrl = '/printer/gcode/script?script='
printerInformationUrl = '/printer/info'

home_axis_command = 'G28'
move_axis_command = 'G1'
get_current_position = 'M114'
endstop_status = 'M119'


def get_url(url):
    return requests.post(url)


# Home printer's axes
# 0:X axis, 1:Y axis, 2:Z axis, 3:All Axes
def home(printer, axis):
    if printer == 1:
        if axis == 0:
            return http_link + printer1 + gcodeUrl + home_axis_command + X
        if axis == 1:
            return http_link + printer1 + gcodeUrl + home_axis_command + Y
        if axis == 2:
            return http_link + printer1 + gcodeUrl + home_axis_command + Z
        if axis == 3:
            return http_link + printer1 + gcodeUrl + home_axis_command + X + Y + Z

    if printer == 2:
        if axis == 0:
            return http_link + printer2 + gcodeUrl + home_axis_command + X
        if axis == 1:
            return http_link + printer2 + gcodeUrl + home_axis_command + Y
        if axis == 2:
            return http_link + printer2 + gcodeUrl + home_axis_command + Z
        if axis == 3:
            return http_link + printer2 + gcodeUrl + home_axis_command + X + Y + Z


# Get Printer's motor positions
def get_pos(printer):
    if printer == 1:
        return http_link + printer1 + gcodeUrl + get_current_position

    if printer == 2:
        return http_link + printer2 + gcodeUrl + get_current_position
