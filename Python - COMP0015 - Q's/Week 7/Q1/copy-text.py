#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    n = 1
    prev = ""
    infile = open('poem.txt', 'rt')
    outfile = open('flippedpoem.txt', 'wt')
    
    for line in infile:
        if n % 2 == 0:
            print(line.rstrip(), file=outfile)
            print(prev.rstrip(), file=outfile)
            print('.', end='', flush=True)
            n += 1
        else:
            prev = line
            n+=1
                
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
