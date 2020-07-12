#pragma once

#include "TBP_class.hpp"

#include <filesystem>
#include <fstream>
#include <iostream>

// define constances
constexpr int DATA_DIM = NUMBER_OF_STAR * (1 + 2 * DIM);
static int SizeOfData = 1000;

void Random_Generate(int data_size = SizeOfData);
void Calcdata_for_learning(double t, double dt = 0.0001);
