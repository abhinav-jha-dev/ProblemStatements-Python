''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    factorial = 1
    initialValue = int(input())
    while initialValue > 1:
        factorial *= initialValue
        initialValue = initialValue - 1
    
    print(factorial,end="")
    # Write code here 

main()