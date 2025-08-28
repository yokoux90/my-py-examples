module;

#include <iostream>
#define PI 3.141592653

export module math;

export template <typename T>
T add(T a, T b)
{
    std::cout << "Inner: " << a << " + " << b << std::endl;
    return a + b;
}