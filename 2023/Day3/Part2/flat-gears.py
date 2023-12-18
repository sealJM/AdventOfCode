# import concurrent.futures
import timeit
import re


# Specify the file path
file_path = '2023\\Day3\\input.txt'


# Open the file in read mode and flatten to one string
with open(file_path, 'r') as file:
    first = file.readline().replace('\n', "")
    lines = first + file.read().replace('\n', "")
    length = len(first)


def scan(index):
    line = index // length
    results = []
    # Welcome to spaghetti hell
    for x in range(-1, 2):
        i = index+(length*x)
        x = (line+x)*length
        ahead = 1
        back = 1
        while lines[i-back].isdigit() and (i-back) >= x:
            back += 1
        while lines[i+ahead].isdigit() and (i+ahead) < (x+length):
            ahead += 1
        results.append(lines[i-back+1:i+ahead])
    results = re.findall(r'\d+', ",".join(results))
    if len(results) == 2:
        results = int(results[0])*int(results[1])
    else:
        return 0
    return results


def run():
    global results
    results = 0
    # Multithreading, unsure if can be
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = sum(executor.map(process_line, lines))

    for i, x in enumerate(lines):
        if x != "." and not x.isdigit():
            results = results + scan(i)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=100))/100
    print(results)
    print(f"Execution time: {execution_time} seconds")
