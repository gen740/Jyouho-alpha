#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <filesystem>
#include <fstream>
#include <iostream>

namespace fs = std::filesystem;

void Random_Generate(int data_size)
{
    fs::remove_all("data_for_learning");
    fs::create_directory("data_for_learning");
    std::ofstream("data_for_learning/initial_value.csv");
    std::fstream file;
    file.open("data_for_learning/initial_value.csv");
    for (int i = 0; i < data_size; i++) {
        for (int j = 0; j < NUMBER_OF_STAR; j++) {
            file << Rand_0to1() / 2 + 0.5 << " ";
            for (int k = 0; k < DIM * 2; k++) {
                file << Rand_0to1() - 0.5 << " ";
            }
        }
        file << "\n";
        if (i % 1000 == 0) {
            file << std::flush;
        }
    }
    std::cout << Rand_0to1() << std::endl;
    file.close();
}

void Calcdata_for_learning(int input)
{
    fs::remove_all("data_for_learning");
    fs::create_directory("data_for_learning");
    std::ofstream("data_for_learning/forward_dt_data.csv");
    std::fstream file;
    file.open("data_for_learning/forward_dt_data.csv");
    file.close();
}
