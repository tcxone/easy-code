#!/bin/bash

rm out.py
echo "ready"
python main.py $1
echo "-------------------------"
python out.py