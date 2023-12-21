# import concurrent.futures
import timeit


def process_line(line):
    return line


def run():
    global results
    results = 0

    # Specify the file path
    file_path = '2023\\Day7-CamelCards\\input.txt'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        lines = [line.rstrip('\n') for line in file]

    # for line in lines:
    results = process_line(lines)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
