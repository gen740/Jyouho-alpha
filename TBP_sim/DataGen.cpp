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
std::string file_3 = "forward_step_data.csv";

void Random_Generate(int data_size)
{
    SizeOfData = data_size;
    fs::remove_all(dir);
    fs::create_directory(dir);
    std::ofstream(dir + "/" + file_1);
    std::fstream file;
    file.open(dir + "/" + file_1, std::ios::out);
    file << std::fixed;
    file << std::setprecision(16);
    for (int i = 0; i < data_size; i++) {
        for (int j = 0; j < NUMBER_OF_STAR; j++) {
            //  file << Rand_0to1() / 2 + 0.5 << " ";
            file << 1.0 << " ";
            for (int k = 0; k < DIM; k++) {
                file << (Rand_0to1() - 0.5) << " ";
            }
            for (int k = 0; k < DIM; k++) {
                file << (Rand_0to1() - 0.5) << " ";
            }
        }
        file.seekp(-1, std::ios::cur);
        file << std::endl;
    }
    file.close();
}

void Calcdata_for_learning(double t, double dt)
{
    static unsigned int counter = 0;
    static bool bar = false;
    static int processed = 0;
    const double num = SizeOfData / 50;
    std::ofstream(dir + "/" + file_2);
    std::fstream file;
    file.open(dir + "/" + file_1, std::ios::in);
    std::array<double, DATA_DIM> data;
    file << std::fixed;
    file << std::setprecision(16);
    for (int i = 0; i < SizeOfData; i++) {
        for (int i = 0; i < DATA_DIM; i++) {
            file >> data[i];
        }
        TBP tbp_for_learn(data);
        tbp_for_learn.dt = dt;
        int N = t / dt;
        for (int k = 0; k < N; k++) {
            tbp_for_learn.runge();
        }
        tbp_for_learn.Save_to_file(dir + "/" + file_2);

        if (bar == false) {
            std::cout << "|--------------------------------------------------|"
                      << std::endl
                      << " ";
            bar = true;
        }
        if (counter >= processed * num) {
            std::cout << "#" << std::flush;
            processed++;
        }
        counter++;
    }
    file.close();
}

void Calcdata_for_learning(int step, int data_interval, double dt)
{
    static unsigned int counter = 0;
    static bool bar = false;
    static int processed = 0;
    const double num = SizeOfData / 50;
    std::ofstream(dir + "/" + file_3);
    std::fstream file;
    std::fstream file_out;
    file_out << std::fixed;
    file_out << std::setprecision(16);
    file.open(dir + "/" + file_1, std::ios::in);
    file_out.open(dir + "/" + file_3, std::ios::out);
    std::array<double, DATA_DIM> data;
    for (int i = 0; i < SizeOfData; i++) {
        for (int i = 0; i < DATA_DIM; i++) {
            file >> data[i];
        }
        TBP tbp_for_learn(data);
        tbp_for_learn.dt = dt;
        for (int k = 1; k <= step * data_interval; k++) {
            tbp_for_learn.runge();
            if (k % data_interval == 0) {
                tbp_for_learn.Save_to_file(file_out);
            }
        }
        file_out.seekp(-1, std::ios::cur);
        file_out << std::endl;
        if (bar == false) {
            std::cout << "|--------------------------------------------------|"
                      << std::endl
                      << " ";
            bar = true;
        }
        if (counter >= processed * num) {
            std::cout << "#" << std::flush;
            processed++;
        }
        counter++;
    }
    file.close();
}
