#include "DataGen.hpp"
#include "TBP_class.hpp"

#include <array>
#include <cmath>
#include <filesystem>
#include <fstream>
#include <iostream>

namespace fs = std::filesystem;

std::string dir = "./data_for_evaluation";
std::string file_ini_1 = "initial_value_for_ai.csv";
std::string file_ini_2 = "initial_value_for_runge.csv";
std::string file_1 = "forward_runge_data.csv";
std::string file_2 = "forward_ai_data.csv";

void Random_Generate(int data_size)
{
    SizeOfData = data_size;
    fs::remove_all(dir);
    fs::create_directory(dir);
    // Runge-----file
    std::ofstream(dir + "/" + file_ini_2);
    std::fstream file2;
    file2.open(dir + "/" + file_ini_2, std::ios::out);
    file2 << std::fixed;
    file2 << std::setprecision(16);
    // AI-------file
    std::ofstream(dir + "/" + file_ini_1);
    std::fstream file1;
    file1.open(dir + "/" + file_ini_1, std::ios::out);
    file1 << std::fixed;
    file1 << std::setprecision(16);
    // START
    for (int i = 0; i < data_size; i++) {
        double x_2, y_2;
        x_2 = -Rand_0to1() / 2;
        y_2 = Rand_0to1() * std::sqrt(1 - std::pow(x_2, 2));
        file2 << x_2 << " " << y_2 << " ";
        file2.seekp(-1, std::ios::cur);
        file2 << std::endl;
        for (int i = 0; i < TIME; i++) {
            file1 << (double)i / 100 + 0.01 << " "
                  << x_2 << " "
                  << y_2 << " ";
        }
        file1.seekp(-1, std::ios::cur);
        file1 << std::endl;
    }
    file1.close();
    file2.close();
}

void Calcdata_for_learning()
{
    // file------set
    std::fstream file;
    file.open(dir + "/" + file_ini_2, std::ios::in);
    // file_output------set
    std::ofstream(dir + "/" + file_1);
    std::fstream file_out;
    file_out.open(dir + "/" + file_1, std::ios::out);
    file_out << std::fixed;
    file_out << std::setprecision(16);
    // START
    std::array<double, DATA_DIM> data;
    std::array<double, 15> stars_initial;
    for (int i = 0; i < SizeOfData; i++) {
        double x_2, y_2;
        file >> x_2;
        file >> y_2;
        stars_initial[0] = 1.0;
        stars_initial[1] = 1.0;
        stars_initial[2] = 0.0;
        stars_initial[3] = 0.0;
        stars_initial[4] = 0.0;
        stars_initial[5] = 1.0;
        stars_initial[6] = x_2;
        stars_initial[7] = y_2;
        stars_initial[8] = 0.0;
        stars_initial[9] = 0.0;
        stars_initial[10] = 1.0;
        stars_initial[11] = -1.0 - x_2;
        stars_initial[12] = -y_2;
        stars_initial[13] = 0.0;
        stars_initial[14] = 0.0;
        TBP tbp_for_learn(stars_initial);
        tbp_for_learn.dt = 0.001;
        for (int k = 1; k <= TIME * 10; k++) {
            tbp_for_learn.runge();
            if (k % 10 == 0) {
                tbp_for_learn.Save_to_file(file_out);
            }
        }
        file_out.seekp(-1, std::ios::cur);
        file_out << std::endl;
    }
    file.close();
    file_out.close();
}
