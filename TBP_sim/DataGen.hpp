#pragma once

#include "TBP_class.hpp"

#include <fstream>
#include <iostream>

// define constances
constexpr int DATA_DIM = NUMBER_OF_STAR * (1 + 2 * DIM);
static int SizeOfData = 1000;

void Random_Generate(int data_size = SizeOfData);
void Calcdata_for_learning(double t, double dt = 0.001);
void Calcdata_for_learning(int step, int data_interval = 10, double dt = 0.001);
