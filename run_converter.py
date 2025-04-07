import argparse
from convert_fu6 import convert_fu6
from convert_bin import convert_bin

parser = argparse.ArgumentParser()
parser.add_argument('--type', required=True, choices=['fu6', 'bin'])
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
parser.add_argument('--shape', required=True)
args = parser.parse_args()

if args.type == 'fu6':
    convert_fu6(args.input, args.output, args.shape)
elif args.type == 'bin':
    convert_bin(args.input, args.output, args.shape)
