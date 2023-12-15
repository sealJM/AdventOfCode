import timeit
import concurrent.futures

# Specify the file path
file_path = '2023\\Day1\\Part1\\input.txt'
global results

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read lines and store them in a list
    lines = [line.rstrip('\n') for line in file]


def process_line(x):
    first = ""
    last = ""
    reverse = False
    for s in x:
        # if (first.isdigit() and last.isdigit()):
        #     break
        # else:
        if True:
            if (s.isdigit() and not first.isdigit()):
                first = s
                reverse = True
            if (s.isdigit() and reverse):
                last = s
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
