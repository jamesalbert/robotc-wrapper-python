#pragma config(Sensor, in2, "button", sensorTouch);
bMotorReflected[port2] = true;
bVexAutonomousMode = false;
void forward() {
motor[port2] = 127;
motor[port1] = 127;
}
void reverse() {
motor[port2] = -127;
motor[port1] = -127;
}
void turn_left() {
motor[port2] = 127;
motor[port1] = -127;
wait1Msec(1000);
}
void turn_right() {
motor[port2] = -127;
motor[port1] = 127;
wait1Msec(1000);
}
void stop() {
motor[port2] = 0;
motor[port1] = 0;
}
void set_cont() {
motor[port2] = vexRT[Ch2];
motor[port1] = vexRT[Ch3];
}
void klaw_kont() {
int POS = 0;
int C_5 = 'vexRT[Ch5]';
int C_6 = 'vexRT[Ch6]';
if ( C_5 == 127 ) {
if ( POS <= 1 ) {
POS++;
motor[port3] = 40;
motor[port4] = 40;
wait1Msec(1000);
}
}
else if ( C_5 == -127 ) {
if ( POS >= 1 ) {
POS--;
motor[port3] = -40;
motor[port4] = -40;
wait1Msec(1000);
}
}
else if ( C_6 == 127 ) {
if ( POS == 0 ) {
POS++;
POS++;
motor[port3] = 40;
motor[port4] = 40;
wait1Msec(2000);
}
}
else if ( C_6 == -127 ) {
if ( POS == 2 ) {
POS--;
POS--;
motor[port3] = -40;
motor[port4] = -40;
wait1Msec(2000);
}
}
task main() {
while (true) {
set_cont();
klaw_kont();
}
}
}
