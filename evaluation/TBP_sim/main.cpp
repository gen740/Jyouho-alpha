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
    Random_Generate(1000);
    Calcdata_for_learning();
}
