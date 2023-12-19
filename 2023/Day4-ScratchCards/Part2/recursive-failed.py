# import concurrent.futures
import timeit
# Specify the file path
file_path = '2023\\Day4-ScratchCards\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = []
    for line in file:
        lines = lines + [line.rstrip('\n').split(": ")[1]]


def process_line(index=0, end=len(lines)):
    global results
    global lines

    for i in range(index, end):
        wins = 0
        if i >= len(lines):
            break
        winners, numbers = lines[i].replace("  ", " ").split(" | ")
        for x in numbers.split():
            if x in winners.split():
                wins += 1
        if wins > 0:
            results = results + wins
            process_line(i+1, i+wins+1)
    if index == 65:
        print(index)


def run():
    global results
    results = 0
    # Multithreading
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = sum(executor.map(process_line, lines))

    # Single Thread
    process_line()


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1))/1
    print(results)
    print(f"Execution time: {execution_time} seconds")
