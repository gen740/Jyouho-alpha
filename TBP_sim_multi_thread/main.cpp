#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <array>
#include <filesystem>
#include <iostream>
#include <string>
#include <thread>

// Other Functions
namespace fs = std::filesystem;

int main()
{
    Random_Generate_2(10000);
    Calcdata_for_learning_2();
}
