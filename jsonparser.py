#!/usr/bin/env python 

import argparse
import json

def printnlines(filename, nlines):
    data, lines = loadfile(filename)
    for item in lines[:nlines]:
        print item

def loadfile(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    lines = json.dumps(data, indent=4).split('\n')
    return data, lines

if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='A program to parse and explore json files')
    parser.add_argument('-f', '--filename',
                        help='Filename of json file',
                        required=True)
    parser.add_argument('-n', '--nlines',
                        help='Number of lines to print from file',
                        required=False)
    
    args = vars(parser.parse_args())
    
    filename = args['filename']
    
    if args['nlines']:
        nlines = int(args['nlines'])
    else:
        nlines = None

    printnlines(filename, nlines)

