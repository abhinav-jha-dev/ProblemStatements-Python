''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

elements = []
def maxSum(arr, N, k):

    # MS[i] is going to store maximum sum
    # subsequence in subarray from arr[i]
    # to arr[n-1]
    MS = [0 for i in range(N)]

    # We fill MS from right to left.
    MS[N - 1] = arr[N - 1]
    for i in range(N - 2, -1, -1):
        if (i + k + 1 >= N):
            MS[i] = max(arr[i], MS[i + 1])
            elements.append(arr[i])
        else:
            MS[i] = max(arr[i] + MS[i + k + 1],
                        MS[i + 1])
            elements.append(arr[i])

    return MS


def main():
    numberOfTests = int(input())
    while numberOfTests > 0:
        numberOfHouses = int(input())
        ticketValues = input()
        originalValues = []

        for ticket in ticketValues.split(" "):
            if ticket != "" and numberOfHouses > 0:
                originalValues.append(int(ticket))
                numberOfHouses -= 1

        print(maxSum(originalValues, len(originalValues), 1))
        print(elements)

        numberOfTests -= 1

 # Write code here
main()
