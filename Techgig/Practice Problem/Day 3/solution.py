''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def CalculateSimpleInterest(principal, Interest, Year):
    return round((principal*Interest*Year)/100)

def main():
    a = float(input())
    b = int(input())
    c = int(input())

    print(CalculateSimpleInterest(a,b,c), end="")
    # Write code here 

main()
