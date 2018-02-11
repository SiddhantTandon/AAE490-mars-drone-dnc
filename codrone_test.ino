#include <CoDrone.h>   // allows use of functions in Codrone library (takeoff, control, trim, etc.)

void setup() {
  // put your setup code here, to run once:
  CoDrone.begin(115200);             // 115200 = "Baud rate of serial communication" = communication speed in bytes per second -- must be set at 115200 
  CoDrone.AutoConnect(NearbyDrone);  // Automatically connects to drone -- flashing green light = unpaired, solid green light = paired
  delay(2000);
  CoDrone.FlightEvent(TakeOff);
  delay(1000);
  CoDrone.Set_TrimAll(0,0,0,0,0);

  elevate(3); 

  PITCH = 80;
  THROTTLE = 20;
  CoDrone.Control();
  delay(3000);
  
  //zigzag(6);

 
  CoDrone.FlightEvent(Landing);
  CoDrone.Buzz(3000, 50);
  delay(1000);
}


void elevate(float height){
  THROTTLE = 70;
  CoDrone.Control();
  delay(height*1000);
  
}
void zigzag(int numZig){
  int sign  = 1;
  for(int i = 0; i<numZig; i++){
    Maneuver(20, sign*50, 70, 0);
    delay(1200);
    sign = sign * -1;
  }
}

void Maneuver (int throttle, int roll, int pitch, int yaw){
  THROTTLE = throttle;
  ROLL = roll;
  PITCH = pitch;
  YAW = yaw;
  CoDrone.Control();
}
void loop() {
  // put your main code here, to run repeatedly:  

}


