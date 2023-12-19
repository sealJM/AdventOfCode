# import concurrent.futures
import timeit
import re


# Specify the file path
file_path = '2023\\Day1-Trebuchet\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(line):
    # Find all matches of the number pattern in the string
    numbers = re.findall(r'\d', line)
    if numbers:
        return int(numbers[0] + numbers[-1])


def run():
    global results
    results = 0

    # Multithreading
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = sum(executor.map(process_line, lines))

    # Single Thread
    for line in lines:
        results = results + process_line(line)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
