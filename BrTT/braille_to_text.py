import os

# GLOBAL PARAMETERS
UPPER_LIMIT = 100

PALM_SENSOR_VOLTAGE = 0
INDEX_SENSOR_VOLTAGE = 0
THUMB_SENSOR_VOLTAGE = 51
MID_SENSOR_VOLTAGE = 0
RING_SENSOR_VOLTAGE = 0
PINKY_SENSOR_VOLTAGE = 70


# FUNCTION DEFENETIONS
def isOn(sensor_value, upper_limit):
        return True if sensor_value > (upper_limit / 2) else False

def sensorSwitchVals(voltage_values):
    sensor_switch_vals = []

    for value in voltage_values:
        sensor_switch = isOn(value, UPPER_LIMIT)
        sensor_switch_vals.append(sensor_switch)

    return sensor_switch_vals

def concatVoltVals():
    return [PALM_SENSOR_VOLTAGE, INDEX_SENSOR_VOLTAGE, THUMB_SENSOR_VOLTAGE, MID_SENSOR_VOLTAGE, RING_SENSOR_VOLTAGE, PINKY_SENSOR_VOLTAGE]

def mapToBraille():
    # ASK CLIENT FOR MAPPING
    return None

def handler():
    voltage_list = concatVoltVals()
    switch_values = sensorSwitchVals(voltage_list)
    print(switch_values)

# MAIN
handler()
