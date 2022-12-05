# Input filename
filename = "./Inputs/Day3Input.txt"

# Initialise sum
prioritySum = 0

# Begin read in
with open(filename, 'r') as f:

    for line in f:
        strpln = line.rstrip()

        if len(strpln) > 0:

            # Split out contents
            compartment1 = strpln[:len(strpln)//2]
            compartment2 = strpln[len(strpln)//2:]

            # Error handling in case of uneven lengths
            if len(compartment1) == len(compartment2):

                # Pull out matching items
                matchingItems = list(set(compartment1).intersection(set(compartment2)))

                # Probably overkill as problem statements says only one matching item but whatev
                for item in matchingItems:

                    if item.isupper():
                        # ASCII code for letter
                        priority = ord(item) - 38
                    
                    elif item.islower():
                        # ASCII code for letter
                        priority = ord(item) - 96

                    # Add to sum
                    prioritySum += priority

# Return priority sum
print(f"Total sum: {prioritySum}")
