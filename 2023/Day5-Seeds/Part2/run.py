import timeit


def process_deltas(line, index):
    if index != 0:
        # Pre process deltas to reduce calculations needed
        for i, info in enumerate(line):
            delta, s_range, e_range = info.split(" ")
            delta, s_range, e_range = int(delta), int(s_range), int(e_range)
            delta, e_range = delta-s_range, s_range+e_range
            line[i] = [delta, s_range, e_range]
        return line
    else:
        line = list(zip(line.split(" ")[::2], line.split(" ")[1::2]))
        for i, x in enumerate(line):
            line[i] = [int(x[0]), int(x[0]) + int(x[1])]
        return line


def process_ranges(ranges, seeds):
    # Processes ranges at a time and will split them if needed
    new_seeds = []
    for i0, i1 in seeds:
        nothing = True
        for x0, x1, x2 in ranges:
            # Fits in between [...(...)...]
            if x1 <= i0 and i1 <= x2:
                new_seeds.append([i0+x0, i1+x0])
                nothing = False
            # Overhanging (...[...]...)
            elif x1 >= i0 and i1 >= x2:
                if [i0, x1-1] not in seeds:
                    seeds.append([i0, x1-1])
                if [x2+1, i1] not in seeds:
                    seeds.append([x2+1, i1])
                new_seeds.append([x1+x0, x1+x0])
                nothing = False
            # Hanging left (...[...)...]
            elif x1 >= i0 and i1 >= x1:
                if [i0, x1-1] not in seeds:
                    seeds.append([i0, x1-1])
                new_seeds.append([x1+x0, i1+x0])
                nothing = False
            # Hanging right [...(...]...)
            elif x2 >= i0 and i1 >= x2:
                if [x2+1, i1] not in seeds:
                    seeds.append([x2+1, i1])
                new_seeds.append([i0+x0, x2+x0])
                nothing = False
        if nothing:
            new_seeds.append([i0, i1])

    return new_seeds


def run():
    global results
    results = []

    file_path = '2023\\Day5-Seeds\\input.txt'
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        lines = file.read()[:-1].split("\n\n")
        for i, x in enumerate(lines):
            if i == 0:
                lines[i] = x.split(": ")[1]
            else:
                lines[i] = x.split(":\n")[1].split("\n")

    for i, line in enumerate(lines):
        lines[i] = process_deltas(line, i)

    for i in lines[1::]:
        lines[0] = process_ranges(i, lines[0])
    results = min(sublist[0] for sublist in lines[0])


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
