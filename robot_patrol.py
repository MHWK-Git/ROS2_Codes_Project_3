#!/usr/bin/env python3
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import time
import keyboard


def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.00
    initial_pose.pose.position.y = 0.00
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 1.0
    navigator.setInitialPose(initial_pose)

    # Wait for navigation to fully activate
    navigator.waitUntilNav2Active()

    # using function to go to goal

    # point 1
    if keyboard.is_pressed("1"):
        goal_waypoint(navigator, 2.0, 2.5, 0.0, 1.0)
        time.sleep(1.2)

    # point 2
    if keyboard.is_pressed("2"):
        goal_waypoint(navigator, 4.0, 0.5, -0.7, 0.7)
        time.sleep(1.2)

    # point 3
    if keyboard.is_pressed("3"):
        goal_waypoint(navigator, 1.5, -1.5, -1.0, 0.0)
        time.sleep(1.2)

    # point 4
    if keyboard.is_pressed("4"):
        goal_waypoint(navigator, 0.0, 0.0, 0.7, 0.7)
        time.sleep(1.2)


def goal_waypoint(navigator, x_pos, y_pos, z_ori, w_ori):
    # Variables to a given pose
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = x_pos
    goal_pose.pose.position.y = y_pos
    goal_pose.pose.orientation.z = z_ori
    goal_pose.pose.orientation.w = w_ori

    navigator.goToPose(goal_pose)
    while not navigator.isTaskComplete():
        pass


if __name__ == '__main__':
    main()
