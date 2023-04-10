#!/usr/bin/env python3
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import time
from getkey import getkey


def main():

    print('Press 1, 2, 3, 4 or 5 for the turtlebot to move to a location and back to home point')
    rclpy.init()

    navigator = BasicNavigator()
    key = getkey()
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

    # using function to request for robot and for robot go to goal
    # after user selects option
    while True:
        if key == '1':
            request(navigator, 2.6, 0.0, 0.0, 1.0)
            ask_and_fulfil(navigator)
            break

        elif key == '2':
            request(navigator, 7.0, -0.5, 0.0, 1.0)
            ask_and_fulfil(navigator)
            break

        elif key == '3':
            request(navigator, 2.6, 5.0, 0.0, 1.0)
            ask_and_fulfil(navigator)
            break

        elif key == '4':
            request(navigator, 3.1, 11.3, -1.0, 0.0)
            ask_and_fulfil(navigator)
            break

        elif key == '5':
            request(navigator, 2.6, 0.0, 0.0, 1.0)
            ask_and_fulfil(navigator)
            break


# robot goes to user location after call
def request(navigator, x_pos_goal, y_pos_goal, z_ori_goal, w_ori_goal):
    goal_waypoint(navigator, x_pos_goal, y_pos_goal, z_ori_goal, w_ori_goal)
    time.sleep(0.5)
    Questions()


# Robot goes to location and back to home base
def destination(navigator, x_pos_goal, y_pos_goal, z_ori_goal, w_ori_goal):
    time.sleep(0.5)
    goal_waypoint(navigator, x_pos_goal, y_pos_goal, z_ori_goal, w_ori_goal)
    time.sleep(5.0)
    goal_waypoint(navigator, 0.0, 0.0, 0.0, 1.0)
    time.sleep(0.5)


# function for robot to go to a waypoint
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


# Select enquiry and robot goes to location to answer enquiry
def ask_and_fulfil(navigator):
    Option = input("\nEnter Option:")
    print("Option: " + Option)
    print("\n")
    if Option == 'A' or Option == 'a':
        destination(navigator, 3.0, -3.1, 0.0, -1.0)

    elif Option == 'B' or Option == 'b':
        destination(navigator, 8.0, 5.1, 0.0, -1.0)

    elif Option == 'C' or Option == 'c':
        destination(navigator, 9.0, -8.1, 0.0, -1.0)

    elif Option == 'D' or Option == 'd':
        destination(navigator, 11.0, 0.1, 0.0, -1.0)


# Select FAQs that fits your enquiry
def Questions():
    print("\nPlease select your enquiry option so our automated assistant can guide you")
    print("A:Question 1")
    print("B:Question 2")
    print("C:Question 3")
    print("D:Question 4")


if __name__ == '__main__':
    main()
