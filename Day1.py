import numpy as np

# Define file name to read
filename = "./Inputs/Day1Input1.txt"

# Empty array for sums
elfCalories = []

# Open file
with open(filename, 'r') as f:

    # Intialise sum
    sum = 0

    for line in f:
        # Remove whitespace
        strpln = line.rstrip()

        # If line is non-empty, add to sum
        if len(strpln) > 0:
            sum += float(strpln)
            continue
        # If line is empty, store sum in array and re-initialise sum
        else:
            elfCalories.append(sum)
            sum = 0
            continue

# Sort array from largest to smallest
elfCalories.sort(reverse = True)

# Extract the top 3 calories and sum
top3 = elfCalories[:3]
topSum = 0
for cal in top3:
    topSum += cal

# Display results
print(f'Maximum individual calories: {max(elfCalories)}')
print(f'Sum of Top 3 calories: {topSum}')


