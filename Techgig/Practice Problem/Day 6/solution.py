''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    inputValue = int(input())
    numberOfDigit=0
    while inputValue>0:
        test = round(inputValue/10)
        numberOfDigit+=1
        inputValue = test
    
    print(numberOfDigit, end="")
 # Write code here 

main()

