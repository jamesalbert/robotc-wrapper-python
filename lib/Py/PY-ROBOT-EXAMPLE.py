#!/usr/bin/env python

import Robot
from Robot import Utils

robot = Robot.new()
utils = Utils.new()

def BASIC():
    utils.BASIC_MOVEMENTS()

def SET_CONT():
    robot.start_void("set_cont")
    robot.cont(2, 2)
    robot.cont(1, 3)
    robot.end()

def KLAW_KONT():
    robot.start_void("klaw_kont")
    robot.int_var("POS", 0)
    robot.int_var("C_5", "vexRT[Ch5]")
    robot.int_var("C_6", "vexRT[Ch6]")
    robot.start_if("C_5 == 127")
    robot.start_if("POS <= 1")
    robot.inc_plus("POS")
    robot.motor(3, 40)
    robot.motor(4, 40)
    robot.wait(1)
    robot.end()
    robot.end()
    robot.start_else_if("C_5 == -127")
    robot.start_if("POS >= 1")
    robot.inc_minus("POS")
    robot.motor(3, -40)
    robot.motor(4, -40)
    robot.wait(1)
    robot.end()
    robot.end()
    robot.start_else_if("C_6 == 127")
    robot.start_if("POS == 0")
    robot.inc_plus("POS")
    robot.inc_plus("POS")
    robot.motor(3, 40)
    robot.motor(4, 40)
    robot.wait(2)
    robot.end()
    robot.end()
    robot.start_else_if("C_6 == -127")
    robot.start_if("POS == 2")
    robot.inc_minus("POS")
    robot.inc_minus("POS")
    robot.motor(3, -40)
    robot.motor(4, -40)
    robot.wait(2)
    robot.end()
    robot.end()

def MAIN_TASK():
    robot.start_task()
    robot.start_while("true")
    robot.call("set_cont")
    robot.call("klaw_kont")
    robot.end()
    robot.end()
    robot.end()

BASIC()
SET_CONT()
KLAW_KONT()
MAIN_TASK()
