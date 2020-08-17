#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <array>
#include <filesystem>
#include <iostream>
#include <string>

// Other Functions
namespace fs = std::filesystem;

int main()
{
    Random_Generate(10);
    Calcdata_for_learning();
}
