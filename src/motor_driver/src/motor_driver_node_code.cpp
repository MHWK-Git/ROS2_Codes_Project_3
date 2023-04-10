#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/float64.hpp"
#include "motor_driver/driver.hpp"

class MotorDriver : public rclcpp::Node // MODIFY NAME
{
public:
    MotorDriver() : Node("motor_driver")  // MODIFY NAME
    {
        md.init();
        position_state_pub = this->create_publisher<example_interfaces::msg::Float64>("/position_state",10);

        freq = this->create_wall_timer(std::chrono::milliseconds(100),std::bind(&MotorDriver::motor_publisher, this));

        position_command_sub = this->create_subscription <example_interfaces::msg::Float64>(
            "/position_command", 10, std::bind(&MotorDriver::motor_callback, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "MotorDriver node is active.");
    }

private:
    void motor_publisher()
    {
        auto msg = example_interfaces::msg::Float64();
        msg.data = md.readPosition();
        position_state_pub->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Pos: %.1f", msg.data);
        RCLCPP_INFO(this->get_logger(), "--------------------------------------");
    }


    void motor_callback(const example_interfaces::msg::Float64::SharedPtr msg)
    {
        md.writePosition(msg->data);   
    }
        MyDriver md;
        rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr position_state_pub;
        rclcpp::Subscription<example_interfaces::msg::Float64>::SharedPtr position_command_sub;
        rclcpp::TimerBase::SharedPtr freq;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MotorDriver>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}