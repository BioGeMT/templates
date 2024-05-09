import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Process some data.')
    parser.add_argument('--ifile', type=str, help='Input file name')
    parser.add_argument('--ofile', type=str, help='Output file name')

    args = parser.parse_args()

    # Setting up input: file if specified, otherwise stdin
    if args.ifile:
        infile = open(args.ifile, 'r')
    else:
        infile = sys.stdin

    # Setting up output: file if specified, otherwise stdout
    if args.ofile:
        outfile = open(args.ofile, 'w')
    else:
        outfile = sys.stdout

    # Process data
    for line in infile:
        # Modify this part to perform any specific processing
        outfile.write(line)

    # Close the files if they were opened
    if infile is not sys.stdin:
        infile.close()
    if outfile is not sys.stdout:
        outfile.close()

if __name__ == '__main__':
    main()
