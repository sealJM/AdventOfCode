# import concurrent.futures
import timeit
from functools import reduce


# Specify the file path
file_path = '2023\\Day2\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(line):
    rule = {"red": 0, "green": 0, "blue": 0}
    line = ", ".join(line.split(": ")[1].split("; ")).split(", ")
    for i in line:
        quantity, color = i.split(" ")
        if int(quantity) > rule[color]:
            rule[color] = int(quantity)
    return reduce(lambda x, y: x * y, rule.values())


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
