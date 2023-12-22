import timeit


def process_network(instructions, network, step="AAA"):
    lr_map = {"L": 0, "R": 1}
    for i, x in enumerate(instructions, start=1):
        step = network[step][lr_map[x]]
        if step == "ZZZ":
            return i
    return i + process_network(instructions, network, step)


def run():
    global results
    results = 0

    # Specify the file path
    file_path = '2023\\Day8-LeftRight\\input.txt'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        instructions, network = file.read().split("\n\n")
    network = network.split("\n")
    network = {step[0:3]: [step[7:10], step[12:15]] for step in network[:-1]}

    # for line in lines:
    results = process_network(instructions, network)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
