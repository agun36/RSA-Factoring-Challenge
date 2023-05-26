#!/usr/bin/python3
import sys

def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        number = int(number)
        factors = factorize(number)
        for factor in factors:
            print("{}={}*{}".format(number, factor[0], factor[1]))

if __name__ == "__main__":
    main()


