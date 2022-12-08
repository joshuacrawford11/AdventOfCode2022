import numpy as np

filename = "./Inputs/Day4Input.txt"

# Initialise counter
counter = 0

with open(filename, 'r') as f:
    for line in f:
        strpln = line.rstrip()

        if len(strpln) > 0:

            # Split text at comma
            assignments = strpln.split(',')

            # Designate elf assignments, noting bounds of arrays
            elf1_assign = assignments[0].split('-')
            elf1_assign = np.arange(int(elf1_assign[0]), int(elf1_assign[1])+1)

            elf2_assign = assignments[1].split('-')
            elf2_assign = np.arange(int(elf2_assign[0]), int(elf2_assign[1])+1)

            # Check to see whether one range is contained in the other
            if set(elf1_assign).issubset(set(elf2_assign)) or set(elf2_assign).issubset(set(elf1_assign)):
                counter += 1

print(f"Num overlaps: {counter}")

