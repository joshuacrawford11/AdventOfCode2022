# Input filename
filename = "./Inputs/Day3Input.txt"

# Initialise sum
prioritySum = 0
groupSum = 0
linecount = 0

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

# Begin read in
with open(filename, 'r') as f:

    for line in f:
        strpln = line.rstrip()

        if len(strpln) > 0:

            # Only read in groups on multiples of 3
            elf1 = strpln
            elf2 = f.readline().rstrip()
            elf3 = f.readline().rstrip()

            # Find matching item between all 3
            groupItem = list(set(elf1).intersection(set(elf2).intersection(elf3)))[0]

            if groupItem.isupper():
                # ASCII code for letter
                priority = ord(groupItem) - 38
            
            elif groupItem.islower():
                # ASCII code for letter
                priority = ord(groupItem) - 96

            groupSum += priority

# Return priority sum
print(f"Total sum: {prioritySum}")
print(f"Group sum: {groupSum}")
