# import concurrent.futures
import timeit
import re


# Specify the file path
file_path = '2023\\Day1\\input.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]

# lines = ["sevenseven7eightoneightvvj"]


def process_line(line):
    number_map = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }
    # TODO findall does not include overlapping words
    # Find all matches of the number pattern in the string
    word_pattern = r'one|two|three|four|five|six|seven|eight|nine'
    digit_pattern = r'\d'
    search = f'{word_pattern}|{digit_pattern}'
    numbers = re.findall(search, line)
    if numbers:
        first = (number_map[numbers[0]] if numbers[0]
                 in number_map else numbers[0])
        last = (number_map[numbers[-1]] if numbers[-1]
                in number_map else numbers[-1])
        # print(int(first+last))
        return int(first+last)


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
    execution_time = (timeit.timeit(run, number=1))/1
    print(results)
    print(f"Execution time: {execution_time} seconds")
