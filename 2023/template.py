# import concurrent.futures
import timeit


# Specify the file path
file_path = '2023\\Day1\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(line):
    return line


def run():
    global results
    results = 0
    # Multithreading
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = sum(executor.map(process_line, lines))

    # Single Thread
    for line in lines:
        results = process_line(line)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
