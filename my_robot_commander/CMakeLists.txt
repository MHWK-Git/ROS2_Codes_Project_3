cmake_minimum_required(VERSION 3.8)
project(my_robot_commander)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_move_group REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
#find_package(Quaternion REQUIRED)

add_executable(commander src/robot_commander.cpp)
ament_target_dependencies(commander rclcpp moveit_ros_move_group moveit_ros_planning_interface )#Quaternion)

install (TARGETS commander
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
