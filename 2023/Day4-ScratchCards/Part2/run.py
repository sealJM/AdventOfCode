import timeit

# Specify the file path
file_path = '2023\\Day4-ScratchCards\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = []
    for line in file:
        lines = lines + [line.rstrip('\n').split(": ")[1]]


def process_line(lines):
    result = 0
    wins = [0]
    for i in lines:
        # Resets the list if no wins are left
        if len(wins) == 0:
            wins = [0]

        # Includes the given card
        wins[0] += 1

        # Checks winning numbers
        winners, numbers = i.replace("  ", " ").split(" | ")
        winners = len(set(numbers.split()) & set(winners.split()))

        # Manages list of won cards
        for x in range(1, winners+1):
            if x < len(wins):
                wins[x] += (wins[0])
            else:
                wins.append(wins[0])

        # Pops checked cards and adds to total
        result += (wins.pop(0))
    return result


def run():
    global results
    results = process_line(lines)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
