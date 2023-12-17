# import concurrent.futures
import timeit


# Specify the file path
file_path = '2023\\Day2\\input.txt'


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(line):
    rule = {"red": 12, "green": 13, "blue": 14}
    game = int(line.split(": ")[0].split(" ")[1])
    line = ", ".join(line.split(": ")[1].split("; ")).split(", ")
    for i in line:
        quantity, color = i.split(" ")
        if int(quantity) > rule[color]:
            return 0
    return game


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
