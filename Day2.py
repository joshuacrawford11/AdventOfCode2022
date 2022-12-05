# Import data
importFilename = "./Inputs/Day2Input.txt"

# Constants for scores
rockScore = 1
paperScore = 2
scissorsScore = 3

drawScore = 3
winScore = 6

# Key for data
rockIcons = ['A', 'X']
paperIcons = ['B', 'Y']
scissorsIcons = ['C', 'Z']

# Initialise score
totalScore = 0
realScore = 0

# Begin data read
with open(importFilename, 'r') as f:

    for line in f:
        strpln = line.rstrip()

        if len(strpln) > 0:

            play_round = strpln.split()

            # Case where we play rock
            if play_round[1] in rockIcons:
                # Score for playing rock
                totalScore += rockScore
                # Had to lose
                realScore += 0

                # Determine winnings
                if play_round[0] in rockIcons:
                    totalScore += drawScore
                    # Must have played scissors
                    realScore += scissorsScore

                elif play_round[0] in paperIcons:
                    totalScore += 0
                    # Must have played rock 
                    realScore += rockScore

                elif play_round[0] in scissorsIcons:
                    totalScore += winScore
                    # Must have played paper
                    realScore += paperScore

            elif play_round[1] in paperIcons:
                # Score for playing paper
                totalScore += paperScore
                # Draw score
                realScore += drawScore

                # Determine winnings
                if play_round[0] in rockIcons:
                    totalScore += winScore
                    # Must have played rock
                    realScore += rockScore

                elif play_round[0] in paperIcons:
                    totalScore += drawScore
                    # Must have played paper
                    realScore += paperScore

                elif play_round[0] in scissorsIcons:
                    totalScore += 0
                    # Must have played scissors
                    realScore += scissorsScore

            elif play_round[1] in scissorsIcons:
                # Score for playing scissors
                totalScore += scissorsScore
                # Winning score
                realScore += winScore

                # Determine winnings
                if play_round[0] in rockIcons:
                    totalScore += 0
                    # Must have played paper
                    realScore += paperScore

                elif play_round[0] in paperIcons:
                    totalScore += winScore
                    # Must have played scissors
                    realScore += scissorsScore

                elif play_round[0] in scissorsIcons:
                    totalScore += drawScore
                    # Must have played rock
                    realScore += rockScore

print(f"Total Score: {totalScore}")
print(f"Real Score : {realScore}")

