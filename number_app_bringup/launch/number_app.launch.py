from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    number_publisher_node = Node(
        package="number_app_py",
        executable="number_publisher",
        name="my_number_publisher",
        parameters=[
            {"number_to_publish": 4},
            {"publish_frequency": 5.0}
        ]
    )

    number_counter_node = Node(
        package="number_app_cpp",
        executable="number_counter",
        name="my_number_counter",
    )

    ld.add_action(number_publisher_node)
    ld.add_action(number_counter_node)
    return ld
