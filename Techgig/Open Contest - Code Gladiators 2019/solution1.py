''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    villainsStrengths = []
    playersEnergies = []
    numberOfTests = int(input())
    while numberOfTests > 0:
        numberOfPlayers = int(input())
        villainsStrength = input()
        playersEnergy = input()
        for strength in villainsStrength.split(" "):
            if strength != "":
                villainsStrengths.append(int(strength))
        for energy in playersEnergy.split(" "):
            if energy != "":
                playersEnergies.append(int(energy))
        villainsStrengths.sort()
        playersEnergies.sort()
        i=0
        isWin = True
        for energy in playersEnergies:
            if i < int(numberOfPlayers):
                if villainsStrengths[i] > energy:
                    isWin = False
            i += 1
        
        if isWin:
            print("WIN")
        else:
            print("LOSE")
        
        numberOfTests -= 1
    

 # Write code here 

main()

