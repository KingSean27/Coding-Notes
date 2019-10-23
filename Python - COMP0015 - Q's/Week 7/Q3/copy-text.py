#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    
    infile = open('input.txt', 'rt')
    outfile = open('leet.txt', 'wt')
    
    for line in infile:
        list1 = line.split()
        
        for item in list1:
            word = item
            
            if word [-1:] == 's':
                word = word [:-1] + 'Z'
                
            word = word.replace('o', '0')
            word = word.replace('l','1')
            word = word.replace('e', '3')
            word = word.replace('a', '444')
            word = word.replace('t', '7')
            
            leetword = "({}) ".format(word)
            print(leetword, end='', file=outfile)
        print ("", file=outfile)
      
        print('.', end='', flush=True)
         
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
