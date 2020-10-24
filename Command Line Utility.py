import argparse
import sys

def clac(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    if args.o == 'div':
        return args.x / args.y
    else:
        return 'Something Went Wrong...'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='Enter first number. This is utility Calculation, Please Contact Shahzaib for More Information')

    parser.add_argument('--y', type=float, default=3.0,
                        help='Enter first number. This is utility Calculation, Please Contact Shahzaib for More Information')

    parser.add_argument('--o', type=str, default='Add',
                        help='Enter first number. This is utility Calculation, Please Contact Shahzaib for More Information')

    args = parser.parse_args()
    sys.stdout.write(str(clac(args)))