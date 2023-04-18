#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

static const rclcpp::Logger LOGGER = rclcpp::get_logger("move_group_demo");

void go_to_goal(moveit::planning_interface::MoveGroupInterface &move_group, double r1, double r2, double r3, double r4, double r5, double r6)
{
  std::vector<double> joint_group_positions = {r1, r2, r3, r4, r5, r6};
  
  move_group.setJointValueTarget(joint_group_positions);
  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  move_group.plan(my_plan);
  move_group.move();
}

int main(int argc, char **argv)
{
    // INIT - Beginning - do not modify
    rclcpp::init(argc, argv);
    rclcpp::NodeOptions node_options;
    node_options.automatically_declare_parameters_from_overrides(true);
    auto move_group_node = rclcpp::Node::make_shared("robot_commander", node_options);

    rclcpp::executors::SingleThreadedExecutor executor;
    executor.add_node(move_group_node);
    std::thread([&executor]() { executor.spin(); }).detach();

    static const std::string PLANNING_GROUP = "arm";
    moveit::planning_interface::MoveGroupInterface move_group(move_group_node, PLANNING_GROUP);
  
    const moveit::core::JointModelGroup* joint_model_group =
      move_group.getCurrentState()->getJointModelGroup(PLANNING_GROUP);

    RCLCPP_INFO(LOGGER, "Planning frame: %s", move_group.getPlanningFrame().c_str());
    RCLCPP_INFO(LOGGER, "End effector link: %s", move_group.getEndEffectorLink().c_str());
    // INIT - End

    std::vector<double> joint_group_positions = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

    //point 1
    go_to_goal(move_group, -1.0, 1.0, 0.5, 0.2, 0.3, 0.3);

    //point 2
    go_to_goal(move_group, 1.0, 1.0, 1.5, -0.4, 0.6, 0.3);

    //point 3
    go_to_goal(move_group, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

    rclcpp::shutdown();
    return 0;
}