#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("Move_Node") # MODIFY NAME
        self.get_logger().info("Node active")
        self.pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel",1)
        self.timer_ = self.create_timer(0.2,self.directions)

        
    def directions(self):
        msg = Twist()
        msg.linear.x = -1.0
        msg.angular.z = -1.0
        self.pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoveNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()