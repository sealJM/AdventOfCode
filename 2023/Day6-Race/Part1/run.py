# import concurrent.futures
from functools import reduce
from operator import mul
import timeit
import cmath


def process_line(time, distance):
    # This problem deals with pure ints and no rounding
    discriminant = cmath.sqrt(time**2 - 4*distance)
    root1 = ((time + discriminant) / (2))
    root2 = ((time - discriminant) / (2))

    return int(root1.real) - int(root2.real)

    # # Brute force method
    # ways = 0
    # for s in range(1, time):
    #     if s*(time-s) >= distance:
    #         ways += 1
    # return ways


def run():
    global results
    results = []

    # Specify the file path
    file_path = '2023\\Day6-Race\\input.txt'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        races = [line.rstrip('\n').split()[1::] for line in file]

    # Calculate max and min values
    for i, race in enumerate(races[0]):
        results.append(process_line(int(race), int(races[1][i])))
    results = reduce(mul, results)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(results)
    print(f"Execution time: {execution_time} seconds")
