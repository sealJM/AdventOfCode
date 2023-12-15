import timeit
import concurrent.futures

# Specify the file path
file_path = '2023\\Day1\\input.txt'
global results

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(line):
    first = ""
    last = ""
    reverse = False
    for c in line:
        # if (first.isdigit() and last.isdigit()):
        #     break
        # else:
        if True:
            if (c.isdigit() and not first.isdigit()):
                first = c
                reverse = True
            if (c.isdigit() and reverse):
                last = c
    if first+last != "":
        return int(first+last)


def run():
    global results
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = sum(executor.map(process_line, lines))


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
