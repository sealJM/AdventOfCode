# import concurrent.futures
import timeit


# Specify the file path
file_path = '2023\\Day1\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(line):
    number_map = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }

    numbers = {}

    for key in number_map.keys():
        index = line.find(key)
        # if index != -1:
        while index != -1:
            numbers[index] = number_map[key]
            index = line.find(key, index + 1)

    for i, x in enumerate(line):
        if x.isdigit():
            numbers[i] = x
    return int(f"{numbers[min(numbers)]}{numbers[max(numbers)]}")


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
