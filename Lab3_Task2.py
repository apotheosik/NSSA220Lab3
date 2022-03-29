# Chris Sequeira 1 April 2022
import sys

#parse file to list of rows in [name, hash] format
def readFile(filename):
    hashes = []
    with open(filename, 'r') as file:
        for line in file:
            hashes.append(line.strip().split())
    return hashes

#iterate through both lists, return output when rows are not identical
def compare(binHashesOG, binHashesNew):
    i = 0
    while i < len(binHashesOG):
        if binHashesOG[i] != binHashesNew[i]:
            print(binHashesOG[i][0], ": md5 original= ", binHashesOG[i][1], ", md5 new= ", binHashesNew[i][1])
        i += 1

if __name__ == '__main__':
    print("This output assumes you passed the original hashes before the newer hashes.")
    compare(readFile(sys.argv[1]), readFile(sys.argv[2]))
