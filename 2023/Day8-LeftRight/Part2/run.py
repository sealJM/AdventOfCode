from math import lcm
import timeit


def process_network(inst, network, steps, lengths=[], count=0):
    # Will add to a list containing the minimum steps for ending Z
    lr_map = {"L": 0, "R": 1}
    for i, x in enumerate(inst, start=1):
        steps = [network[step][lr_map[x]] for step in steps]
        for z, x in enumerate(steps):
            if x[-1] == "Z":
                steps.pop(z)
                lengths.append(i+count)
        if not steps:
            return lengths
    return process_network(inst, network, steps, lengths, i+count)


def run():
    global results
    results = 0

    # Specify the file path
    file_path = '2023\\Day8-LeftRight\\input.txt'

    # Open the file in read mode and format data
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        inst, network = file.read().split("\n\n")
    network = network.split("\n")
    network = {step[0:3]: [step[7:10], step[12:15]] for step in network[:-1]}

    # Groups lines ending with A
    starts = list(network.keys())
    starts = [step for step in starts if step[-1] == "A"]

    # LCM because path lengths are divisible by instruction set
    results = lcm(*process_network(inst, network, starts))


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
