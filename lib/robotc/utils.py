#!/usr/bin/env python

import __init__

robot = __init__.robotcwrapper()

class robotcwrapperutils:

    def SETUP(self, sensor_in, sensor_name, sensor_type, reflect_port, reflect_switch, auto_switch):
        robot.pragma(sensor_in, sensor_name, sensor_type)

        robot.reflect(reflect_port, reflect_switch)
        robot.auto(auto_switch)

    def FORWARD(self, port_1, port_2, speed):
        robot.start_void("forward")
        robot.motor(port_1, speed)
        robot.motor(port_2, speed)
        robot.end()

    def REVERSE(self, port_1, port_2, speed):
        robot.start_void("reverse")
        robot.motor(port_1, -(speed))
        robot.motor(port_2, -(speed))
        robot.end()

    def TURN_LEFT(self, port_1, port_2, speed, duration):
        robot.start_void("turn_left")
        robot.motor(port_1, -(speed))
        robot.motor(port_2, speed)
        robot.wait(duration)
        robot.end()

    def TURN_RIGHT(self, port_1, port_2, speed, duration):
        robot.start_void("turn_right")
        robot.motor(port_1, -(speed))
        robot.motor(port_2, speed)
        robot.wait(duration)
        robot.end()

    def SUSPEND(self, port_1, port_2):
        robot.start_void("stop")
        robot.motor(port_1, 0)
        robot.motor(port_2, 0)
        robot.end()

