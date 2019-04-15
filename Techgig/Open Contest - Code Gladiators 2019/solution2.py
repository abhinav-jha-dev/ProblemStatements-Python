''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT


def maxSubArraySum(a, size):
    elementsSoFar = []
    even_elementsSoFar = []
    odd_elementsSoFar = []
    max_so_far = 0
    even_max_so_far = 0
    odd_max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        if i % 2 == 0:
            max_ending_here = max_ending_here + a[i]
            if max_ending_here < 0:
                max_ending_here = 0

            # Do not compare for all elements. Compare only
            # when  max_ending_here > 0
            elif (even_max_so_far < max_ending_here):
                even_elementsSoFar.append(a[i])
                even_max_so_far = max_ending_here

    max_ending_here = 0

    for i in range(0, size):
        if i % 2 != 0:
            max_ending_here = max_ending_here + a[i]
            if max_ending_here < 0:
                max_ending_here = 0

            # Do not compare for all elements. Compare only
            # when  max_ending_here > 0
            elif (odd_max_so_far < max_ending_here):
                odd_elementsSoFar.append(a[i])
                odd_max_so_far = max_ending_here

    if odd_max_so_far < even_max_so_far:
        elementsSoFar.append(even_elementsSoFar)
        max_so_far = even_max_so_far
    elif odd_max_so_far == even_max_so_far:
        if odd_elementsSoFar[(len(odd_elementsSoFar)-1)] < even_elementsSoFar[(len(even_elementsSoFar)-1)]:
            elementsSoFar.append(even_elementsSoFar)
        else:
            elementsSoFar.append(odd_elementsSoFar)
    else:
        elementsSoFar.append(odd_elementsSoFar)
        max_so_far = odd_max_so_far
    return elementsSoFar[0]


def main():
    numberOfTests = int(input())
    while numberOfTests > 0:
        numberOfHouses = int(input())
        ticketValues = input()
        originalTicketValues = []
        index = 1

        for ticket in ticketValues.split(" "):
            if ticket != "" and index <= numberOfHouses:
                originalTicketValues.append(int(ticket))

        maxvalue = maxSubArraySum(
            originalTicketValues, len(originalTicketValues))
        
        for i in reversed(maxvalue):
            print(i, end='')
        
        print()
        numberOfTests -= 1


 # Write code here
main()
