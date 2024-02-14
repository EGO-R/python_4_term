from math import atan, pow

def main(y, z):
    return 7 + pow(67 * pow(y, 3) - 4 * pow(z, 2), 4) + atan(z) + (0.03 - 20 * y^3 - 79 * z)^5

if __name__ == '__main__':
    print(main(-0.97, 0.63))
    print(main(0.09, 0.79))
    print(main(0.01, 0.03))
    print(main(0.37, 0.25))
    print(main(0.44, 0.31))


