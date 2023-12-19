import timeit


# Specify the file path
file_path = '2023\\Day1-Trebuchet\\input.txt'


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
    results = 0
    for line in lines:
        results = results + process_line(line)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
