import timeit


def process_line(line):
    # Will take the hand and convert it to a power value
    power = {
        "J": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
        "Q": 11, "K": 12, "A": 13
    }

    hand, bet = line.split()
    # Length and uniques are used to find power value
    if "J" in hand:
        return [process_j(hand, power), bet]
    else:
        hand = [power[i] for i in hand]
        char_count = len(set(hand))
        if char_count == 1:
            pairs = 6
        elif char_count == 2:
            for i in set(hand):
                if hand.count(i) > 3:
                    pairs = 5
                    break
                else:
                    pairs = 4
        elif char_count == 3:
            for i in set(hand):
                if hand.count(i) > 2:
                    pairs = 3
                    break
                else:
                    pairs = 2
        elif char_count == 4:
            pairs = 1
        elif char_count == 5:
            pairs = 0

        power = [pairs] + hand
        return [power, bet]


def process_j(hand, power):
    # Old way used a loop in spots when not needed
    char_count = {}
    pairs = 0
    cards = []
    # Convert cards to power values and count cards
    for char in hand:
        cards.append(power[char])
        char_count[char] = char_count.get(char, 0) + 1
    # Return number of J cards and remove from set
    j = char_count.pop("J")
    if char_count:
        #  Add number of J cards to highest set found
        char_count[max(char_count, key=char_count.get)] += j
        for i in char_count:
            if char_count[i] == 2:
                pairs += 1
            elif char_count[i] == 3:
                pairs += 3
            elif char_count[i] == 4:
                pairs += 5
            elif char_count[i] == 5:
                pairs += 6
    else:
        # If all cards are J
        pairs = 6
    return [pairs]+cards


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

    # Sorts the results based on the list containing power
    results = sorted(results, key=lambda x: x[0])
    for i, rank in enumerate(results):
        total += int(rank[1])*(i+1)


if __name__ == "__main__":
    execution_time = (timeit.timeit(run, number=1000))/1000
    print(total)
    print(f"Execution time: {execution_time} seconds")
