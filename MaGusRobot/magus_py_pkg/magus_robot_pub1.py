#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
class MagusRobotPub1(Node):
    def __init__(self):
        super().__init__("magus_robot_1")
        self.declare_parameter("name", "Magus 1")
        self.robot_name_ = self.get_parameter("name").value
        self.create_publisher(String, "/magus_topic", 10)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Data from " + self.robot_name_ + " to the Magus Server"
        self.get_logger().info("Sending message from " + self.robot_name_)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = MagusRobotPub1()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()