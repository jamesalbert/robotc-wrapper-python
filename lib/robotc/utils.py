#!/usr/bin/env python

import __init__

robot = __init__.robotcwrapper()

class robotcwrapperutils:

    def SETUP(self):
        robot.pragma(2, "button", "Touch")

        robot.reflect(2, "true")
        robot.auto("false")

    def FORWARD(self):
        robot.start_void("forward")
        robot.motor(2, 127)
        robot.motor(1, 127)
        robot.end()

    def REVERSE(self):
        robot.start_void("reverse")
        robot.motor(2, -127)
        robot.motor(1, -127)
        robot.end()

    def TURN_LEFT(self):
        robot.start_void("turn_left")
        robot.motor(2, 127)
        robot.motor(1, -127)
        robot.wait(1)
        robot.end()

    def TURN_RIGHT(self):
        robot.start_void("turn_right")
        robot.motor(2, -127)
        robot.motor(1, 127)
        robot.wait(1)
        robot.end()

    def SUSPEND(self):
        robot.start_void("stop")
        robot.motor(2, 0)
        robot.motor(1, 0)
        robot.end()

    def BASIC_MOVEMENTS(self):
        self.SETUP()
        self.FORWARD()
        self.REVERSE()
        self.TURN_LEFT()
        self.TURN_RIGHT()
        self.SUSPEND()

