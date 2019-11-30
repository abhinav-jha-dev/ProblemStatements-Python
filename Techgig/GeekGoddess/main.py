''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
class PeopleType(object):
    def __init__(self, type):
        self.type = type
        self.count = 1
    
    def incrementCount():
        self.count += 1

def main():

    testCases = input()
    for case in testCases:
        publicTypes = []
        publicData = input()
        for people in publicData:
            if (publicTypes.):
                publicTypes[publicTypes.index(PeopleType(people))].incrementCount()
            else:
                publicTypes.append(PeopleType(people))

    for people in publicTypes:
        print(people.type)
        print(people.count)
 # Write code here 

main()