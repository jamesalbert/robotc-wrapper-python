#!/usr/bin/env python

class new:
    def __init__(self):
        next

    def start_void(self, name):
        print "void %s() {" % name

    def start_task(self):
         print "task main() {"

    def start_if(self, cond):
         print "if ( %s ) {" % cond

    def start_else_if(self, cond):
         print "else if ( %s ) {" % cond

    def start_for(self, init, end):
         print "for (int i = %d; i < %d; i++) {" % (init, end)

    def end(self):
         print "}"

    def int_var(self, name, value):
         print "int %s = %r;" % (name, value)

    def char_var(self, name, value):
         print "char %s = %r;" % (name, value)

    def long_var(self, name, value):
         print "in %s = %r;" % (name, value)

    def battery(self, name):
         print "int %s = nImmediateBatteryLevel;" % name

    def cos(self, radians):
         print "cos(%d);" % radians

    def sin(self, radians):
         print "sin(%d);" % radians

    def tan(self, radians):
         print "tan(%d);" % radians

    def d_r(self, degrees):
         print "degreesToRadians(%d);" % degrees

    def r_d(self, radians):
         print "radiansToDegrees(%d);" % radians

    def kill(self, task):
         print "StopTask(%s);" % task

    def mute(self):
         print "ClearSounds();"

    def sound(self, freq, dur):
         print "PlayImmediateTone(%d, %d);" % (freq, dur)

    def tone(self, tone):
         print "PlaySound(%s);" % tone

    def sound_power(self, switch):
         print "bPlaySounds = %s;" % switch

    def start_while(self, cond):
         print "while (%s) {" % cond

    def if_sound(self):
         print "if(bHasSoundDriver){"

    def if_active(self):
         print "if(bVEXNETActive = true){"

    def pragma(self, port, name, sensor):
         print "#pragma config(Sensor, in%d, \"%s\", sensor%s);" % (port, name, sensor)

    def reflect(self, port, switch):
         print "bMotorReflected[port%d] = %s;" % (port, switch)

    def auto(self, switch):
         print "bVexAutonomousMode = %s;" % switch

    def inc_plus(self, var):
         print "%s++;" % var

    def inc_minus(self, var):
        print "%s--;" % var

    def motor(self, port, speed):
         print "motor[port%r] = %r;" % (port, speed)

    def speed_up(self, port, speed):
         print "motor[port%r] += %r;" % (port, speed)

    def clear_time(self):
         print "ClearTimer(T1);";

    def time_while(self, end):
         print "while(Time1[T1] <= %d){" % end

    def wait(self, dur):
         print "wait1Msec(%d000);" % dur

    def cont(self, port, channel):
         print "motor[port%d] = vexRT[Ch%d];" % (port, channel)

    def call(self, call):
         print "%s();" % call
