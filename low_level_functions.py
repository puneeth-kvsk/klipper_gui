
#http_link = 'http://192.168.236.220:'

gcodeUrl = 'http://fluiddpi.local/printer/gcode/script?script='
printerInfoUrl = 'http://192.168.6.228:7125/printer/info'
speedSettingUrl = gcodeUrl + 'SET_VELOCITY_LIMIT VELOCITY='
accelerationSettingUrl = gcodeUrl + 'M204S'

axis_accel_values = {'H': 1500, 'I': 1500, 'J': 1500, 'K': 200, 'L': 150, 'X': 1500, 'Y': 1500, 'N': 150}
axis_vel_values = {'H': 300, 'I': 300, 'J': 300, 'K': 3, 'L': 3, 'X': 300, 'Y': 300, 'N': 3}


# VELOCITY MACROS

# Velocity Setting
def m201(value):
    command_pool = speedSettingUrl + value
    return command_pool


# Acceleration Setting
def m204(value):
    command_pool = accelerationSettingUrl + value
    return command_pool


# Set maximum velocity and acceleration value for axis manually - not useful
def set_max_vel_accel_manual(velocity, acceleration):
    command_pool = [m201(velocity), m204(acceleration)]
    return command_pool


# Set max accel value (used for homing)
def set_max_accel(axis):
    value = axis_accel_values.get(axis)
    return m204(value)


# Set velocity and acceleration values routine
def set_vel_accel_auto(axis):
    vel_value = axis_vel_values.get(axis)
    accel_value = axis_accel_values.get(axis)

    command_pool = []
    command_pool.append(m201(str(vel_value)))
    command_pool.append(m204(str(accel_value)))
    return command_pool

# VELOCITY MACROS END
