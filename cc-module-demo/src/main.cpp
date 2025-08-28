import math;
#include <iostream>
#include <string>

int main()
{
    std::cout << "1 + 2 = " << add<int>(1, 2) << std::endl;
    std::cout << "Hello + World! = " << add<std::string>("Hello ", "World!") << std::endl;
    return 0;
}
