#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <array>
#include <filesystem>
#include <fstream>
#include <iostream>

namespace fs = std::filesystem;

std::string dir = "data_for_learning";
std::string file_1 = "initial_value.csv";
std::string file_2 = "forward_dt_data.csv";

void Random_Generate(int data_size)
{
    SizeOfData = data_size;
    fs::remove_all(dir);
    fs::create_directory(dir);
    std::ofstream(dir + "/" + file_1);
    std::fstream file;
    file.open(dir + "/" + file_1);
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

void Calcdata_for_learning()
{
    fs::remove_all(dir);
    fs::create_directory(dir);
    std::ofstream(dir + "/" + file_2);
    std::fstream file;
    file.open(dir + "/" + file_2);
    std::array<double, DATA_DIM> data;
    for (int i = 0; i < SizeOfData; i++) {
        for (int i = 0; i < DATA_DIM; i++) {
            file >> data[i];
        }
    }
    file.close();
}
