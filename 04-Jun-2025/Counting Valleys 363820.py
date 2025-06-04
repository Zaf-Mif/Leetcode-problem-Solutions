# Problem: Counting Valleys - https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    altitude = 0
    valleys = 0

    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1
        elif step == 'D':
            altitude -= 1

    return valleys

# Sample test
steps = 8
path = "UDDDUDUU"
print(countingValleys(steps, path))  # Output: 1
