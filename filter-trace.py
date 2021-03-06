#!/usr/bin/env python

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file", help="trace file to process")
parser.add_argument("-s", help="start filter from this second", type=int, default=0)
parser.add_argument("-f", help="finish filter until this second", type=int, default=0)
args = parser.parse_args()

start = args.s * 1000 # convert to ms
finish = args.f * 1000
with open(args.file) as f:
	for line in f:
		token = line.split(" ")
		time = float(token[0].strip())
		if time < start:
			continue
		if time > finish:
			break
		sys.stdout.write(line)
