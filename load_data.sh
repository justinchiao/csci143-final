#!/bin/sh

python3 fake_data.py --db=postgresql://postgres:pass@localhost:1319 --rows=1000000
