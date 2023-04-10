#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
#include "number_app_interfaces/srv/reset_counter.hpp"

using std::placeholders::_1;
using std::placeholders::_2;

class NumberCounterNode : public rclcpp::Node
{
public:
    NumberCounterNode() : Node("number_counter"), counter_(0)
    {
        // Create publishers, subscribers, services, etc
        number_subscriber_ = this->create_subscription<example_interfaces::msg::Int64>(
            "number", 10, std::bind(&NumberCounterNode::callbackNumber, this, std::placeholders::_1));
        reset_number_service_ = this->create_service<number_app_interfaces::srv::ResetCounter>(
            "reset_counter",
            std::bind(&NumberCounterNode::callbackResetCounter, this, _1, _2));
        RCLCPP_INFO(this->get_logger(), "Number Counter has been started.");
    }

private:
    // callback for the subscriber
    void callbackNumber(const example_interfaces::msg::Int64::SharedPtr msg)
    {
        counter_ += msg->data;
        RCLCPP_INFO(this->get_logger(), "Counter: %d", counter_);
    }

    // callback for the service
    void callbackResetCounter(const number_app_interfaces::srv::ResetCounter::Request::SharedPtr request,
                              const number_app_interfaces::srv::ResetCounter::Response::SharedPtr response)
    {
        if (request->reset_value >= 0)
        {
            counter_ = request->reset_value;
            RCLCPP_INFO(this->get_logger(), "Counter: %d", counter_);
            response->success = true;
        }
        else
        {
            response->success = false;
        }
    }

    // declare class attributes
    int counter_;
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr number_subscriber_;
    rclcpp::Service<number_app_interfaces::srv::ResetCounter>::SharedPtr reset_number_service_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberCounterNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
