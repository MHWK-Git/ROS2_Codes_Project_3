from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    motor_driver_node = Node(
        package="motor_driver",
        executable="MotorDrv",
        name="motor_driver",
    )

    motor_controller_node = Node(
        package="motor_controller",
        executable="MotorCon",
        name="motor_controller",
    )


    ld.add_action(motor_controller_node)
    ld.add_action(motor_driver_node)
    return ld
