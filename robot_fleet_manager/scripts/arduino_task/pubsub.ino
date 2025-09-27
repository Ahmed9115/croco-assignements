/*
 * rosserial PubSub Example
 * Prints "hello world!" and toggles led
 */

#include <ros.h>
#include <robot_fleet_manager/custom.h>

ros::NodeHandle  nh;


void messageCb( const robot_fleet_manager::custom)
{

  if custom.key == "q" 
    {
      digitalWrite(13, HIGH);
    }

  else if  custom.key == "w" 
    {
      digitalWrite(13, LOW);
    }

}

ros::Subscriber<robot_fleet_manager::custom> sub("keyboard", messageCb );


void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(500);
}














