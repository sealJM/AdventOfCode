import timeit


def process_line(line):
    power = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,
        "Q": 12, "K": 13, "A": 14
    }
    hand, bet = line.split()
    char_count = {}
    pairs = 0
    cards = []
    for char in hand:
        cards.append(power[char])
        char_count[char] = char_count.get(char, 0) + 1
    for i in char_count:
        if char_count[i] == 2:
            pairs += 1
        elif char_count[i] == 3:
            pairs += 3
        elif char_count[i] == 4:
            pairs += 5
        elif char_count[i] == 5:
            pairs += 6
    power = [pairs] + cards
    return [power, bet]


def run():
    global total
    total = 0
    results = []

    # Specify the file path
    file_path = '2023\\Day7-CamelCards\\input.txt'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read lines and store them in a list
        lines = [line.rstrip('\n') for line in file]

    for line in lines:
        results.append(process_line(line))
    results = sorted(results, key=lambda x: x[0])
    for i, rank in enumerate(results):
        total += int(rank[1])*(i+1)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(total)
    print(f"Execution time: {execution_time} seconds")
