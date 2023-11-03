#!/usr/bin/python3
a = 10
b = 5

if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    print("{:d} + {:d} = {:d}".format(a, b, add))
    print("{:d} - {:d} = {:d}".format(a, b, subtract))
    print("{:d} * {:d} = {:d}".format(a, b, multiply))
    print("{:d} / {:d} = {:d}".format(a, b, divide))
