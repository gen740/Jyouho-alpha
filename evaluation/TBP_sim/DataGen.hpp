#pragma once

#include "TBP_class.hpp"

#include <filesystem>
#include <fstream>
#include <iostream>

// define constances
constexpr int DATA_DIM = 2;
static int SizeOfData = 20;
static int TIME = 500;

void Random_Generate(int data_size = SizeOfData);
void Calcdata_for_learning();
