# import concurrent.futures
import timeit
# Specify the file path
file_path = '2023\\Day4\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = []
    for line in file:
        lines = lines + [line.rstrip('\n').split(": ")[1]]


def process_line(line):
    wins = -1
    winners, numbers = line.replace("  ", " ").split(" | ")
    for i in numbers.split():
        if i in winners.split():
            wins += 1
    if wins >= 0:
        return int(1 << wins)
    # print(f"{winners.split()} and {numbers.split()}")
    else:
        return 0


def run():
    global results
    results = 0
    # Multithreading
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = sum(executor.map(process_line, lines))

    # Single Thread
    for line in lines:
        # process_line(line)
        results = results + process_line(line)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
