from Host import *
from Client import *
import sys


def main():
    script, side = sys.argv
    if side == "host":
        host()
    elif side == 'client':
        client()
    else:
        if input('Host? (y/n)').lower() == 'y':
            host()
        else:
            client()


if __name__ == '__main__':
    main()
