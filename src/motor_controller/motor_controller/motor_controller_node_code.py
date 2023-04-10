#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class MotorController(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("motor_controller") # MODIFY NAME
        self.bool = True
        self.MotCom_publisher = self.create_publisher(Float64, "position_command", 10)    
        self.get_logger().info("MotorController node is active.")

        self.MotCom_subscriber = self.create_subscription(
            Float64, "position_state", self.callback, 10)

    def callback(self, msg):
        self.get_logger().info("Active")
        if msg.data < 100 and self.bool == True:
            msg.data += 1.0
            if msg.data == 100:
                self.bool = False

        elif msg.data > -100 and self.bool == False:
            msg.data -= 1.0
            if msg.data == -100:
                self.bool = True

        self.MotCom_publisher.publish(msg)
    

def main(args=None):
    rclpy.init(args=args)
    node = MotorController() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
