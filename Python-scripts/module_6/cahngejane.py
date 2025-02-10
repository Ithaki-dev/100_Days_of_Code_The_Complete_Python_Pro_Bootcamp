import sys
import subprocess

with open(sys.argv[1]) as f:
    for line in f:
        if 'jane' in line:
            new_name = line.replace('jane', 'jdoe')
            subprocess.run(['mv', line.strip(), new_name.strip()])