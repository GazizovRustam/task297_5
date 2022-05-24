def estimatedValue(price):
    estimated = price * 0.60
    return estimated


def main():
    price = float(input('Please enter price home: '))
    total = estimatedValue(price)
    return total

main()

