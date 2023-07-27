#!/bin/bash
python3 ./simulation_monitoring.py &
python3 ./test_code.py f &
wait