"""
Calculate Random Python Function for Electron App
"""

__author__ = 'Omar'


from sys import argv

# lets change to argparse


def main():
    print(f'{int(argv[1]) ** 2 } is the number entered, squared.')


if __name__ == '__main__':
    main()
