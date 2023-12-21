import timeit


def process_deltas(line):
    # Pre process deltas to reduce calculations needed
    for i, info in enumerate(line):
        delta, s_range, e_range = info.split(" ")
        delta, s_range, e_range = int(delta), int(s_range), int(e_range)
        delta, e_range = delta-s_range, s_range+e_range
        line[i] = [delta, s_range, e_range]
    return line


def process_seed(lines, seed, level=1):
    # Using recursion, process seeds found
    max = 7
    for i in lines[level]:
        if seed >= i[1] and seed <= i[2]:
            location = seed+i[0]
            if level < max:
                location = process_seed(lines, seed+i[0], level+1)
            return location
    location = seed
    if level < max:
        location = process_seed(lines, seed, level+1)
    return location


def run():
    global results
    results = []

    file_path = '2023\\Day5-Seeds\\input.txt'
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        lines = file.read().split("\n\n")
        for i, x in enumerate(lines):
            if i == 0:
                lines[i] = x.split(": ")[1]
            else:
                lines[i] = x.split(":\n")[1].split("\n")

    # Single Thread
    for i, line in enumerate(lines[1::], 1):
        lines[i] = process_deltas(line)

    all_seed_numbers = []

    '''Generate all seed numbers based on the ranges provided.
        In theory this should work but, this cant even finish this segment
        without running out of memory'''
    for i in range(0, len(lines[0].split(" ")), 2):
        start, length = int(lines[0].split(" ")[i]), int(
            lines[0].split(" ")[i + 1])
        all_seed_numbers.extend(range(start, start + length))

    for seed in all_seed_numbers:
        results.append(process_seed(lines, int(seed)))
    results = min(results)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1))/1
    print(results)
    print(f"Execution time: {execution_time} seconds")
