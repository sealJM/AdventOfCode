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
    # This works but I don't think it should
    new_seeds = []
    for i in seeds:
        nothing = True
        for scope in ranges:
            # Fits in between [...(...)...]
            if scope[1] <= i[0] and i[1] <= scope[2]:
                new_seeds.append([i[0]+scope[0], i[1]+scope[0]])
                nothing = False
            # Hanging left (...[...)...]
            elif scope[1] >= i[0] and i[1] >= scope[1]:
                new_seeds.append([scope[1]+scope[0], i[1]+scope[0]])
                nothing = False
            # Hanging right [...(...]...)
            elif scope[2] >= i[0] and i[1] >= scope[2]:
                new_seeds.append([i[0]+scope[0], scope[2]+scope[0]])
                nothing = False
            # Overhanging (...[...]...)
            elif scope[1] >= i[0] and i[1] >= scope[2]:
                new_seeds.append([i[0], scope[1]-1])
                new_seeds.append([scope[1]+scope[0], scope[1]+scope[0]])
                new_seeds.append([scope[2]+1, i[1]])
                nothing = False
        if nothing:
            new_seeds.append([i[0], i[1]])

    return new_seeds


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

    for i, line in enumerate(lines):
        lines[i] = process_deltas(line, i)

    for i in lines[1::]:
        lines[0] = process_ranges(i, lines[0])
    results = min(sublist[0] for sublist in lines[0])


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1))/1
    print(results)
    print(f"Execution time: {execution_time} seconds")
