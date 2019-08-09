from argparse import ArgumentParser

from package.app import run

if __name__ == '__main__':

    parser = ArgumentParser(description="Smart XML analyzer.")
    parser.add_argument('origin', type=str, help='Path to the origin file.')
    parser.add_argument('other', type=str, help='Path to the other file.')

    args = parser.parse_args()

    x = run(args.origin, args.other)
