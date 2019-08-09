from argparse import ArgumentParser

from package.app import run

if __name__ == '__main__':

    parser = ArgumentParser(description="Smart XML analyzer.")
    parser.add_argument('origin', type=str, help='Path to the origin file.')
    parser.add_argument('other', type=str, help='Path to the other file.')
    parser.add_argument('element_id', type=str, help='Id of the element to search.')

    args = parser.parse_args()

    x = run(args.origin, args.other, args.element_id)
