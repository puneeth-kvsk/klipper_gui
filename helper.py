import requests

http_link = 'http://192.168.6.228:'
printer1 = '7125'
printer2 = '7126'

X = 'X'
Y = 'Y'
Z = 'Z'

gcodeUrl = 'http://192.168.6.228:7125/printer/gcode/script?script='

printerInfoUrl = 'http://192.168.6.228:7125/printer/info'

speedSettingUrl = gcodeUrl + 'SET_VELOCITY_LIMIT VELOCITY='

accelerationSettingUrl = gcodeUrl + 'M204S'

#gcodeUrl = 'http://192.168.6.228:7125/printer/gcode/script?script=G90'


home_axis_command = 'G28'
absolute_position_command = 'G90'
relative_position_command = 'G91'
move_axis_command = 'G1'
get_current_position = 'M114'
endstop_status = 'M119'

axis_accel_values = {'h': 1500, 'i': 1500, 'j': 1500, 'k': 200, 'l': 150, 'x': 1500, 'y': 1500, 'n': 150}
axis_vel_values = {'h': 300, 'i': 300, 'j': 300, 'k': 3, 'l': 3, 'x': 300, 'y': 300, 'n': 3}


# Fetch URL
def get_url(url):
    return requests.post(url)

# VELOCITY MACROS

# Velocity Setting
def m201(value):
    command_pool = [speedSettingUrl + value]
    return command_pool


# Acceleration Setting
def m204(value):
    command_pool = accelerationSettingUrl + value
    return command_pool


# Set maximum velocity and acceleration value for axis
def set_max_vel_accel(velocity, acceleration):
    command_pool = [m201(velocity), m204(acceleration)]
    return command_pool


# Set max accel value (used for homing)
def set_max_accel(axis):
    value = axis_accel_values.get(axis)
    return m204(value)

# VELOCITY MACROS END

# HOMING COMMANDS


# Home axis
def home_axis(axis):
    command_pool = [set_max_accel(axis), gcodeUrl + home_axis_command + axis]
    return command_pool


# Home all
def home_all():
    command_pool = [home_axis('I'), home_axis('H'), home_axis('J'), home_axis('Y'), home_axis('X'), home_axis('N'), home_axis('K')]
    return command_pool

# HOMING COMMANDS END

# AXIS MOVEMENT COMMANDS


# Move axis to
def move_axis_to(axis, value):
    command_pool = [set_max_vel_accel(str(axis_vel_values.get(axis)), str(axis_accel_values.get(axis))), gcodeUrl + absolute_position_command, gcodeUrl + move_axis_command + axis + str(value)]
    return command_pool


# Move axis forward by
def move_axis_forward_by(axis, value):
    command_pool = [set_max_vel_accel(str(axis_vel_values.get(axis)), str(axis_accel_values.get(axis))), gcodeUrl + relative_position_command, gcodeUrl + move_axis_command + axis + str(value)]
    return command_pool


# Move axis backward by
def move_axis_backward_by(axis, value):
    command_pool = [set_max_vel_accel(str(axis_vel_values.get(axis)), str(axis_accel_values.get(axis))), gcodeUrl + relative_position_command, gcodeUrl + move_axis_command + axis + str(value)]
    return command_pool


# HIGHER LEVEL CALLS

# MOVE WIRE GANTRY CALLS

# MOVE WIRE - create example for each


# Move Wire to
def move_wire_to(value):
    command_pool = [move_axis_to('Y', value)]
    return command_pool


# Move Wire Up by
def move_wire_up_by(value):
    command_pool = [move_axis_backward_by('Y', value)]
    return command_pool


# Move Wire Down by
def move_wire_down_by(value):
    command_pool = [move_axis_forward_by('Y', value)]
    return command_pool


# MOVE WIRE END


# MOVE GANTRY


# Move Gantry to
def move_gantry_to(value):
    command_pool = [move_axis_to('X', value)]
    return command_pool


# Move Gantry Forward by - towards blade
def move_gantry_forward_by(value):
    command_pool = [move_axis_forward_by('X', value)]
    return command_pool


# Move Gantry Backward to - away from blade
def move_gantry_backward_by(value):
    command_pool = [move_axis_backward_by('X', value)]
    return command_pool

# MOVE GANTRY END

# MOVE SLIDE GANTRY


# Move 
def get_current_position():
    command_pool = [gcodeUrl + get_current_position]
    return command_pool
