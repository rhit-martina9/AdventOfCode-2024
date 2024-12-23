input = []

with open("day22.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append(int(line))

def mix(num1,num2):
    return num1 ^ num2
def prune(num):
    return num & 0xFFFFFF
def evolve(num):
    val = prune(mix(num,num<<6))
    val = prune(mix(val,val>>5))
    val = prune(mix(val,val<<11))
    return val

def part_one():
    total = 0
    for num in input:
        for _ in range(2000):
            num = evolve(num)
        total += num
    return total

def get_prices(num,count=2000):
    out = [num % 10]
    for _ in range(count):
        num = evolve(num)
        out.append(num % 10)
    return out

def get_price_changes(prices,count=2000):
    out = []
    for i in range(count):
        out.append(prices[i+1]-prices[i])
    return out

def get_payouts(num):
    prices = get_prices(num)
    price_changes = get_price_changes(prices)
    out = {}
    for i in range(len(price_changes)-3):
        key = (price_changes[i],price_changes[i+1],price_changes[i+2],price_changes[i+3])
        if key not in out:
            out[key] = prices[i+4]
    return out

def part_two():
    payouts = [get_payouts(num) for num in input]
    sequences = set()
    for payout in payouts:
        sequences = sequences.union(set(payout.keys()))
        
    best_total = 0
    for sequence in sequences:
        total = 0
        for payout in payouts:
            if sequence in payout:
                total += payout[sequence]
        if total > best_total:
            best_total = total
    return best_total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two()) #1923 too low
    