#!/usr/bin/env python3
import rclpy
import requests
from rclpy.node import Node
from example_interfaces.msg import Float64
from temperature_collector_interfaces.msg import TemperatureCollector

 
class TempCollectorNode(Node):
    def __init__(self):
        super().__init__("temp_collector_node")
        self.temp_collector_publisher_ = self.create_publisher(TemperatureCollector, "temp_collector_msg", 10)
        self.timer_ = self.create_timer(10.0, self.extract_temp_collector)
        self.get_logger().info("Temperature Collector publisher has been started.")

    def extract_temp_collector(self):
        msg = TemperatureCollector()
        msg.temperature_campinas = 35.0
        msg.temperature_santoandre = 27.0
        msg.temperature_saopaulo = 18.0
        self.temp_collector_publisher_.publish(msg) 
 
def main(args=None):
    rclpy.init(args=args)
    node = TempCollectorNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()