#ifndef MY_DRIVER_HPP
#define MY_DRIVER_HPP

class MyDriver 
{
public:
    MyDriver() {
        position_command_ = 0.0;
        position_state_ = 0.0;
    }

    void init() {
        // Init communication with hardware
    }

    double readPosition() {
        // Read data (state) from hardware
        // For simulation purpose, as we don't have hardware, 
        // we just "loop back" the command into the position
        position_state_ = position_command_;
        return position_state_;
    }

    void writePosition(double cmd) {
        // Write data (command) to hardware
        position_command_ = cmd;
    }

private:
    double position_command_;
    double position_state_;
};

#endif