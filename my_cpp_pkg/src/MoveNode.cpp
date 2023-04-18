#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"


class MoveNode : public rclcpp::Node 
{
public:
    MoveNode() : Node("MoveNode") 
    {
    Move_Node_ = this->create_publisher<geometry_msgs::msg::Twist>("turtle1/cmd_vel",1);
    number_timer_ = this->create_wall_timer(std::chrono::milliseconds((int)(1000.0 / 5000.0)),
                                                std::bind(&MoveNode::directions, this));
    RCLCPP_INFO(this->get_logger(), "Node active.");
    }

private:
    void directions()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 1.0;
        msg.angular.z  = 1.0;
        Move_Node_->publish(msg);
    }
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr Move_Node_;
    rclcpp::TimerBase::SharedPtr number_timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MoveNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}