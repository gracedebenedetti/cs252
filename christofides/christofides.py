'''
christofides.py

Grace de Benedetti and John Witte implementation of Christofides' Algorithm for CS252: Algorithms

June 7th, 2021
'''

def readPaths():
    "reads paths and weights from data file into dictionary"
    paths = [line.strip().lower() for line in open('paths.txt')]
    pathsDict = {}
    for path in paths:
        pathsDict[path[:3]] = int(path[4:])
    return (pathsDict)

#find MST
    #prims implementation

#odd vertices

#perfect matches
    #brute force possibility

#Eulerian tour

#Hamiltonian circuit

def main():
    readPaths()

if __name__ == '__main__':
    main()
