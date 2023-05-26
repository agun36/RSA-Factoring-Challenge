#!/usr/bin/python3
import sys
import math

def factors(filename):
    with open(filename, 'r') as f:
        for line in f:
            n = int(line.strip())
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    print(f"{n}={i}*{n//i}")
                    break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    factors(sys.argv[1])


