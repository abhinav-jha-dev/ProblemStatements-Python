import numpy as np

def find_nearest(array, values):
    indices = np.abs(np.subtract.outer(array, values)).argmin(0)
    return array[indices]
def main():
    numberOfTests = int(input())
    numberOfPlayers = int(input())
    numberOfGMembers = input().split()
    numberOfOppMembers = input().split()
    numberOfGMembers = list(map(int,numberOfGMembers))
    numberOfOppMembers = sorted(map(int,numberOfOppMembers))
    numberOfWins = 0
    print(numberOfGMembers)
    print(numberOfOppMembers)
    for test in range(0,numberOfTests):
        # print(get_closest(numberOfOppMembers,numberOfGMembers))
        for player in range(0, numberOfPlayers):
            source = numberOfOppMembers
            idx = find_nearest(source,numberOfGMembers[player])
            if idx>-1:
                numberOfOppMembers.remove(numberOfOppMembers[idx])
                numberOfWins = numberOfWins + 1
            print(numberOfWins)


 # Write code here 

main()