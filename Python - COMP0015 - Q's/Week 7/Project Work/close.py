
s projectone
3
tim
kim
lim
tim
{'lim': 50, 'kim': 50}
kim
{'lim': 60, 'tim': 40}
lim
{'tim': 70, 'kim': 30}






# just need to read or need to display?????
def start():
    infile = open('votes.txt', 'rt')
    print ('The data from the previous running of this program was:')
    for line in infile:
        print(line)

def end():
    print ('No')
    
start()
end()