cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

# Create executables
add_executable(Circle src/MoveNode.cpp)
ament_target_dependencies(Circle rclcpp geometry_msgs)


# Install the executables
install(TARGETS
  Circle
  DESTINATION lib/${PROJECT_NAME}/
)


ament_package()
