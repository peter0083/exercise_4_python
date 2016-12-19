import argparse
import math

def square_root(n):
    if n >= 0:
        return math.sqrt(n)


parser = argparse.ArgumentParser()
parser.add_argument("num", help="display the square root of the given number", type=int)
args = parser.parse_args()
print(square_root(args.num))
