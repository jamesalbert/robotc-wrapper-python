#!/usr/bin/env python

from robotc import __init__, utils

shortcut = utils.robotcwrapperutils()

def create_a_lot_of_voids():
    shortcut.SETUP(2, "button", "Touch", 2, "true", "false")

robot = __init__.robotcwrapper()

def create_void():
    robot.start_void("function_name")
    robot.motor(1, 127)
    robot.motor(2, 127)
    robot.end()

create_a_lot_of_voids()
create_void()
