#!/bin/bash

mkdir build
cd build
cmake .. -DGPU_MODE=CPU_ONLY
make -j4
