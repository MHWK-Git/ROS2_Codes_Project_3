cmake_minimum_required(VERSION 3.8)
project(motor_driver)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

include_directories(include)

add_executable(MotorDrv src/motor_driver_node_code.cpp)
ament_target_dependencies(MotorDrv rclcpp example_interfaces)

# Install the executables
install(TARGETS
  MotorDrv
  DESTINATION lib/${PROJECT_NAME}/
)
ament_package()
