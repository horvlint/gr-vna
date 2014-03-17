#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/balint/workspace/gr-vna/lib
export PATH=/home/balint/workspace/gr-vna/build/lib:$PATH
export LD_LIBRARY_PATH=/home/balint/workspace/gr-vna/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-vna 
